+++
kind = "proof"
of   = "prop-offdiagonal-hypotheses-hold"
uses = ["lem-local-decomposition-inputs", "thm-counting-constant-mass-constant", "prop-pair-coefficient-local-decomposition", "prop-archimedean-model-data", "thm-siegel-main-theorem-hermitian", "thm-hc-finiteness-unitary"]
+++
The archimedean model data exist ([prop-archimedean-model-data]). The
spaces of automorphic forms cut out by discrete series are
finite-dimensional ([thm-hc-finiteness-unitary]), and the bound on
non-generic terms holds. Discrete series with a large gap in the
Harish-Chandra parameter have unique Bessel models. The coefficient
identities come from the local decomposition of
[prop-pair-coefficient-local-decomposition], whose inputs hold for every
datum ([lem-local-decomposition-inputs]). Uniqueness of Bessel models gives
decay of gaps and independence of the volumes at every prime; the counting
formula and the oddness of the volume give the summation identity and the
form of the mass data. The normalising constants come from the covolume
reference and the mass data of the Siegel–Weil formula
([thm-siegel-main-theorem-hermitian], [thm-counting-constant-mass-constant]),
and the mass data are positive because the local densities are. The
remaining statements are proved directly.
