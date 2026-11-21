+++
id    = "prop-period-identity-from-point-conditions"
kind  = "proposition"
title = "The period identity from conditions at points"
lean  = ["GlobalTheory.Fam.miStar_row_alt_alt", "GlobalTheory.T.main_theorem_published_results_final_alt_alt"]
uses  = ["thm-casselman-wallach", "thm-cusp-rapid-decay", "def-local-parameters", "thm-hc-discrete-series-classification",
         "thm-discrete-series-parametrisation", "thm-doubling-method", "thm-hc-finiteness-unitary",
         "thm-hc-modules-unitary", "thm-siegel-weil-convergent-doubling", "thm-strong-approximation-su",
         "thm-unramified-doubling-gl", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range"]
order = 1
+++
Assume the hypotheses of [prop-period-identity-from-diagonal-estimate].
Suppose moreover that at every good admissible datum the following hold:
the real realisation joins with the spectral data, the decomposition point
condition holds, frames exist and the realisation extends, the primitivity
and separation of types hold, the spectral data are finite, the spectral
gap is at least $100r^4$ and the node gap holds, and $r_S \ge 1$. Then the
isometric period identity holds at every good admissible datum.
