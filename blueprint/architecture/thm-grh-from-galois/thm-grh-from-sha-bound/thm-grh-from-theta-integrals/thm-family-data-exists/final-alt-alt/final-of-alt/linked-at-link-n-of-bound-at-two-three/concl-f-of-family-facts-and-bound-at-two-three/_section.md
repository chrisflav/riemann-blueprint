+++
id    = "concl-f-of-family-facts-and-bound-at-two-three"
kind  = "proposition"
title = "Congruence bounds at all primes"
lean  = ["GlobalTheory.NLinkClose.main_alt_alt", "GlobalTheory.T.conclF_of_family_facts_and_bound_at_two_three"]
uses  = ["hypotheses2"]
order = 2
+++
Assume the $l$-adic inputs ([hypotheses2]). Let $\mathcal F$ be a family with
good twists, satisfying the bound at $g_0, g_1$ of
[exists-const-tie-chi-bound-of-facts] for some $C, C_T$ and the bound at $2$
and $3$. Then there is $C'$ such that for all large $x$, every member whose
groups $Ш^1_p(E, e)$, $0 < e < t$, are finite carries Galois representations
$\rho_\pi$ at all its local data with:

* small Selmer groups: $s_\pi \le \nu_l + l^{-2}$ at every twisted local
  datum, where $\nu_l$ is an explicit cyclotomic invariant;
* multiplicities of the good eigensystems at most the ranks of the lattices;
* congruence bounds
  $$\delta_\pi \le s_\pi + \textstyle\sum_{\lambda\mid l}\ell_{i,\lambda} + V_l + v_l(h_E) + B_i + l^{-2}$$
  in every range of primes $l$: large $l$, an intermediate range, the
  primes $q, d$ of the auxiliary pair, the small primes, and $3$ and $2$.
  The local lengths $\ell_{i,\lambda}$ and the errors $B_i$ are bounded by
  $C'$ times explicit polynomials in the size parameters;
* a bound on the number of exceptional primes, and a polynomial bound on
  the parameters.
