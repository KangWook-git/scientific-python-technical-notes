# Scientific Python Technical Notes

## From Mathematical Meaning to Verified Computation

**Wook Kang · Revised English edition · Version 1.0.0 · 3 October 2026**

This collection is a working reference for understanding scientific Python through the structure of a calculation. It connects a mathematical question to a numerical object, an array representation, an algorithm, and evidence about the result. It grew from notes prepared for wood science and multiphysics research, but most examples are general engineering calculations.

The purpose is to preserve an accessible record of the reasoning that conventional package catalogues often leave implicit: what enters a calculation, what comes out, what each axis means, where quantities live, which assumptions make an operation valid, and what a successful solver actually establishes.

The collection contains **15 English notebooks covering P0–P13**, including two explicitly distinguished P5 routes. English explanations have been rewritten and expanded from the supplied Korean notes rather than translated line by line. Every original code cell is represented; documented repairs update paths, comparison tolerances, interfaces, and selected numerical checks. Language-independent display equations and the original tables are retained and edited. The supplied notebooks are also preserved unchanged in a provenance archive.

## Start here

1. Read P0 to locate your problem in the ecosystem.
2. Read P1–P4 to connect program structure, arrays, and component operations.
3. Choose P5A for a short field introduction or P5B for the extended stencil and operator treatment. These overlap intentionally.
4. Use P6 as a catalogue of loop-to-array patterns.
5. Read P7–P12 according to the mathematical problem you need to solve.
6. Use P13 to inspect, verify, record, and qualify the calculation.

| Note | Subject | Notebook |
|---|---|---|
| P0 | Scientific Python Ecosystem Map | [Open](notebooks/TN_P0_Scientific_Python_Ecosystem_Map_EN.ipynb) |
| P1 | Python Computational Grammar | [Open](notebooks/TN_P1_Python_Computational_Grammar_EN.ipynb) |
| P2 | NumPy Array, Shape, Axis | [Open](notebooks/TN_P2_NumPy_Array_Shape_Axis_EN.ipynb) |
| P3 | NumPy Indexing, Slicing, Broadcasting | [Open](notebooks/TN_P3_NumPy_Indexing_Slicing_Broadcasting_EN.ipynb) |
| P4 | NumPy Vector, Matrix, Tensor Operations | [Open](notebooks/TN_P4_NumPy_Vector_Matrix_Tensor_Operations_EN.ipynb) |
| P5A | NumPy Fields and Grids: Foundations | [Open](notebooks/TN_P5A_NumPy_Fields_and_Grids_EN.ipynb) |
| P5B | NumPy Fields and Grids: FDM Discrete Operators | [Open](notebooks/TN_P5B_NumPy_Fields_and_Grids_v02_FDM_Discrete_Operators_EN.ipynb) |
| P6 | NumPy Advanced Array Operations | [Open](notebooks/TN_P6_NumPy_Advanced_Array_Operations_v02_Vectorization_Catalog_EN.ipynb) |
| P7 | SciPy Linear Algebra | [Open](notebooks/TN_P7_SciPy_Linear_Algebra_EN.ipynb) |
| P8 | SciPy Sparse Matrices and Sparse Solvers | [Open](notebooks/TN_P8_SciPy_Sparse_Matrices_and_Solvers_EN.ipynb) |
| P9 | SciPy Nonlinear Equations and Root Finding | [Open](notebooks/TN_P9_SciPy_Nonlinear_Equations_and_Root_Finding_EN.ipynb) |
| P10 | SciPy ODE and Time Integration | [Open](notebooks/TN_P10_SciPy_ODE_and_Time_Integration_EN.ipynb) |
| P11 | SciPy Optimization and Least Squares | [Open](notebooks/TN_P11_SciPy_Optimization_and_Least_Squares_EN.ipynb) |
| P12 | SciPy Interpolation, Integration, and Numerical Differentiation | [Open](notebooks/TN_P12_SciPy_Interpolation_Integration_Numerical_Differentiation_EN.ipynb) |
| P13 | Matplotlib, pandas, and Verification Workflow | [Open](notebooks/TN_P13_Matplotlib_pandas_Verification_Workflow_EN.ipynb) |

## Install and run

The recorded execution environment uses Python 3.12. The exact direct package versions are listed in `requirements.txt` and the [verification report](docs/VERIFICATION_REPORT.md). Compatibility with other versions has not been exhaustively tested.

