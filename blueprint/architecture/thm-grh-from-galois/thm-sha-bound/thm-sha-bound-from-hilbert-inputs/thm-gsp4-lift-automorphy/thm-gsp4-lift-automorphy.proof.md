+++
kind = "proof"
of   = "thm-gsp4-lift-automorphy"
uses = ["thm-labesse-base-change", "thm-bloch-kato-local", "thm-borel-casselman", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius",
        "thm-chebotarev-degree-one", "thm-cusp-bounded-gl", "thm-multiplicity-one-gl", "def-local-parameters",
        "thm-depth-zero-support", "thm-fontaine-bcris", "thm-tadic-generic-unitary-dual", "thm-geometric-lemma-filtration",
        "thm-tate-global-euler-characteristic", "thm-tate-global-finiteness", "thm-greenberg-wiles", "thm-hasse-norm-quadratic",
        "thm-hecke-l-adic-character", "thm-hecke-l-adic-character-de-rham", "thm-automorphic-induction-quadratic", "thm-jacquet-irreducible-admissible",
        "thm-jacquet-shalika-strong-mult-one", "thm-tate-euler-characteristic-global-places", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness",
        "thm-tate-local-finiteness-padic", "thm-tate-local-duality-global-places", "thm-tate-local-duality-l-adic", "thm-poitou-tate",
        "thm-potential-automorphy-seeds", "thm-local-parameters-exist", "thm-unramified-annihilators"]
+++
A potential automorphy argument, which we have not checked in detail. [thm-potential-automorphy-seeds] gives automorphic seed
points in a tower of potential modularity; automorphic induction
([thm-automorphic-induction-quadratic]) and [base change from definite unitary groups](@thm-labesse-base-change)
carry automorphy between the 2-dimensional and 4-dimensional
representations involved. A lifting step for the adjoint representation,
with the theorem of Ferrero and Washington to control the relevant class
groups, spreads automorphy from the seeds to all irreducible lifts. The
[Greenberg–Wiles formula](@thm-greenberg-wiles), the [Poitou–Tate sequence](@thm-poitou-tate)
and the local theory of Galois cohomology bound the tangent spaces, which
gives finiteness of the ring of traces; the absence of block-diagonal lifts
comes from the irreducibility of the seeds.
