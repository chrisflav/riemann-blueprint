+++
kind  = "proposition"
title = "Congruence bound at large primes"
provenance = "new"
lean  = ["GlobalTheory.NLinkE.main_alt_alt", "GlobalTheory.T.eventually_congBound_of_facts"]
order = 3
+++
For every family there is $x_0$ such that every member at scale $x \ge x_0$
satisfying the Galois and character conditions has the following property.
Let $i$ be a local datum at a prime $l > l^*$ (an explicit threshold),
$l \ne g_0, g_1$, outside a finite exceptional set, with the weight
condition at $l$. Let $r_\pi$ be a good Galois representation attached to
$\pi$ which decomposes as
$$r_\pi \cong \rho \oplus \chi_2 \oplus \dots \oplus \chi_{t+1},$$
with $\rho$ of rank $r$ and the $\chi_c$ fixed characters. Then
$$\delta_\pi \le s_\pi(\rho) + V_l + v_l(h_E) + t\sum_{P\in Q_i} v(\zeta_P - 1),$$
where $Q_i$ is a finite set of auxiliary primes with roots of unity
$\zeta_P$.
