+++
id    = "thm-indefinite-slope-bound"
kind  = "theorem"
title = "The slope bound on the indefinite side"
lean  = ["GlobalTheory.BigTop.Fun.Close.fittedFunction_at_zero_close_alt",
         "GlobalTheory.BigTop.Fun.Close.fourier_coefficient_fit_of_join_alt"]
uses  = ["def-family-data"]
order = 113
+++
There is $C_{F,0}$ such that for every $C_F \ge C_{F,0}$ the families of
[def-family-data] satisfying the divisibility bound have the following
property, for every small $\varepsilon$ and large scale. At every point of
the family that carries a grid of evaluation points with constant $C_F$,
the largest slope of the hermitian lattice on the indefinite side is at most
its height minus the mean of $\log\kappa$ over the twists.

The proof fits a function to Fourier coefficients on the grid of
evaluation points.
*It is not clear* to us how the evaluation points enter.
