+++
id    = "prop-exponent-bounds-twisting-places"
kind  = "proposition"
title = "Bounds on the exponents at the twisting places"
provenance = "new"
lean  = ["GlobalTheory.BigOn.exponent_bound_of_unitaryThetaStandardTheorems_alt",
         "GlobalTheory.T.expSt_of_base_change_and_crystalline_lattices",
         "GlobalTheory.ExpTie.Asm.expSt_of_alt", "GlobalTheory.ExpTie.Asm.hasExpBound_at",
         "GlobalTheory.T.expSt_of_num_sumExp_model"]
uses = ["def-local-parameters"]
order = 1
+++
Fix a system of local parameters ([def-local-parameters]). Then at every
point of the families at a large scale, for every $j$: $J_j(w) \ge 0$ at the
twisting places $w$, and there are numbers $J_j(l) \ge 0$, one for each
prime $l$, with
$$\sum_{l \in Q}J_j(l)\log l \le E_J \quad\text{for every finite set of primes } Q, \qquad J_j(w) \le J_j(p_w) \quad\text{for } w \in T.$$
