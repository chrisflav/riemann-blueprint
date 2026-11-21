+++
kind = "proof"
of   = "thm-family-sha-error-bound"
uses = ["thm-borel-casselman", "thm-cusp-bounded-gl", "thm-discrete-series-exist", "thm-doubling-method", "thm-sha-error-from-local-bounds", "thm-fontaine-bcris", "thm-geometric-lemma-filtration", "thm-hasse-norm-quadratic", "thm-hecke-l-nonvanishing-line-one", "thm-hodge-tate-count", "thm-jacquet-irreducible-admissible", "thm-jacquet-shalika-strong-mult-one", "thm-bz-derivative-leibniz", "thm-downward-theta-lift-nonvanishing", "thm-inner-form-multiplicities-equal", "thm-unramified-doubling-gl", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range", "thm-hc-finiteness-gl", "thm-labesse-base-change", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal", "thm-depth-zero-jacquet-injective", "thm-depth-zero-support", "thm-zelevinsky-segments", "thm-tadic-generic-unitary-dual", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-green-parametrisation", "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-character-local-parameter-above-l", "thm-jacquet-shalika", "thm-tate-euler-characteristic-global-places", "thm-tate-local-finiteness", "thm-tate-local-duality-global-places", "thm-ray-class-characters-galois", "thm-ray-class-field", "thm-clozel-regular-algebraic", "thm-disjoint-support-product-irreducible", "thm-p-adic-monodromy", "def-theta-analytic-inputs", "def-padic-hodge-package", "prop-hecke-integrality-transformation"]
+++
Apply [thm-sha-error-from-local-bounds]. It has two hypotheses beyond the
bound at $2$ and $3$. The first, that each member can be cut down to its
good eigensystems, follows from Chebotarev's density theorem
([thm-chebotarev-degree-one]), local finiteness
([thm-tate-local-finiteness]), local Tate duality
([thm-tate-local-duality-global-places]) and the Euler characteristic
formula ([thm-tate-euler-characteristic-global-places]). The second is a
list of Galois conditions at every member. They come from the $l$-adic
Hodge theory of [def-padic-hodge-package], the analytic inputs of
[def-theta-analytic-inputs], the depth-zero support theorem
([thm-depth-zero-support]), the integrality of the Hecke series of the
members, which we read as [prop-hecke-integrality-transformation], and the
local parameters: the representations $\rho_\pi$ are built by the doubling
method ([thm-doubling-method]) and the non-vanishing of theta lifts
([thm-downward-theta-lift-nonvanishing]), separated by twisted multiplicity
one ([thm-inner-form-multiplicities-equal]) and Jacquet–Shalika rigidity
([thm-jacquet-shalika]), and controlled above $l$ by Fontaine's crystalline
period ring ([thm-fontaine-bcris]).
