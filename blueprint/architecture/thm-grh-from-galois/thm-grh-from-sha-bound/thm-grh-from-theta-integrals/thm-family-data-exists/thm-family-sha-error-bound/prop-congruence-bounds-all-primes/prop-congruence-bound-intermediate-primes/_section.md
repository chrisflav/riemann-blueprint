+++
id    = "prop-congruence-bound-intermediate-primes"
kind  = "proposition"
title = "Congruence bound at intermediate primes"
provenance = "new"
lean  = ["GlobalTheory.NLink.InertStep.main_alt_alt", "GlobalTheory.NLink.rowsAD_in_setting_alt", "GlobalTheory.T.adm_at_inert_of_range", "GlobalTheory.T.star_ad_and_bb_le_of_joint_cond"]
order = 2
+++
Let a member satisfy the setup of the family at scale $x$, the corollary of
[thm-wach-lifting-theorem] with a constant $C_2 \ge 1$, and, at the inert
primes, the local bound or congruence conditions on its Galois
representations. Then at every local datum $i$ at a twisted place with
$l \ne g_0, g_1$ in the intermediate range, and every good $\pi$,
$$\delta_\pi \le s_\pi + \sum_{\lambda\mid l}\ell_{i,\lambda}(\pi) + V_l + v_l(h_E) + B_i(\pi) + l^{-2},$$
with
$$B_i(\pi) \le 7200\, f\, n\, t^2\, n_V\, \Lambda^2,$$
where $n$, $t$, $n_V$ are ranks of the member.
