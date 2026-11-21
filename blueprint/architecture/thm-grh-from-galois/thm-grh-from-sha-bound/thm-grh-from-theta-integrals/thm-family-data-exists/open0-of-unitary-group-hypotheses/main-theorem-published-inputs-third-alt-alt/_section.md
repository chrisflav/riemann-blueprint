+++
id    = "main-theorem-published-inputs-third-alt-alt"
kind  = "proposition"
title = "The isometric period identity and the multiplicity condition"
lean  = ["GlobalTheory.T.main_theorem_published_inputs_third_alt_alt", "GlobalTheory.miStarRow_alt_alt"]
uses  = ["casselman-wallach", "cusp-rapid-decay", "def-local-parameters", "discrete-series-classification",
         "discrete-series-cover", "doubling-method-local-zeta-integrals", "harish-chandra-finite",
         "harish-chandra-modules", "published-siegel-weil-unitary-convergent", "siegel-weil-unitary-convergent",
         "strong-approx-su", "unramified-doubling-gl", "weil-representation-unitary-pair", "weil-unitary"]
order = 1
+++
Assume Harish-Chandra's finiteness theorem, the rapid decay of cusp forms,
the theory of discrete series, the Casselman–Wallach theorem, unramified
Howe duality, the Weil representation of unitary dual pairs, the
Siegel–Weil formula, the doubling method, unramified doubling for $\GL_n$
and strong approximation for special unitary groups. Then for any
construction data built from a system of local parameters
([def-local-parameters]), at every admissible datum of the families the
following *isometric period identity* holds. There are an isometry $V$ of
the space of theta functions, unitary matrices $U_u$, non-zero constants
$a_u$ and non-zero constants $\zeta_u(t)$ with $\zeta_u(\mu_0) = 1$ such that
$$\zeta_u(t)\,\mathrm{ev}\big(P_{u,t}(\varphi, F)\big) = a_u\,\big\langle V\,\Theta_t(F),\ P_u(U_u\varphi)\big\rangle$$
for all $u$, $t$, $\varphi$ and $F$. In words: evaluating the period
$P_{u,t}$ is, up to an isometry and non-zero constants, an inner product of
a theta lift with a projection. In particular the multiplicity condition
holds at these data.

Unramified Howe duality here is the statement that in the Weil
representation of an unramified local dual pair, the vectors fixed by the
maximal compact subgroup of one group lie in the span of the orbit of the
vacuum vector under the other group.
