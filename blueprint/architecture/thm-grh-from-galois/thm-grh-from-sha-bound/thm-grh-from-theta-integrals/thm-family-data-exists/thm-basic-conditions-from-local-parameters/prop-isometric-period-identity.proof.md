+++
kind = "proof"
of   = "prop-isometric-period-identity"
uses = ["thm-discrete-series-bessel-pointwise-bound", "thm-hasse-norm-quadratic", "thm-landherr-cm", "prop-period-identity-from-diagonal-estimate", "thm-counting-constant-mass-constant", "thm-lattice-term-pair-bound", "thm-weighted-bessel-sum-bound", "thm-casselman-wallach", "thm-cusp-rapid-decay", "thm-hc-discrete-series-classification", "thm-discrete-series-parametrisation", "thm-doubling-method", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary", "thm-siegel-weil-convergent-doubling", "thm-siegel-main-theorem-hermitian", "thm-strong-approximation-su", "thm-unramified-doubling-gl", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range"]
+++
The Siegel–Weil formula ([thm-siegel-weil-weil-range]) gives the diagonal
estimate that [prop-period-identity-from-diagonal-estimate] asks for. Its
proof uses the pointwise bound for coefficients of discrete series
([thm-discrete-series-bessel-pointwise-bound]), the uniform weighted bound at
rotated points ([thm-weighted-bessel-sum-bound]), the Hasse norm theorem
([thm-hasse-norm-quadratic]) and Landherr's classification of hermitian
forms ([thm-landherr-cm]). That proposition then gives the identity at
every admissible datum. The multiplicity condition asks for the identity
only eventually in the scale, so it follows.

Along the way the argument uses unramified Howe duality, in this form: in
the Weil representation of an unramified local dual pair
([thm-weil-representation-auxiliary-pairs]), the vectors fixed by the
maximal compact subgroup of one group lie in the span of the orbit of the
vacuum vector under the other group.
