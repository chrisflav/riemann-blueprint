+++
kind = "proof"
of   = "thm-rational-test-vectors-theta"
uses = ["thm-casselman-wallach", "thm-cusp-uniform-decay", "thm-cusp-rapid-decay",
        "lem-grid-steps-preserve-cusp-forms", "thm-discrete-series-parametrisation", "thm-discrete-series-exist",
        "thm-discrete-series-exist-upq", "thm-hc-modules-unitary", "thm-hasse-norm-quadratic",
        "thm-strong-approximation-su", "lem-twisted-jets-assemble", "lem-twisted-theta-unfolding",
        "thm-weil-representation-auxiliary-pairs"]
+++
The published inputs show that the finite sums are well defined and that
twisted theta lifts of cusp forms are cusp forms ([thm-cusp-rapid-decay],
[thm-cusp-uniform-decay], the discrete series results). With the step
identities and Weil's convergence criterion, the constants are nonzero.
Cuspidality gives convergence and linear independence of the twisted
characters. The lift formula (4) comes from four identities: a twisted
period identity, invariance of the lift under the flips of the tower
([lem-grid-steps-preserve-cusp-forms]), the unfolding of the twisted theta
integral ([lem-twisted-theta-unfolding]) and the assembly of jets
([lem-twisted-jets-assemble]). The rationality (5) follows from (1).
