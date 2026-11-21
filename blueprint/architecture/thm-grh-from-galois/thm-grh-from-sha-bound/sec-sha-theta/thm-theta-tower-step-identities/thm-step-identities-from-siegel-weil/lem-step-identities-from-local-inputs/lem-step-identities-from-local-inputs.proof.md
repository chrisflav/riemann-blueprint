+++
kind = "proof"
of   = "lem-step-identities-from-local-inputs"
uses = ["thm-hasse-norm-quadratic", "thm-hecke-l-entire", "prop-theta-integrals-along-towers", "thm-eisenstein-continuation-growth", "thm-reduction-theory-unitary", "thm-siegel-weil-definite", "thm-weil-representation-unitary-exists"]
+++
The statements of [prop-theta-integrals-along-towers] give matching of
local data for triples, and the constant-term computations of theta
integrals. The Siegel–Weil formula ([thm-siegel-weil-definite]) and the
Rallis inner product formula then give the step constants
$C \cdot L^S(\nu, \tfrac{a - (b+2)}{2} + 1)$, with convergence from the bound
on Siegel Eisenstein series ([thm-eisenstein-continuation-growth]) and
reduction theory on Siegel sets ([thm-reduction-theory-unitary]); the Weil
representation exists by [thm-weil-representation-unitary-exists]. Hecke
$L$-functions do not vanish at $s = 1$ ([thm-hecke-l-entire]), which makes the
constants non-zero; Hasse's norm theorem ([thm-hasse-norm-quadratic]) is used
at inert places.
