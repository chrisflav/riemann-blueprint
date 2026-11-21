+++
kind = "proof"
of   = "all-rows-of-open0-alt"
uses = ["ab-mul-n-st", "cusp-decay-sobolev", "discrete-series-hermitian-unique",
        "ds-exhaust", "h-serv-of-link-r", "hasse-norm-st", "landherr-st",
        "lg1-s-lp-s-o-h-tf", "part-i-of-semistable-reduction",
        "period-entries-tie-and-level-valuations-at-built",
        "row-counts-of-labels-alt", "semistable-reduction-st"]
+++
We check the 26 conditions one group at a time.

1. The twelve basic conditions are hypotheses, and $\mathcal N$ is a hypothesis.
2. The values, periods and valuations come from
   [period-entries-tie-and-level-valuations-at-built].
3. The bound on small terms, the off-diagonal bound and the lower bound on
   levels come from [lg1-s-lp-s-o-h-tf], which uses the Siegel–Weil formula.
4. Global Artin reciprocity gives the reciprocity condition by
   [h-serv-of-link-r]. The labels give the counting constants by
   [row-counts-of-labels-alt].
5. The volume ratio that the Siegel–Weil formula gives yields the rank
   condition. The class-number bound and the divisibility of complements
   hold at every constructed point. Primitivity gives the $j$-invariant and
   zero-locus conditions, and the compatibility condition gives the twist condition.
6. The definite-side condition combines nine of the hypotheses with the
   surjectivity statement, the lower bound on weights and the published
   results on discrete series and cusp forms.
