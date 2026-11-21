+++
kind  = "corollary"
title = "GRH for primitive characters"
provenance = "new"
lean  = ["LFunction_eq_zero_re_of_isPrimitive", "critAll", "Formalism.VW.critLine",
         "Formalism.VW.gammaFactor_ne_zero"]
uses  = ["def-zeros-on-line"]
order = 8
+++
For a primitive Dirichlet character $\chi$, every zero of $L(\chi, s)$ with
$0 < \Re s < 1$ lies on $\Re s = \tfrac12$.
