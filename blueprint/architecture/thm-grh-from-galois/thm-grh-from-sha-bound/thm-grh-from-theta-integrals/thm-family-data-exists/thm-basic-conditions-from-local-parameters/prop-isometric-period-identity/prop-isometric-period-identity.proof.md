+++
kind = "proof"
of   = "prop-isometric-period-identity"
uses = ["thm-discrete-series-bessel-pointwise-bound", "thm-hasse-norm-quadratic", "thm-landherr-cm",
        "prop-period-identity-from-diagonal-estimate", "thm-counting-constant-mass-constant", "thm-lattice-term-pair-bound",
        "thm-weighted-bessel-sum-bound"]
+++
The Siegel–Weil formula gives the diagonal estimate that
[prop-period-identity-from-diagonal-estimate] asks for. Its proof uses the
pointwise bound for coefficients of discrete series
([thm-discrete-series-bessel-pointwise-bound]), the uniform weighted bound at
rotated points ([thm-weighted-bessel-sum-bound]), the Hasse norm theorem
and Landherr's classification of hermitian forms. That proposition then
gives the identity at every admissible datum. The multiplicity condition
asks for the identity only eventually in the scale, so it follows.
