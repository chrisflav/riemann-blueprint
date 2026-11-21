+++
kind = "proof"
of   = "thm-reciprocity-fixed-exponent"
uses = ["thm-siegel-units-diamond"]
+++
Write the zeta class as a sum over diamond operators $\langle\delta\rangle$
of twisted Kummer classes of Siegel units. [thm-siegel-units-diamond] computes the
$q$-expansion of each term modulo $l^n$, up to a Galois coboundary. Apply
$\lambda$, which kills the coboundaries because it is Hecke-equivariant and
integral, and sum over $\delta$ with the weights $\chi(\delta)^{-1}$.
