+++
id    = "prop-exponent-bounds-twisting-places"
kind  = "proposition"
title = "Bounds on the exponents at the twisting places"
lean  = ["GlobalTheory.BigOn.exponent_bound_of_unitaryThetaStandardTheorems_alt", "GlobalTheory.T.expSt_of_base_change_and_crystalline_lattices"]
uses  = ["thm-labesse-base-change", "thm-bhatt-scholze-coefficients", "thm-chebotarev-degree-one", "thm-clozel-cohomological", "thm-galois-reps-polarized-cuspidal", "def-local-parameters", "thm-hecke-l-adic-character", "thm-hecke-l-adic-character-above-l"]
order = 3
+++
Assume Clozel's theorem on cohomological representations
([thm-clozel-cohomological]), the existence of $l$-adic characters attached to
algebraic Hecke characters ([thm-hecke-l-adic-character],
[thm-hecke-l-adic-character-above-l]), Chebotarev's density theorem for primes of
degree one ([thm-chebotarev-degree-one]), Galois representations for polarized
cuspidal representations ([thm-galois-reps-polarized-cuspidal]), base change for definite unitary
groups ([thm-labesse-base-change]), the theorem of Bhatt and
Scholze on crystalline lattices ([thm-bhatt-scholze-coefficients]) and a
system of local parameters ([def-local-parameters]).

Then at every point of the families at a large scale, for every $j$:
$J_j(w) \ge 0$ at the twisting places $w$, and there are numbers
$J_j(l) \ge 0$, one for each prime $l$, with
$$\sum_{l \in Q}J_j(l)\log l \le E_J \quad\text{for every finite set of primes } Q, \qquad J_j(w) \le J_j(p_w) \quad\text{for } w \in T.$$
