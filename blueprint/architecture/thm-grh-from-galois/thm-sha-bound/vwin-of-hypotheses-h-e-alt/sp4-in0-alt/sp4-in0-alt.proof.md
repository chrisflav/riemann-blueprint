+++
kind = "proof"
of   = "sp4-in0-alt"
uses = ["base-change-definite-unitary-group", "bloch-kato-local", "borel-casselman", "car-u-alt", "cheb",
        "chebotarev-degree-one", "cusp-forms-bounded-gl", "cuspidal-multiplicity-one", "def-local-parameters",
        "depth-zero-support", "fontaine-bcris", "generic-unitary-dual-gl", "geometric-lemma-filtration",
        "global-euler-char-full", "global-finiteness", "greenberg-wiles", "hasse-norm-st",
        "hecke-l-adic-character", "hecke-l-adic-character-de-rham", "ind-cs", "irreducible-admissible-gl",
        "jacquet-shalika-rigidity", "local-euler-char", "local-euler-char-k", "local-finiteness",
        "local-finiteness-k", "local-tate-duality", "local-tate-duality-k", "poitou-tate-normalised",
        "seed-i-is-alt", "thm-local-parameters-exist", "unramified-orthogonality"]
+++
A potential automorphy argument; *we read* its steps from the names of its
inputs. [seed-i-is-alt] gives automorphic seed
points in a tower of potential modularity; automorphic induction
([ind-cs]) and [base change from definite unitary groups](@base-change-definite-unitary-group)
carry automorphy between the 2-dimensional and 4-dimensional
representations involved. A lifting step for the adjoint representation,
with the theorem of Ferrero and Washington to control the relevant class
groups, spreads automorphy from the seeds to all irreducible lifts. The
[Greenberg–Wiles formula](@greenberg-wiles), the [Poitou–Tate sequence](@poitou-tate-normalised)
and the local theory of Galois cohomology bound the tangent spaces, which
gives finiteness of the ring of traces; the absence of block-diagonal lifts
comes from the irreducibility of the seeds.
