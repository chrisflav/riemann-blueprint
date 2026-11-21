+++
kind = "proof"
of   = "thm-rational-test-vectors-theta"
uses = ["thm-casselman-wallach", "thm-cusp-uniform-decay", "thm-cusp-rapid-decay",
        "lem-grid-steps-preserve-cusp-forms", "thm-discrete-series-parametrisation", "thm-discrete-series-exist",
        "thm-discrete-series-exist-upq", "thm-hc-modules-unitary", "thm-hasse-norm-quadratic",
        "thm-strong-approximation-su", "lem-twisted-jets-assemble", "lem-twisted-theta-unfolding",
        "thm-weil-representation-auxiliary-pairs", "thm-theta-tower-step-identities",
        "thm-weil-convergence-criterion"]
+++
The step identities of theta towers ([thm-theta-tower-step-identities])
hold along the rows of the grid, and give those of the towers that square
them. Rapid and uniform decay of cusp forms ([thm-cusp-rapid-decay],
[thm-cusp-uniform-decay]) and the results on discrete series
([thm-discrete-series-exist], [thm-discrete-series-exist-upq],
[thm-discrete-series-parametrisation]) show that the finite sums are well
defined and that twisted theta lifts of cusp forms are cusp forms. With the
step identities and [Weil's convergence criterion](@thm-weil-convergence-criterion),
the constants are nonzero. Cuspidality gives convergence and linear
independence of the twisted characters. The lift formula (4) comes from
four identities: a twisted period identity, invariance of the lift under the
flips of the tower ([lem-grid-steps-preserve-cusp-forms]), the unfolding of
the twisted theta integral ([lem-twisted-theta-unfolding]) and the assembly
of jets ([lem-twisted-jets-assemble]). The rationality (5) follows from (1).
