+++
id    = "exp-st-of-base-change-and-crystalline-lattices"
kind  = "proposition"
title = "Bounds on the exponents at the twisting places"
lean  = ["GlobalTheory.BigOn.exponent_bound_of_unitaryThetaStandardTheorems_alt", "GlobalTheory.T.expSt_of_base_change_and_crystalline_lattices"]
uses  = ["base-change-definite-unitary-group", "bhatt-scholze-crystalline-lattices", "chebotarev-degree-one", "clozel-cohomological", "cusp-u-alt", "def-local-parameters", "hecke-l-adic-character", "hecke-l-adic-character-above"]
order = 3
+++
Assume Clozel's theorem on cohomological representations
([clozel-cohomological]), the existence of $l$-adic characters attached to
algebraic Hecke characters ([hecke-l-adic-character],
[hecke-l-adic-character-above]), Chebotarev's density theorem for primes of
degree one ([chebotarev-degree-one]), Galois representations for polarized
cuspidal representations ([cusp-u-alt]), base change for definite unitary
groups ([base-change-definite-unitary-group]), the theorem of Bhatt and
Scholze on crystalline lattices ([bhatt-scholze-crystalline-lattices]) and a
system of local parameters ([def-local-parameters]).

Then at every point of the families at a large scale, for every $j$:
$J_j(w) \ge 0$ at the twisting places $w$, and there are numbers
$J_j(l) \ge 0$, one for each prime $l$, with
$$\sum_{l \in Q}J_j(l)\log l \le E_J \quad\text{for every finite set of primes } Q, \qquad J_j(w) \le J_j(p_w) \quad\text{for } w \in T.$$
