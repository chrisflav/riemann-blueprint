+++
kind = "proof"
of   = "thm-family-conditions-from-basic"
uses = ["thm-abelian-variety-torsion-count", "thm-cusp-decay-sobolev", "thm-discrete-series-frame-independent", "thm-harish-chandra-discrete-series", "prop-chosen-data-serve-families", "thm-hasse-norm-quadratic", "thm-landherr-cm", "prop-small-terms-offdiag-level", "thm-unitary-integral-models", "prop-periods-valuations-good-data", "prop-counting-constants-constituents", "thm-semistable-reduction", "thm-casselman-wallach", "thm-cusp-rapid-decay", "thm-hc-discrete-series-classification", "thm-discrete-series-parametrisation", "thm-artin-reciprocity", "thm-hc-modules-unitary", "thm-siegel-main-theorem-hermitian", "thm-twisting-index-and-archimedean-bounds"]
+++
We check the 26 conditions one group at a time.

1. The twelve basic conditions and $\mathcal N$ hold by hypothesis.
2. The values, periods and valuations come from
   [prop-periods-valuations-good-data].
3. The bound on small terms, the off-diagonal bound and the lower bound on
   levels come from [prop-small-terms-offdiag-level].
4. By global Artin reciprocity [thm-artin-reciprocity], the chosen data
   satisfy the reciprocity condition ([prop-chosen-data-serve-families]).
   The labels give the counting constants by
   [prop-counting-constants-constituents].
5. The volume ratio that the Siegel–Weil formula
   [thm-siegel-main-theorem-hermitian] gives yields the rank condition. The
   class-number bound and the divisibility of complements hold at every
   constructed point. Primitivity gives the $j$-invariant and zero-locus
   conditions, and the compatibility condition gives the twist condition.
6. The definite-side condition combines nine of the hypotheses with the
   surjectivity statement and the lower bound on weights of
   [thm-twisting-index-and-archimedean-bounds], the theory of discrete
   series ([thm-hc-discrete-series-classification],
   [thm-casselman-wallach]) and the rapid decay of cusp forms
   ([thm-cusp-rapid-decay]).
