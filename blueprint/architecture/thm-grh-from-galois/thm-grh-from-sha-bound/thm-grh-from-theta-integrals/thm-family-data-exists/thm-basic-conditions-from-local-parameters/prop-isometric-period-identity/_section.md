+++
id    = "prop-isometric-period-identity"
kind  = "proposition"
title = "The isometric period identity and the multiplicity condition"
lean  = ["GlobalTheory.T.main_theorem_published_inputs_third_alt_alt", "GlobalTheory.miStarRow_alt_alt"]
uses  = ["thm-casselman-wallach", "thm-cusp-rapid-decay", "def-local-parameters", "thm-hc-discrete-series-classification",
         "thm-discrete-series-parametrisation", "thm-doubling-method", "thm-hc-finiteness-unitary",
         "thm-hc-modules-unitary", "thm-siegel-weil-convergent-doubling", "thm-siegel-main-theorem-hermitian",
         "thm-strong-approximation-su", "thm-unramified-doubling-gl", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range"]
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
