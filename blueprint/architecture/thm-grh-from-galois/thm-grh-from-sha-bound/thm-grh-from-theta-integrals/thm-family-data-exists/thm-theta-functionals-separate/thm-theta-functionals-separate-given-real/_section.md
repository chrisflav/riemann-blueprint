+++
id    = "thm-theta-functionals-separate-given-real"
kind  = "theorem"
title = "Theta functionals separate vectors, given the real input"
lean  = ["UpperTheory.Lit.real_functionals_separate_of_hypothesis"]
uses  = ["thm-siegel-weil-convergent-doubling", "thm-discrete-series-branching-coefficients",
         "thm-grh-from-theta-integrals"]
order = 2
+++
Assume the published results of [thm-grh-from-theta-integrals], unramified
Howe duality, the Siegel–Weil formula in its convergent range
([thm-siegel-weil-convergent-doubling]), and the statement on matrix
coefficients of discrete series of [thm-discrete-series-branching-coefficients]. Then the
conclusion of [thm-theta-functionals-separate] holds:
theta integrals detect every nonzero vector.
