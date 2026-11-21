+++
kind = "proof"
of   = "thm-sha-error-from-local-bounds"
uses = ["thm-borel-casselman", "thm-chevalley-congruence-units", "thm-cusp-bounded-gl", "thm-fontaine-bcris", "thm-green-regular-characters", "thm-hodge-tate-count", "thm-jacquet-irreducible-admissible", "thm-jacquet-shalika-strong-mult-one", "thm-sha-error-from-congruence-bounds", "thm-hc-finiteness-gl", "thm-labesse-base-change", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal", "thm-depth-zero-jacquet-injective", "thm-depth-zero-support", "thm-zelevinsky-segments", "thm-tadic-generic-unitary-dual", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-green-parametrisation", "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-character-local-parameter-above-l", "thm-jacquet-shalika", "thm-ray-class-characters-galois", "thm-ray-class-field", "thm-clozel-regular-algebraic", "thm-disjoint-support-product-irreducible", "thm-p-adic-monodromy", "def-theta-analytic-inputs", "thm-bloch-kato-local", "thm-tate-local-duality-l-adic", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness-padic", "thm-bhatt-scholze-crystalline-lattices"]
+++
The results on representations of $\GL_n$ over local fields, with
[global Artin reciprocity](@thm-artin-reciprocity) and the
[depth-zero support theorem](@thm-depth-zero-support), give the
*character conditions* at the two auxiliary primes $g_0, g_1$ of every
member: at the places above $g_k$ the relevant characters have eigenvalues
$u$ and $u^{-1}$ at a place and its conjugate. Together with the Galois
conditions, these pass to the classes of families. The bound then follows
from [thm-sha-error-from-congruence-bounds]. Along the way the proof uses
the Borel–Casselman theorem [thm-borel-casselman], Chevalley's unit theorem
[thm-chevalley-congruence-units], the boundedness of cusp forms
[thm-cusp-bounded-gl], Green's regular characters
[thm-green-regular-characters], Jacquet–Shalika rigidity
[thm-jacquet-shalika] and the $p$-adic monodromy theorem
[thm-p-adic-monodromy].
