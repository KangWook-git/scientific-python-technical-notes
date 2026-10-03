# Execution and verification report

Tested with Python 3.12.14. Engine: process.

Fresh independent IPython subprocess for each notebook; code errors disallowed; stdout and rich displays captured, figures rendered with Matplotlib Agg. Real Jupyter-kernel execution is an optional separate engine. Added assertions assess selected independent identities and references. No experimental validation is claimed.

| Notebook | Result | Executed code cells | Seconds |
|---|---|---:|---:|
| TN_P0_Scientific_Python_Ecosystem_Map_EN.ipynb | passed | 9 | 2.0 |
| TN_P1_Python_Computational_Grammar_EN.ipynb | passed | 30 | 0.73 |
| TN_P2_NumPy_Array_Shape_Axis_EN.ipynb | passed | 34 | 0.92 |
| TN_P3_NumPy_Indexing_Slicing_Broadcasting_EN.ipynb | passed | 49 | 0.9 |
| TN_P4_NumPy_Vector_Matrix_Tensor_Operations_EN.ipynb | passed | 68 | 0.99 |
| TN_P5A_NumPy_Fields_and_Grids_EN.ipynb | passed | 14 | 0.82 |
| TN_P5B_NumPy_Fields_and_Grids_v02_FDM_Discrete_Operators_EN.ipynb | passed | 29 | 1.19 |
| TN_P6_NumPy_Advanced_Array_Operations_v02_Vectorization_Catalog_EN.ipynb | passed | 77 | 1.43 |
| TN_P7_SciPy_Linear_Algebra_EN.ipynb | passed | 14 | 0.76 |
| TN_P8_SciPy_Sparse_Matrices_and_Solvers_EN.ipynb | passed | 25 | 1.62 |
| TN_P9_SciPy_Nonlinear_Equations_and_Root_Finding_EN.ipynb | passed | 19 | 0.9 |
| TN_P10_SciPy_ODE_and_Time_Integration_EN.ipynb | passed | 23 | 1.26 |
| TN_P11_SciPy_Optimization_and_Least_Squares_EN.ipynb | passed | 26 | 1.08 |
| TN_P12_SciPy_Interpolation_Integration_Numerical_Differentiation_EN.ipynb | passed | 22 | 1.71 |
| TN_P13_Matplotlib_pandas_Verification_Workflow_EN.ipynb | passed | 35 | 2.66 |

## Tested package versions

- numpy: 2.3.5
- scipy: 1.17.0
- pandas: 2.2.3
- matplotlib: 3.10.8
- sympy: 1.14.0
- nbformat: 5.11.1
- nbclient: 0.11.0
- nbconvert: 7.17.1
- ipykernel: 7.4.0
- ipython: 9.17.1

Execution establishes that these examples run in the recorded environment. Added checks cover selected basis invariants, flux balance, refinement order, operator equivalence, time integration, and sensitivities. This is not an all-platform compatibility test or experimental validation of the illustrative wood laws. Caught invalid-input examples and deliberately failed conservation diagnostics remain pedagogical output. Timing and iteration counts can vary. The process engine is sufficient for this Python-only series but does not test GUI backends, notebook-server networking, widgets, or Jupyter frontend rendering.
