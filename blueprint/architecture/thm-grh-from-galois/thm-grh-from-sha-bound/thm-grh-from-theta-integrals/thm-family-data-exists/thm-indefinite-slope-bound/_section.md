+++
id    = "thm-indefinite-slope-bound"
kind  = "theorem"
title = "The slope bound on the indefinite side"
lean  = ["GlobalTheory.BigTop.Fun.Close.fittedFunction_at_zero_close_alt",
         "GlobalTheory.BigTop.Fun.Close.fourier_coefficient_fit_of_join_alt"]
uses  = ["thm-hecke-functional-equation-cm", "thm-non-endoscopic-hypotheses-hold",
         "thm-grh-from-theta-integrals"]
order = 113
+++
Assume:

* the published results of [thm-grh-from-theta-integrals] and the step
  identities of theta towers ([def-theta-tower-step]);
* the functional equation of Hecke $L$-functions
  ([thm-hecke-functional-equation-cm]);
* five arithmetic inputs on $L$-values: denominators of toric periods, a
  transport of lattice norms and its twisted form, denominators of zeta
  values, and the reflection $\Lambda(s)\Lambda_0(1-s) = \varepsilon\,\Lambda(1-s)\Lambda_0(s)$
  with $\varepsilon$ a unit away from a fixed set of primes, for
  $1 - e_0 \le s \le 0$;
* that theta functionals separate vectors
  ([thm-theta-functionals-separate]);
* a lower bound for the $L$-values on the definite side.

Then there is $C_{F,0}$ such that for every $C_F \ge C_{F,0}$ the families
satisfying the divisibility bound have the following property, for every
small $\varepsilon$ and large scale. At every point of the family that
carries a grid of evaluation points with constant $C_F$, the largest slope
of the hermitian lattice on the indefinite side is at most its height minus
the mean of $\log\kappa$ over the twists.

The proof fits a function to Fourier coefficients on the grid of
evaluation points.
*It is not clear* to us how the evaluation points enter.
