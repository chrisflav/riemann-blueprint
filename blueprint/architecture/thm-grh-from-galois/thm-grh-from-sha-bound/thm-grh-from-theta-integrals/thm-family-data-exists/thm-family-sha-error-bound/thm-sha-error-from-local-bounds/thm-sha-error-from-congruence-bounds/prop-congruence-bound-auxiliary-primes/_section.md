+++
id    = "prop-congruence-bound-auxiliary-primes"
kind  = "proposition"
title = "Congruence bound at the auxiliary primes"
lean  = ["GlobalTheory.ExtraFromFacts.main_alt_alt", "GlobalTheory.T.exists_const_tieChi_bound_of_facts"]
uses  = ["def-padic-hodge-package"]
order = 1
+++
Assume the $l$-adic inputs ([def-padic-hodge-package]). There are constants $C \ge 0$
and $C_T$ such that every member satisfying the Galois conditions and the
character conditions at $g_0, g_1$ has the two following properties.

* At each local datum at a twisted place with $l \ne g_0, g_1$ there is a
  Hecke-equivariant endomorphism acting by a fixed nonzero integer on the
  good eigensystems and by $0$ on the others.
* At each local datum $i$ with $l = g_k$, if $\log g_{k'} \le 2\log g_k$, if
  $g_k$ is larger than $C_T$ times a polynomial in the ranks and the twist
  sizes, and if the groups $Ш^1_l(E, e)$, $0 < e < t$, are finite, then
  $$\eta_i \le \sum_\pi \mathrm{mult}(\pi)\big(s_\pi + V_l + v_l(h_E) + R_\pi\big),$$
  the sum over good $\pi$, where $R_\pi$ is explicit: polynomial in $C$ and
  the ranks, plus valuations of a discriminant and of $\zeta - 1$ for roots
  of unity $\zeta$ attached to auxiliary primes.
