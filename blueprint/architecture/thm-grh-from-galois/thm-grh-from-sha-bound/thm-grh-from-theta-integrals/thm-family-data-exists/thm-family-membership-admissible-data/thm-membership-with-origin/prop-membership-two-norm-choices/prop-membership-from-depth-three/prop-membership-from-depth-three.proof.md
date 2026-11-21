+++
kind = "proof"
of   = "prop-membership-from-depth-three"
uses = ["lem-membership-two-passes", "lem-depth-three-to-four", "thm-hasse-norm-quadratic", "thm-casselman-wallach", "thm-gross-cm-curves", "thm-cusp-rapid-decay", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary", "thm-siegel-main-theorem-hermitian", "thm-weil-representation-auxiliary-pairs", "thm-weber-ray-class-field", "thm-hc-discrete-series-classification", "thm-discrete-series-parametrisation", "thm-formal-degree-upq"]
+++
Extend depth three to depth four for $p$ and for $p_g$ by
[lem-depth-three-to-four]. Ambient and division data exist for both. Theta
data with all compatibilities exist by the theory of discrete series
([thm-hc-discrete-series-classification],
[thm-discrete-series-parametrisation], [thm-hc-modules-unitary],
[thm-casselman-wallach]) and the Weil representation
[thm-weil-representation-auxiliary-pairs]. Points built for $p_g$ are good
for $p$. Apply [lem-membership-two-passes].
