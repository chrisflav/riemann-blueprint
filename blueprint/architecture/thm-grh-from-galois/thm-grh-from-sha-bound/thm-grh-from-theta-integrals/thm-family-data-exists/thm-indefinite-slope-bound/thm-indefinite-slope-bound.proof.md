+++
kind = "proof"
of   = "thm-indefinite-slope-bound"
uses = ["thm-bz-finiteness", "thm-casselman-wallach", "thm-cusp-rapid-decay",
        "thm-discrete-series-parametrisation", "thm-discrete-series-exist", "thm-discrete-series-exist-upq",
        "thm-doubling-method", "thm-geometric-lemma-filtration",
        "thm-artin-reciprocity", "thm-hc-modules-unitary", "thm-hasse-norm-quadratic",
        "thm-howe-duality-archimedean-trivial", "thm-siegel-weil-convergent-doubling",
        "thm-oscillator-lie-action", "thm-reduction-theory-unitary", "thm-square-term-estimates",
        "thm-rational-test-vectors-theta", "thm-unramified-doubling-gl",
        "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range"]
+++
The estimates on the leading square term ([thm-square-term-estimates])
give the bounds on $L$-values and the Witt tower identity. The rational
test vectors of [thm-rational-test-vectors-theta] give finite rational sums
with nonzero constants. Separation
([thm-theta-functionals-separate]) makes the test
functionals injective. A size bound at all places, a bound
$|L'/L(1,\chi)| \le x^{\varepsilon}$, toric ratio estimates and the
rationality of the square ratios then give a function on the grid of
evaluation points with the required properties. A scaling bound turns it
into the slope inequality at the point $0$ of the grid.
