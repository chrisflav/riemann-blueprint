+++
kind = "proof"
of   = "thm-hilbert-modular-inputs"
uses = ["thm-borel-casselman", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-cusp-bounded-gl",
        "thm-multiplicity-one-gl", "thm-geometric-lemma-filtration", "thm-hasse-norm-quadratic", "thm-jacquet-irreducible-admissible",
        "thm-jacquet-shalika-strong-mult-one", "thm-local-parameters-exist"]
+++
Each item is checked separately. Most are the standard inputs for $\GL_n$
specialised to totally real fields: [Jacquet–Shalika rigidity](@thm-jacquet-shalika-strong-mult-one)
gives strong multiplicity one, and the [boundedness of cusp forms](@thm-cusp-bounded-gl)
with [multiplicity one](@thm-multiplicity-one-gl) gives semisimplicity. The
Galois representations for $\GL_2$ over a totally real field come from
quadratic base change to a CM field, where the Galois representations of
polarized pairs exist for the [local parameters](@thm-local-parameters-exist);
[Chebotarev's theorem](@thm-chebotarev-degree-one-frobenius) and the [Hasse norm theorem](@thm-hasse-norm-quadratic)
control the descent back. *We read* the remaining inputs
([Borel–Casselman](@thm-borel-casselman), the [geometric lemma](@thm-geometric-lemma-filtration))
as used for admissibility. Weak descent is passed on unchanged.
