+++
kind = "proof"
of   = "thm-theta-functionals-separate"
uses = ["thm-discrete-series-branching-coefficients", "thm-siegel-weil-convergent-doubling",
        "thm-bessel-period-ascent", "thm-casselman-wallach", "thm-cusp-rapid-decay",
        "thm-discrete-series-parametrisation", "thm-discrete-series-exist",
        "thm-discrete-series-exist-upq", "thm-doubling-method", "thm-hc-finiteness-unitary",
        "thm-hc-modules-unitary", "thm-hasse-norm-quadratic", "thm-unramified-doubling-gl",
        "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range",
        "thm-unitary-quotient-finite-volume"]
+++
Build models of the Weil representations for the separating data, extend the
separating family by a twist using a see-saw pair, and obtain a tower of
multiplicity spaces along the first row. The theta integrals along this
tower converge, since the [adelic quotients have finite volume](@thm-unitary-quotient-finite-volume),
and decay rapidly ([thm-cusp-rapid-decay]). From the statement on matrix
coefficients of discrete series of real unitary groups
([thm-discrete-series-branching-coefficients]), with Harish-Chandra modules
[thm-hc-modules-unitary] and the Casselman–Wallach theorem
[thm-casselman-wallach], the real local periods do not vanish. Howe duality
at unramified places, in the form that for the Weil representation of an
unramified dual pair $\U(V) \times \U(W)$ over a $p$-adic field every vector
fixed by the maximal compact subgroup of one group lies in the span of the
translates of the spherical vector under the other, the Siegel–Weil formula
([thm-siegel-weil-weil-range], [thm-siegel-weil-convergent-doubling]), the
doubling method [thm-doubling-method], [thm-unramified-doubling-gl] and the
discrete series results make the twisting map onto. These give a weak
separation by real functionals; the non-vanishing of Bessel periods up the
tower ([thm-bessel-period-ascent]) and a gap condition on the sizes then
upgrade it to separation by Bessel periods, which is the claim.
