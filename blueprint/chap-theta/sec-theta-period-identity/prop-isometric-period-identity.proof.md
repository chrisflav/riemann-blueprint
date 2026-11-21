+++
kind = "proof"
of   = "prop-isometric-period-identity"
uses = ["thm-discrete-series-bessel-pointwise-bound", "thm-hasse-norm-quadratic",
        "thm-landherr-cm", "thm-counting-constant-mass-constant", "thm-lattice-term-pair-bound",
        "thm-weighted-bessel-sum-bound", "thm-casselman-wallach", "thm-cusp-rapid-decay",
        "thm-hc-discrete-series-classification", "thm-discrete-series-parametrisation",
        "thm-doubling-method", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary",
        "thm-siegel-weil-convergent-doubling", "thm-siegel-main-theorem-hermitian",
        "thm-strong-approximation-su", "thm-unramified-doubling-gl",
        "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range",
        "prop-period-identity-real-package"]
+++
We argue in three steps.

1. *A diagonal estimate.* The Siegel–Weil formula
   ([thm-siegel-weil-weil-range]) gives, at every scale with bounded
   constant $C_\Gamma$, the two-term bound
   $$4\big(e^{C m_L} + 1\big), \qquad 4e^{-k/2} + 2e^{-k}$$
   on the diagonal terms, and the rank identity
   $d_0 = d^*\,(T^{k} - 1)^{f}$ for each member. Its proof uses the
   pointwise bound for coefficients of discrete series
   ([thm-discrete-series-bessel-pointwise-bound]), the uniform weighted
   bound at rotated points ([thm-weighted-bessel-sum-bound]), the Hasse norm
   theorem ([thm-hasse-norm-quadratic]) and Landherr's classification of
   hermitian forms ([thm-landherr-cm]).
2. *Conditions at points.* Every good point carries real data. By the
   classification of discrete series
   ([thm-hc-discrete-series-classification],
   [thm-discrete-series-parametrisation]), Harish-Chandra's theorems
   ([thm-hc-finiteness-unitary], [thm-hc-modules-unitary]), the
   Casselman–Wallach theorem ([thm-casselman-wallach]) and the rapid decay
   of cusp forms ([thm-cusp-rapid-decay]), the following hold at every good
   admissible datum: the real realisation joins with the spectral data, the
   decomposition point condition holds, frames exist and the realisation
   extends, the primitivity and separation of types hold, the spectral data
   are finite, the spectral gap is at least $100r^4$ and the node gap holds,
   and $r_S \ge 1$.
3. *The identity.* At a good datum these conditions show that the attached
   real package satisfies all family conditions, and the diagonal estimate
   shows that the projections $P_u$ do not vanish on the ramified part.
   With $r_S \ge 1$, [prop-period-identity-real-package] gives the identity
   at every good admissible datum.

The multiplicity condition asks for the identity only eventually in the
scale, so it follows.

Along the way the argument uses unramified Howe duality, in this form: in
the Weil representation of an unramified local dual pair
([thm-weil-representation-auxiliary-pairs]), the vectors fixed by the
maximal compact subgroup of one group lie in the span of the orbit of the
vacuum vector under the other group.
