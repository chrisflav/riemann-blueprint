+++
kind = "proof"
of   = "thm-square-term-estimates"
uses = ["thm-bz-finiteness", "thm-cusp-rapid-decay",
        "thm-doubling-method", "thm-geometric-lemma-filtration", "thm-hasse-norm-quadratic",
        "thm-siegel-weil-convergent-doubling", "thm-oscillator-lie-action",
        "thm-witt-tower-square-ratios", "thm-unramified-doubling-gl", "thm-weil-representation-auxiliary-pairs",
        "thm-siegel-weil-weil-range"]
+++
Prove the items in order. The bottom constants are small, and with theta
matching they are constants of the bottom triples, which exist by Howe
duality for real groups. The non-vanishing of $L$-values gives a large norm
and, with the triples, the non-vanishing of the bottom theta lifts. A lower
bound on ratios of $L$-values comes from the toric denominators and the
functional equation. The tower identity is [thm-witt-tower-square-ratios]. Finally, all of
these combine into the valuation bound for the square ratios, without using
the norm formula.
