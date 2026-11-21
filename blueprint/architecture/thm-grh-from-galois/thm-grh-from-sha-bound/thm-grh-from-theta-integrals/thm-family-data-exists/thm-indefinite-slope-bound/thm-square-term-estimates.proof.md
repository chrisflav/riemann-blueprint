+++
kind = "proof"
of   = "thm-square-term-estimates"
uses = ["thm-bz-finiteness", "thm-cusp-rapid-decay", "thm-doubling-method", "thm-geometric-lemma-filtration", "thm-hasse-norm-quadratic", "thm-siegel-weil-convergent-doubling", "thm-oscillator-lie-action", "thm-witt-tower-square-ratios", "thm-unramified-doubling-gl", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range", "thm-howe-duality-archimedean-trivial", "thm-hecke-functional-equation-cm", "thm-theta-tower-step-identities", "thm-non-endoscopic-hypotheses-hold", "thm-chowla-selberg"]
+++
Prove the items in order, using the step identities of theta towers
([thm-theta-tower-step-identities]) throughout. The bottom constants are
small, and with theta matching they are constants of the bottom triples,
which exist by Howe duality for real unitary dual pairs
([thm-howe-duality-archimedean-trivial]). The non-vanishing of $L$-values
gives a large norm and, with the triples, the non-vanishing of the bottom
theta lifts. A lower bound on ratios of $L$-values comes from the toric
denominators and the absolute value of the
[functional equation of Hecke $L$-functions](@thm-hecke-functional-equation-cm).
The non-vanishing makes [thm-witt-tower-square-ratios] apply, which gives the
tower identity. The archimedean sizes of the conjugates are bounded on
average by the Chowla–Selberg formula ([thm-chowla-selberg]). Finally, all of these combine into the valuation bound for
the square ratios, without using the norm formula. The arithmetic
statements used along the way (denominators of toric periods, transport of
lattice norms, denominators of zeta values and the reflection identity) are
those proved in [thm-non-endoscopic-hypotheses-hold].
