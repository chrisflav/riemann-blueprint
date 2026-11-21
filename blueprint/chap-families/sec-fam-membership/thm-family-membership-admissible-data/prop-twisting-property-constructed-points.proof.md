+++
kind = "proof"
of   = "prop-twisting-property-constructed-points"
uses = ["thm-abelian-variety-torsion-count", "thm-borel-casselman", "thm-chevalley-congruence-units", "thm-cusp-bounded-gl", "thm-geometric-lemma-filtration", "thm-green-regular-characters", "thm-hasse-norm-quadratic", "thm-jacquet-irreducible-admissible", "thm-jacquet-shalika-strong-mult-one", "thm-landherr-cm", "thm-bz-derivative-leibniz", "thm-unitary-integral-models", "thm-semistable-reduction", "prop-good-twists-from-theta-series", "thm-hc-finiteness-gl", "thm-labesse-base-change", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal", "thm-depth-zero-jacquet-injective", "thm-zelevinsky-segments", "thm-tadic-generic-unitary-dual", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-tate-global-finiteness", "thm-green-parametrisation", "thm-greenberg-wiles", "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-character-local-parameter-above-l", "thm-jacquet-shalika", "thm-tate-euler-characteristic-global-places", "thm-tate-local-finiteness", "thm-tate-local-duality-global-places", "thm-ray-class-characters-galois", "thm-ray-class-field", "thm-clozel-regular-algebraic", "thm-disjoint-support-product-irreducible", "thm-unramified-annihilators", "thm-p-adic-monodromy", "thm-tate-global-euler-characteristic", "thm-poitou-tate", "prop-hecke-integrality-transformation"]
+++
At a constructed point, the choice of norms gives a real side, a series side
and a Galois side with the expected Hodge numbers. The Galois side uses the
Galois representations attached to cuspidal representations of unitary
groups ([thm-galois-reps-polarized-cuspidal]) and Berger's theorem that de
Rham representations are potentially semistable ([thm-p-adic-monodromy]).
Apply [prop-good-twists-from-theta-series] to these three sides. Its proof
uses the rationality and integrality results of
[prop-hecke-integrality-transformation], the finite dimensionality of
spaces of automorphic forms on $\GL_n$ ([thm-hc-finiteness-gl]), and the
Galois cohomology of Poitou–Tate ([thm-poitou-tate]), Tate and
Greenberg–Wiles ([thm-greenberg-wiles]).
