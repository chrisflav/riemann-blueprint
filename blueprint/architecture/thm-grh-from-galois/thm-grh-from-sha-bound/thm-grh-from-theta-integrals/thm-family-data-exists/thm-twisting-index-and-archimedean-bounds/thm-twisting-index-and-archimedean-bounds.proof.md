+++
kind = "proof"
of   = "thm-twisting-index-and-archimedean-bounds"
uses = ["thm-abelian-variety-torsion-count", "thm-bz-finiteness", "thm-cusp-decay-sobolev", "thm-doubling-method", "thm-full-level-ample-models", "prop-exponent-bounds-twisting-places", "thm-formal-degree-upq", "prop-lattice-and-depth-estimates", "thm-artin-reciprocity", "thm-hc-modules-unitary", "thm-hasse-norm-quadratic", "thm-landherr-cm", "thm-unitary-integral-models", "thm-siegel-weil-convergent-doubling", "thm-ray-class-field", "prop-height-inequalities-at-points", "thm-godement-schur-orthogonality", "thm-semistable-reduction", "thm-siegel-eisenstein-continuation", "thm-unramified-doubling-gl", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range", "thm-labesse-base-change", "thm-bhatt-scholze-coefficients", "thm-casselman-wallach", "thm-chebotarev-degree-one", "thm-clozel-cohomological", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal", "thm-discrete-series-parametrisation", "thm-green-parametrisation", "thm-hecke-l-adic-character", "thm-hecke-l-adic-character-above-l"]
+++
*Index bounds.* The $l$-adic characters attached to algebraic Hecke
characters ([thm-hecke-l-adic-character]) give Artin reciprocity, and with it ray
class fields. With the Casselman–Wallach theorem this gives the local
statements needed at the archimedean places. Size estimates at the points
of a family give the lattice and depth estimates of [prop-lattice-and-depth-estimates],
and from these a bound on ranks and on the twists at the twisting places.
Green's classification ([thm-green-parametrisation]) handles the bad places, and
[prop-exponent-bounds-twisting-places] bounds the exponents
$J_j(w)$. Together these give the index bounds.

*Archimedean lower bound.* Along the family the weights of the theta lifts
have the expected sizes. The Siegel–Weil formula, the doubling method and its
unramified computation, the finiteness theorem of Bernstein and Zelevinsky
and the formal degrees of compact duals turn these sizes into the lower
bound on $\log\lambda_j$.
