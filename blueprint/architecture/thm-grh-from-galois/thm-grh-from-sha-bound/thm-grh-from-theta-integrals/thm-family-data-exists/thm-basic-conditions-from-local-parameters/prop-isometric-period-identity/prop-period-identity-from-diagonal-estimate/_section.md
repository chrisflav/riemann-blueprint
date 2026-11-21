+++
id    = "prop-period-identity-from-diagonal-estimate"
kind  = "proposition"
title = "The period identity from a diagonal estimate"
lean  = ["GlobalTheory.T.main_theorem_published_inputs_variant_alt_alt", "GlobalTheory.miStarRowClosing_alt_alt"]
uses  = ["thm-casselman-wallach", "thm-cusp-rapid-decay", "def-local-parameters", "thm-hc-discrete-series-classification",
         "thm-discrete-series-parametrisation", "thm-doubling-method", "thm-hc-finiteness-unitary",
         "thm-hc-modules-unitary", "thm-siegel-weil-convergent-doubling", "thm-strong-approximation-su",
         "thm-unramified-doubling-gl", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range"]
order = 1
+++
Assume the published results of [prop-isometric-period-identity].
Assume also a *diagonal estimate*: at every scale with bounded constant
$C_\Gamma$, a two-term bound
$$4\big(e^{C m_L} + 1\big), \qquad 4e^{-k/2} + 2e^{-k}$$
on the diagonal terms, and the rank identity
$d_0 = d^*\,(T^{k} - 1)^{f}$ for each member. Let $p$ be construction data
built from a system of local parameters, such that every good point carries
real data. Then the isometric period identity holds at every good
admissible datum of the families built from $p$.
