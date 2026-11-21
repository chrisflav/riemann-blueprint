+++
kind = "proof"
of   = "prop-admissible-data-exist"
uses = ["thm-hasse-norm-quadratic", "thm-casselman-wallach", "thm-cusp-rapid-decay", "thm-discrete-series-parametrisation", "thm-discrete-series-exist", "thm-artin-reciprocity", "thm-green-parametrisation", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary", "thm-weber-ray-class-field", "thm-weil-representation-auxiliary-pairs"]
+++
The choice of norms gives a uniform bound for the zeta factors. Witnesses
pass along the division of sets, and the local parameters reduce the
compatibility with $p$ to the multiplicity condition; this step uses Green's
classification [thm-green-parametrisation], the theory of discrete series
([thm-discrete-series-exist], [thm-discrete-series-parametrisation],
[thm-hc-modules-unitary]) and the Weil representation
[thm-weil-representation-auxiliary-pairs]. A recursion on the sizes $\eta$,
using Artin reciprocity [thm-artin-reciprocity] and Weber's ray class fields
[thm-weber-ray-class-field], then builds the admissible data.
