+++
kind = "proof"
of   = "lem-siegel-weil-from-poisson"
uses = ["thm-eisenstein-continuation-growth", "thm-hasse-norm-quadratic", "thm-landherr-cm", "thm-reduction-theory-unitary"]
+++
Induction on $n$. Poisson summation for the twisted Weil representation
computes the constant terms of the theta integral, and the splitting
computes those of the Eisenstein series; they agree by induction. The
difference of the two sides is then a cusp form orthogonal to all cusp
forms, hence zero. The bound on Eisenstein series
([thm-eisenstein-continuation-growth]), reduction theory on Siegel sets
([thm-reduction-theory-unitary]) and the norm theorems of Hasse and Landherr
([thm-hasse-norm-quadratic], [thm-landherr-cm]) give convergence and the
local factors.
