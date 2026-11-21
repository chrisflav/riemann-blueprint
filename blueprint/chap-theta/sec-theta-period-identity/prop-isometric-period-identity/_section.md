+++
id    = "prop-isometric-period-identity"
kind  = "proposition"
title = "The isometric period identity and the multiplicity condition"
provenance = "new"
lean  = ["GlobalTheory.T.main_theorem_published_inputs_third_alt_alt",
         "GlobalTheory.miStarRow_alt_alt",
         "GlobalTheory.T.main_theorem_published_inputs_variant_alt_alt",
         "GlobalTheory.miStarRowClosing_alt_alt", "GlobalTheory.Fam.miStar_row_alt_alt",
         "GlobalTheory.T.main_theorem_published_results_final_alt_alt"]
uses = ["def-local-parameters"]
order = 1
+++
For any construction data built from a system of local parameters
([def-local-parameters]), at every admissible datum of the families the
following *isometric period identity* holds. There are an isometry $V$ of
the space of theta functions, unitary matrices $U_u$, non-zero constants
$a_u$ and non-zero constants $\zeta_u(t)$ with $\zeta_u(\mu_0) = 1$ such that
$$\zeta_u(t)\,\mathrm{ev}\big(P_{u,t}(\varphi, F)\big) = a_u\,\big\langle V\,\Theta_t(F),\ P_u(U_u\varphi)\big\rangle$$
for all $u$, $t$, $\varphi$ and $F$. In words: evaluating the period
$P_{u,t}$ is, up to an isometry and non-zero constants, an inner product of
a theta lift with a projection. In particular the multiplicity condition
holds at these data.
