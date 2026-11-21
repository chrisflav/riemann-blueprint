+++
id    = "prop-period-identity-real-package"
kind  = "proposition"
title = "The period identity for a real package"
lean  = ["GlobalTheory.Fam.miAt_of_truePack_alt_alt", "GlobalTheory.Fam.miStar2_of_allTrue_alt_alt",
         "GlobalTheory.T.main_theorem_from_published_results_alt_alt_alt_alt",
         "GlobalTheory.T.main_theorem_from_published_results_alt_alt_alt_alt_alt"]
uses  = ["thm-casselman-wallach", "thm-cusp-rapid-decay", "thm-hc-discrete-series-classification", "thm-discrete-series-parametrisation",
         "thm-doubling-method", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary",
         "thm-siegel-weil-convergent-doubling", "thm-strong-approximation-su", "thm-unramified-doubling-gl",
         "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range"]
order = 1
+++
Assume the published results of [prop-isometric-period-identity].
Let $W$ be a real package attached to a member of a family: theta
functions on a definite unitary group together with their real
realisation. Suppose that $W$ satisfies all family conditions, that
$r_S \ge 1$, and that for each $u$ the projection $P_u$ is non-zero on some
vector of the ramified space. Then the isometric period identity holds
for $W$.