Create an isolated environment from the collection root:

```bash
python -m venv .venv
python -m pip install --upgrade pip
```

Activate it before installing dependencies:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Then install and register the kernel:

```bash
python -m pip install -r requirements.txt
python -m ipykernel install --user --name scientific-python-notes --display-name "Scientific Python Notes"
```

Open a notebook in VS Code or another Jupyter frontend, select this environment, restart the kernel, and run all cells. Run each notebook independently. Generated files are written to an `outputs` directory beneath the current working directory; the batch runner uses the collection root.

For automated execution and HTML export:

```bash
python scripts/execute_notebooks.py
```

The default runner uses a new IPython subprocess for each notebook, captures prints and explicit rich displays, and renders Matplotlib figures with the noninteractive Agg backend. It avoids notebook-server sockets. It does not test a Jupyter frontend, interactive widgets, or a GUI backend.

For actual Jupyter-kernel execution, when the environment permits local kernel sockets:

```bash
python -m ipykernel install --user --name python3 --display-name "Python 3"
python scripts/execute_notebooks.py --engine kernel
```

Both modes rewrite executed notebooks and regenerate HTML and reports. Commit or copy any changes you want to preserve before rerunning. The examples do not fetch datasets or require a wood-specific external input file.

## Reading without executing

The `html` directory contains exported English notes with code and recorded outputs. Open [the HTML index](html/index.html) in a browser after extracting the archive. Mathematical rendering uses MathJax and may require internet access. The notebook equations also use standard `$...$` and `$$...$$` notation.

## What has been checked

All notes are executed independently in the recorded environment. Selected additions test coordinate-transform invariants, scale-aware transport comparisons, conservative flux cancellation, stencil-to-matrix equivalence, second-order spatial convergence, sparse-solver agreement, discrete versus continuum diffusion modes, heat conservation, event timing, and an independent parameter sensitivity.

Execution, algorithmic convergence, numerical verification, physical validation, and practical predictive usefulness are different outcomes. This collection establishes instructional execution and selected numerical checks. It does **not** report new experimental validation of wood diffusivity, permeability, drying, or constitutive laws. Synthetic data, moisture dependence, FSP-related transitions, and mechanism blends remain teaching examples.

Some original examples intentionally catch an invalid input or show a failed conservation diagnostic. Those are educational demonstrations, not unhandled execution errors. Synthetic curves proportional to `h**2` are now labelled as illustrations rather than measured convergence results.

## Contents and provenance

- `notebooks/`: the 15 revised English notebooks with recorded outputs.
- `html/`: readable exports and a navigation index.
- `scripts/execute_notebooks.py`: repeatable execution and export.
- `docs/EDITORIAL_NOTES.md`: the review scope and scientific qualifications.
- `docs/VERIFICATION_REPORT.md` and `docs/execution_report.json`: actual execution records.
- `docs/ZENODO_METADATA.md`: a ready-to-use description and keywords.
- `docs/PUBLISHING_GUIDE.md`: a GitHub and Zenodo release workflow.
- `requirements.txt`: tested direct dependencies.
- `CITATION.cff`: citation metadata; add the repository URL and DOI when assigned.
- `provenance/source_manifest.json`: source identities and hashes.
- `provenance/original_korean_notebooks.zip`: the 15 supplied notebooks unchanged.

## Citation and release status

This is a prepared English release package. No GitHub repository or Zenodo DOI has been assigned to this edition here. Use `CITATION.cff` for author and version information. Add the final repository URL and release DOI after publication; do not use a placeholder as a real identifier.

GitHub can host evolving notebooks and discussions; Zenodo can preserve a defined release with a persistent identifier. The publication guide explains how to use the two together or publish directly to Zenodo.

## Licensing decision

The package does not impose a new license on the author's material. Before public release, select and record a license. A practical option to consider is MIT for code and CC BY 4.0 for explanatory text and original figures, with the scope clearly distinguished. This is a proposed choice, not an authorization already granted by a license file. Add the selected license files and the corresponding metadata before publishing.

Third-party software has its own licensing terms. Linked documentation is cited rather than copied into this collection.

## AI assistance

AI assisted with English adaptation, editorial supplementation, and numerical review. Wook Kang is the author and is responsible for reviewing the content and its use. The collection preserves a working research and learning record; it makes no claim that computational success establishes predictive validity for an unfamiliar piece of wood.
