+++
kind = "proof"
of   = "thm-offdiagonal-bound"
uses = ["prop-archimedean-model-data", "prop-offdiagonal-hypotheses-hold", "lem-offdiagonal-bound-from-hypotheses", "thm-siegel-main-theorem-hermitian", "thm-hc-finiteness-unitary"]
+++
By [prop-offdiagonal-hypotheses-hold], all hypotheses of the general bound
hold; that proposition uses the archimedean model data
([prop-archimedean-model-data]), the bound on non-generic terms, the
finite-dimensionality of spaces of automorphic forms
([thm-hc-finiteness-unitary]), uniqueness of Bessel models with a large gap
and the mass data that the Siegel–Weil formula
([thm-siegel-main-theorem-hermitian]) gives. So the bound holds for every
datum ([lem-offdiagonal-bound-from-hypotheses]). It remains to check that
the chosen data of the class meet the size and threshold hypotheses; the
rank conditions and the small-terms bound give this.
