+++
id    = "thm-grh-from-theta-integrals"
kind  = "theorem"
title = "GRH from families of unitary groups"
lean  = ["UpperTheory.Lit.every_character_of_theta_integrals_local_matching",
         "GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses",
         "GlobalTheory.FunPr.ThetaLocalInputs"]
uses  = ["def-sha-bound", "def-nonvanishing-half-plane"]
order = 1
+++
Suppose that conjugate self-dual and polarized cuspidal representations of
$\GL_a$ over CM fields have Galois representations as in
[thm-galois-reps-csd-above-l] and [thm-galois-reps-polarized-cuspidal], and
that the Tate–Shafarevich bound ([def-sha-bound]) holds with exponent
$401$. Then Dirichlet $L$-functions do not vanish right of the critical
line.
