+++
kind = "proof"
of   = "prop-period-identity-real-package"
uses = ["thm-discrete-series-frame-independent", "thm-harish-chandra-discrete-series", "thm-hasse-norm-quadratic", "prop-family-characters-with-links", "thm-casselman-wallach", "thm-cusp-rapid-decay", "thm-hc-discrete-series-classification", "thm-discrete-series-parametrisation", "thm-doubling-method", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary", "thm-siegel-weil-convergent-doubling", "thm-strong-approximation-su", "thm-unramified-doubling-gl", "thm-weil-representation-unitary-exists", "thm-siegel-weil-weil-range"]
+++
1. Unramified Howe duality, the Siegel–Weil formula
   ([thm-siegel-weil-weil-range], [thm-siegel-weil-convergent-doubling]),
   the doubling method ([thm-doubling-method]) and unramified doubling for
   $\GL_n$ ([thm-unramified-doubling-gl]) show that the theta maps along
   each chain of localizations are surjective.
2. With this surjectivity, [prop-family-characters-with-links] gives a
   central element $z$ and, for each $u$, a family character with a bottom
   datum pinned at $z$ that has the required links.
3. The bottom datum serves the package. The classification of discrete
   series ([thm-hc-discrete-series-classification]) and the uniqueness of
   hermitian discrete series ([thm-harish-chandra-discrete-series]) then
   turn the non-vanishing of $P_u$ into the constants $a_u \ne 0$ of the
   identity.
