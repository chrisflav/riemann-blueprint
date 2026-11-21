+++
kind = "proof"
of   = "thm-family-sha-error-bound"
uses = ["thm-borel-casselman", "thm-cusp-bounded-gl", "thm-discrete-series-exist", "thm-doubling-method", "thm-sha-error-from-local-bounds", "thm-fontaine-bcris", "thm-geometric-lemma-filtration", "thm-hasse-norm-quadratic", "thm-hecke-l-nonvanishing-line-one", "thm-hodge-tate-count", "thm-jacquet-irreducible-admissible", "thm-jacquet-shalika-strong-mult-one", "thm-bz-derivative-leibniz", "thm-downward-theta-lift-nonvanishing", "thm-inner-form-multiplicities-equal", "thm-unramified-doubling-gl", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range"]
+++
Apply [thm-sha-error-from-local-bounds]. It has two hypotheses beyond the bound at $2$ and $3$.
The first, that each member can be cut down to its good eigensystems, follows
from Chebotarev's density theorem, local finiteness, local Tate duality and
the Euler characteristic formula. The second is a list of Galois conditions
at every member. They come from the published inputs, the depth-zero support
theorem and the local parameters: the representations $\rho_\pi$ are built
by the doubling method and the non-vanishing of theta lifts
([thm-downward-theta-lift-nonvanishing]), separated by twisted multiplicity
one ([thm-inner-form-multiplicities-equal]) and Jacquet–Shalika rigidity, and controlled
above $l$ by Fontaine's crystalline period ring.
