+++
id    = "thm-grh-from-theta-integrals"
kind  = "theorem"
title = "GRH from theta integrals"
lean  = ["UpperTheory.Lit.every_character_of_theta_integrals_local_matching",
         "GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses",
         "GlobalTheory.FunPr.ThetaLocalInputs"]
uses  = ["def-theta-tower-step", "def-sha-bound", "def-local-parameters",
         "def-nonvanishing-half-plane"]
order = 1
+++
Assume the published results on unitary groups and theta lifts listed in
[chap-literature]. Among them are Clozel's purity theorem, Green's
classification, Chebotarev's density theorem, base change for definite
unitary groups, the theorem of Bhatt and Scholze, the Siegel–Weil formula,
the doubling method, the work of Bernstein and Zelevinsky, Jacquet–Shalika
rigidity, Harish-Chandra's and Casselman–Wallach's theorems, strong
approximation, Flath's tensor product theorem, Dixmier–Malliavin
factorisation, continuation of Siegel Eisenstein series, the Rallis inner
product formula, the local–global principle for hermitian forms, Linnik's
theorem, Weyl's branching law and the theory of holomorphic discrete
series.

Assume also:

* the step identities of theta towers ([def-theta-tower-step]);
* a bound on the covolumes of the lattices in the families of
  [def-family-data];
* a system of local parameters;
* the Tate–Shafarevich bound with exponent $401$.

Then Dirichlet $L$-functions do not vanish right of the critical line.
