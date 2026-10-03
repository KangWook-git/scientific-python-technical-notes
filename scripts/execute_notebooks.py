"""Run all notebooks in fresh IPython processes, or use real Jupyter kernels.

python scripts/execute_notebooks.py
python scripts/execute_notebooks.py --engine kernel

The default process engine requires no notebook-server sockets. It captures
stdout, errors, explicit rich displays, and Matplotlib figures. Each notebook
has an independent namespace. The kernel engine uses nbclient instead.
"""
from pathlib import Path
import json,sys,time,platform,importlib.metadata,re,subprocess,argparse,os
import nbformat

root=Path(__file__).resolve().parents[1]

def run_worker(path):
    import io
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from IPython.core.interactiveshell import InteractiveShell
    from IPython.utils.capture import capture_output
    from IPython.display import display,Image
    shell=InteractiveShell.instance()
    def capture_figures(*args,**kwargs):
        for num in list(plt.get_fignums()):
            buffer=io.BytesIO()
            plt.figure(num).savefig(buffer,format='png',bbox_inches='tight')
            display(Image(data=buffer.getvalue()))
            plt.close(num)
    plt.show=capture_figures
    notebook=nbformat.read(path,as_version=4)
    os.chdir(root)
    count=0
    for cell in notebook.cells:
        if cell.cell_type!='code':continue
        count+=1
        cell.outputs=[]
        cell.execution_count=count
        with capture_output(stdout=True,stderr=True,display=True) as captured:
            result=shell.run_cell(cell.source,store_history=True)
        if captured.stdout:cell.outputs.append(nbformat.v4.new_output('stream',name='stdout',text=captured.stdout))
        if captured.stderr:cell.outputs.append(nbformat.v4.new_output('stream',name='stderr',text=captured.stderr))
        for item in captured.outputs:
            cell.outputs.append(nbformat.v4.new_output('display_data',data=item.data,metadata=item.metadata or {}))
        error=result.error_before_exec or result.error_in_exec
        if error:
            raise RuntimeError(f'{path.name}, code cell {count}: {type(error).__name__}: {error}\n{captured.stdout}\n{captured.stderr}')
    nbformat.validate(notebook)
    nbformat.write(notebook,path)

parser=argparse.ArgumentParser()
parser.add_argument('--engine',choices=['process','kernel'],default='process')
parser.add_argument('--worker',type=Path)
args=parser.parse_args()
if args.worker:
    run_worker(args.worker.resolve())
    sys.exit(0)

from nbconvert import HTMLExporter
(root/'html').mkdir(exist_ok=True)
(root/'docs').mkdir(exist_ok=True)
rows=[]
files=sorted((root/'notebooks').glob('*.ipynb'),key=lambda p:(int(re.search(r'_P(\d+)',p.name).group(1)),p.name))
for path in files:
    start=time.perf_counter()
    print('Executing',path.name,flush=True)
    row={'notebook':path.name,'status':'failed'}
    try:
        if args.engine=='process':
            env=os.environ.copy();env['OPENBLAS_NUM_THREADS']='1';env['OMP_NUM_THREADS']='1'
            completed=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--worker',str(path)],
                                     cwd=root,env=env,capture_output=True,text=True,timeout=240)
            if completed.returncode:raise RuntimeError(completed.stdout+'\n'+completed.stderr)
            nb=nbformat.read(path,as_version=4)
        else:
            from nbclient import NotebookClient
            nb=nbformat.read(path,as_version=4)
            for cell in nb.cells:
                if cell.cell_type=='code':cell.outputs=[];cell.execution_count=None
            NotebookClient(nb,timeout=180,kernel_name='python3',allow_errors=False,
                           resources={'metadata':{'path':str(root)}}).execute()
            nbformat.validate(nb)
            nbformat.write(nb,path)
        body,_=HTMLExporter(template_name='lab',exclude_input=False).from_notebook_node(nb)
        (root/'html'/path.with_suffix('.html').name).write_text(body,encoding='utf-8')
        row.update(status='passed',code_cells=sum(c.cell_type=='code' for c in nb.cells),
                   executed_cells=sum(c.cell_type=='code' and c.execution_count is not None for c in nb.cells),
                   error_outputs=sum(o.get('output_type')=='error' for c in nb.cells for o in c.get('outputs',[])),
                   seconds=round(time.perf_counter()-start,2))
    except Exception as exc:
        row['error']=str(exc);rows.append(row)
        (root/'docs/execution_report.json').write_text(json.dumps(rows,indent=2))
        print('FAILED:',path.name,exc,flush=True);sys.exit(1)
    rows.append(row)
    print('Passed',row['code_cells'],'cells in',row['seconds'],'s',flush=True)
rows.sort(key=lambda r:(int(re.search(r'_P(\d+)',r['notebook']).group(1)),r['notebook']))
versions={p:importlib.metadata.version(p) for p in ['numpy','scipy','pandas','matplotlib','sympy','nbformat','nbclient','nbconvert','ipykernel','ipython']}
report={'version':'1.0.0','python':sys.version,'platform':platform.platform(),'packages':versions,'engine':args.engine,
        'method':'Fresh independent IPython subprocess for each notebook; code errors disallowed; stdout and rich displays captured, figures rendered with Matplotlib Agg. Real Jupyter-kernel execution is an optional separate engine. Added assertions assess selected independent identities and references. No experimental validation is claimed.' if args.engine=='process' else 'Fresh Jupyter kernel for each notebook via nbclient; cell errors disallowed.',
        'notebooks':rows}
(root/'docs/execution_report.json').write_text(json.dumps(report,indent=2))
text='# Execution and verification report\n\nTested with Python '+platform.python_version()+'. Engine: '+args.engine+'.\n\n'+report['method']+'\n\n| Notebook | Result | Executed code cells | Seconds |\n|---|---|---:|---:|\n'
for r in rows:text+=f"| {r['notebook']} | {r['status']} | {r['executed_cells']} | {r['seconds']} |\n"
text+='\n## Tested package versions\n\n'+'\n'.join(f'- {k}: {v}' for k,v in versions.items())
text+='\n\nExecution establishes that these examples run in the recorded environment. Added checks cover selected basis invariants, flux balance, refinement order, operator equivalence, time integration, and sensitivities. This is not an all-platform compatibility test or experimental validation of the illustrative wood laws. Caught invalid-input examples and deliberately failed conservation diagnostics remain pedagogical output. Timing and iteration counts can vary. The process engine is sufficient for this Python-only series but does not test GUI backends, notebook-server networking, widgets, or Jupyter frontend rendering.\n'
(root/'docs/VERIFICATION_REPORT.md').write_text(text)
print('All',len(rows),'notebooks passed.',flush=True)
