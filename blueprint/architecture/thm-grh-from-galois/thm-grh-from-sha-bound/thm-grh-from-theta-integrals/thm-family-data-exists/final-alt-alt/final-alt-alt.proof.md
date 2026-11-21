+++
kind = "proof"
of   = "final-alt-alt"
uses = ["borel-casselman", "cusp-forms-bounded-gl", "discrete-series-exists", "doubling-method-local-zeta-integrals", "final-of-alt", "fontaine-bcris", "geometric-lemma-filtration", "hasse-norm-st", "hecke-l-partial-continuation", "ht-card", "irreducible-admissible-gl", "jacquet-shalika-rigidity", "leibniz-ord", "lift-inj-and-non-van-type-nz-of-given", "twisted-multiplicity-one", "unramified-doubling-gl", "weil-representation-unitary-pair", "weil-unitary"]
+++
Apply [final-of-alt]. It has two hypotheses beyond the bound at $2$ and $3$.
The first, that each member can be cut down to its good eigensystems, follows
from Chebotarev's density theorem, local finiteness, local Tate duality and
the Euler characteristic formula. The second is a list of Galois conditions
at every member. They come from the published inputs, the depth-zero support
theorem and the local parameters: the representations $\rho_\pi$ are built
by the doubling method and the non-vanishing of theta lifts
([lift-inj-and-non-van-type-nz-of-given]), separated by twisted multiplicity
one ([twisted-multiplicity-one]) and Jacquet–Shalika rigidity, and controlled
above $l$ by Fontaine's crystalline period ring.
