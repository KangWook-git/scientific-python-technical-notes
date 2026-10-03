# Editorial and numerical review

## Scope of the English edition

The edition reconstructs the explanations in English around the original numbered topics. It is an adapted and expanded edition, not a word-for-word translation. Mathematical displays without Korean text and all actual Markdown tables are carried forward; Korean rhetorical text boxes are replaced by English prose. All original code examples remain represented in their original order, with documented repairs. The original Korean notebooks are preserved unchanged separately.

P5A and P5B identify the short and expanded field notes. They are two reading routes, not a claim that their originally uploaded names represent distinct independent research products. P5B is recommended when spatial operators are the immediate goal. P6 retains all 45 numbered vectorization examples.

## Changes affecting execution or interpretation

| Area | Revision | Reason |
|---|---|---|
| Output paths | Replace P13 `/mnt/data` paths with a created relative `outputs` directory | Permit execution outside the original hosted workspace |
| Comparisons | Add a scale-aware comparison helper and use it in original equivalence demonstrations | The default absolute tolerance can hide errors at coefficients of order 1e-10 |
| P6 stacking | Replace deprecated `np.row_stack` with `np.vstack` | Keep the intended vertical stacking operation |
| P12 interpolation | Use `np.interp` for simple in-domain linear interpolation and a degree-one `make_interp_spline` for explicit extrapolation | Distinguish interpolation, endpoint extension, and extrapolation |
| P12 smoothing | Replace `UnivariateSpline` with `make_splrep` | Use the maintained interface while preserving the illustrative smoothing choices |
| P9 damped Newton | Check finite values and zero derivatives; reject an unsuccessful line search; assess the final residual | Avoid accepting a step merely because the minimum step was reached |
| P10 diffusion | Supply the constant matrix Jacobian and compare with an exact discrete sine mode | Separate time error from fixed-grid spatial error |
| Flux table | Restore the minus sign in the tensor-field flux implementation | Match the stated constitutive law |
| Convergence figures | Label synthetic h-squared curves as illustrative | Avoid treating a constructed reference curve as measured solver convergence |
| Mathematical notation | Remove negative-spacing `\!` commands and use dollar-delimited mathematics | Avoid the spacing problem seen in earlier Typst conversion; this package is checked as notebooks and HTML, not a newly rendered Typst PDF |

## Scientific qualifications

An array's number of axes is not tensor order. Component transformation, units, sampling locations, and physical meaning must be specified separately. `Q` contains local orthonormal basis vectors in global components where local-to-global transformations are discussed. Active rotations and passive component changes must not be conflated.

Flux examples of the form `q=-D grad u` are generic constitutive illustrations. If `u` is a dimensionless moisture ratio and `D` has units of m2/s, this `q` has units of m/s. It is not automatically a mass flux in kg/(m2 s). Under a fixed dry-density formulation, mass flux requires the corresponding dry-density factor and a correctly defined moisture variable. Mass-conservative wood models also require declared reference volumes and state definitions.

A harmonic mean at an interface represents scalar resistance in series for two equal half-distances and positive conductivities. Unequal distances require weighted resistances. A full rotated anisotropic tensor on an irregular grid is not generally handled by independently harmonically averaging tensor entries. Shared face values must represent a physically justified numerical flux.

Repeated use of `np.gradient` is useful for inspection but need not reproduce a standard compact Laplacian or a conservative boundary-value discretization. Centred interior stencils leave boundary treatment unresolved. `np.roll` creates periodic adjacency and must not silently be used for a nonperiodic boundary.

For explicit Euler diffusion on a uniform grid with constant nonnegative diagonal diffusivity, a standard stability condition is `dt * sum(Di/hi**2) <= 1/2`. This condition does not apply unchanged to every tensor, nonlinear coefficient, nonuniform grid, or boundary discretization. Implicit time stepping also requires an accurate accepted solve.

CG needs a Hermitian positive-definite operator and a compatible positive-definite preconditioner. A pure Neumann Poisson operator can have a nullspace, and the raw Laplacian often has the opposite sign to the positive Poisson operator. A generic ILU is not automatically appropriate for CG. Constant-diagonal Jacobi scaling does not necessarily improve condition number.

A scalar sign-changing bracket supports a root-existence argument only with continuity. It does not show uniqueness and misses many even-multiplicity roots. A failure to find a bracket is not evidence of nonexistence. The damped Newton example remains a teaching implementation, not a general production solver with all safeguards.

The `solve_ivp` tolerance scale concerns local error estimates. It does not certify global error, spatial accuracy, conservation, or physical predictive validity. `t_eval` specifies stored outputs rather than internal steps. Events may be missed when several crossings occur within one internal step. The exact discrete diffusion mode is distinct from the continuum mode.

Least-squares cost equals half the raw sum of squared residuals only for linear loss. Jacobian rank and covariance are local, scaling-sensitive diagnostics. Independent-observation standard-deviation weights differ from correlated-noise whitening. Illustrative weights in the exponential example are not the generating noise model. Robust loss and positivity bounds do not create missing information. Physical logarithms should use dimensionless ratios to a declared reference scale.

Interpolation smoothness is not physical validation. Smoothing choices and extrapolation add assumptions. Differentiation can amplify measurement noise. Quadrature error estimates do not automatically include measurement uncertainty or missing resolution.

## Evidence and remaining work

The execution report identifies the actual environment and engine. A fresh independent IPython process is used for each note in the recorded run, and plots are captured with Agg. Real notebook-kernel execution is also provided as an optional mode but is not claimed for the recorded process-engine run.

Selected added assertions test independent mathematical identities and reference solutions. They do not exhaustively test every illustrative algorithm or every operating system. Numerical output, timing, and solver iterations can change across environments. The notes are suitable for review and a documented educational release; further domain validation needs appropriate measurements and independent prediction tests.

Before public publication, the author should settle the license and publication target. Neither a repository URL nor a DOI is fabricated in this prepared package.

## Primary documentation used in the review

- [NumPy allclose: tolerance definition](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html)
- [NumPy solve: batched right-hand-side shapes](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)
- [SciPy CG: operator and preconditioner requirements](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.cg.html)
- [SciPy solve_ivp: tolerances, outputs, events, Jacobians](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)
- [SciPy least_squares: residuals and losses](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html)
- [SciPy make_splrep](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.make_splrep.html)
- [SciPy UnivariateSpline: legacy status](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html)
