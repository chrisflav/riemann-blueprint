+++
kind = "proof"
of   = "thm-family-conditions-from-basic"
uses = ["thm-abelian-variety-torsion-count", "thm-cusp-decay-sobolev", "thm-discrete-series-frame-independent",
        "thm-harish-chandra-discrete-series", "prop-chosen-data-serve-families", "thm-hasse-norm-quadratic", "thm-landherr-cm",
        "prop-small-terms-offdiag-level", "thm-unitary-integral-models",
        "prop-periods-valuations-good-data",
        "prop-counting-constants-constituents", "thm-semistable-reduction"]
+++
We check the 26 conditions one group at a time.

1. The twelve basic conditions are hypotheses, and $\mathcal N$ is a hypothesis.
2. The values, periods and valuations come from
   [prop-periods-valuations-good-data].
3. The bound on small terms, the off-diagonal bound and the lower bound on
   levels come from [prop-small-terms-offdiag-level], which uses the Siegel–Weil formula.
4. Global Artin reciprocity gives the reciprocity condition by
   [prop-chosen-data-serve-families]. The labels give the counting constants by
   [prop-counting-constants-constituents].
5. The volume ratio that the Siegel–Weil formula gives yields the rank
   condition. The class-number bound and the divisibility of complements
   hold at every constructed point. Primitivity gives the $j$-invariant and
   zero-locus conditions, and the compatibility condition gives the twist condition.
6. The definite-side condition combines nine of the hypotheses with the
   surjectivity statement, the lower bound on weights and the published
   results on discrete series and cusp forms.
