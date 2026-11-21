+++
kind = "proof"
of   = "published-hypotheses-from-patching-alt"
uses = ["borel-casselman", "car-u-alt", "cheb", "chebotarev-degree-one", "cusp-forms-bounded-gl",
        "cuspidal-multiplicity-one", "geometric-lemma-filtration", "hasse-norm-st", "irreducible-admissible-gl",
        "jacquet-shalika-rigidity", "thm-local-parameters-exist"]
+++
Each item is checked separately. Most are the standard inputs for $\GL_n$
specialised to totally real fields: [Jacquet–Shalika rigidity](@jacquet-shalika-rigidity)
gives strong multiplicity one, and the [boundedness of cusp forms](@cusp-forms-bounded-gl)
with [multiplicity one](@cuspidal-multiplicity-one) gives semisimplicity. The
Galois representations for $\GL_2$ over a totally real field come from
quadratic base change to a CM field, where the Galois representations of
polarized pairs exist for the [local parameters](@thm-local-parameters-exist);
[Chebotarev's theorem](@cheb) and the [Hasse norm theorem](@hasse-norm-st)
control the descent back. *We read* the remaining inputs
([Borel–Casselman](@borel-casselman), the [geometric lemma](@geometric-lemma-filtration))
as used for admissibility. Weak descent is passed on unchanged.
