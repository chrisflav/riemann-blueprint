+++
kind = "proof"
of   = "thm-siegel-weil-weil-range"
uses = ["thm-hasse-norm-quadratic", "lem-siegel-weil-singular-coefficients", "thm-reduction-theory-unitary", "thm-weil-representation-auxiliary-pairs", "thm-weil-convergence-criterion"]
+++
Weil's convergence criterion, using reduction theory on Siegel sets, gives
the bound. The identity follows by unfolding the Eisenstein series and
comparing Fourier coefficients: for non-singular coefficients this is
Siegel's mass computation, and for singular ones [lem-siegel-weil-singular-coefficients]. Hasse's norm
theorem and the existence of the Weil representation are used.
