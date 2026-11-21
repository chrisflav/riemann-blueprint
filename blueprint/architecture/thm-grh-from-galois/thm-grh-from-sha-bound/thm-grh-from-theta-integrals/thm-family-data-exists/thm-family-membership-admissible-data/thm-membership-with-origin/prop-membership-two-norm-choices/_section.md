+++
id    = "prop-membership-two-norm-choices"
kind  = "proposition"
title = "Membership from two choices of norms"
lean  = ["GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_pair_alt"]
uses  = ["thm-hc-finiteness-gl", "thm-labesse-base-change", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-galois-reps-csd-above-l", "thm-casselman-wallach", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-gross-cm-curves", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal", "thm-p-adic-monodromy", "def-local-parameters", "thm-depth-zero-jacquet-injective", "thm-discrete-series-parametrisation", "thm-discrete-series-exist", "thm-doubling-method", "thm-zelevinsky-segments", "thm-tadic-generic-unitary-dual", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-tate-global-euler-characteristic", "thm-tate-global-finiteness", "thm-green-parametrisation", "thm-greenberg-wiles", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-character-local-parameter-above-l", "thm-hecke-l-nonvanishing-line-one", "thm-jacquet-shalika", "thm-tate-euler-characteristic-global-places", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness", "thm-tate-local-finiteness-padic", "thm-tate-local-duality-global-places", "thm-tate-local-duality-l-adic", "thm-siegel-weil-convergent-doubling", "thm-ray-class-characters-galois", "thm-ray-class-field", "thm-clozel-regular-algebraic", "thm-godement-schur-orthogonality", "thm-siegel-main-theorem-hermitian", "thm-disjoint-support-product-irreducible", "thm-unramified-doubling-gl", "thm-unramified-annihilators", "thm-weber-ray-class-field", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range"]
order = 2
+++
Let $\rec$ be a system of local parameters ([def-local-parameters]), and let
$N_g \subseteq N$ be two choices of norms for it: every choice allowed by
$N$ refines the choice with a Bloch–Kato law, and every choice allowed by
$N_g$ is allowed by $N$ and is good. Let $p$ and $p_g$ be the construction
data for $N$ and $N_g$. Assume the hypotheses of
[thm-membership-with-origin] and:

* every starting datum extends to a depth-three partial construction for
  $p$, and the level-three upgrade holds for $p$ and for $p_g$;
* partial constructions for $p$ move with changes of the division data;
* at constructed points for $p$ one can pass to an enlarged base at which
  depth-three partial constructions for $p_g$ exist;
* the multiplicity condition of [thm-membership-with-origin] holds
  for $p$.

Then the families built from $p$ satisfy the membership conditions, and at
every good constructed point there is an admissible datum compatible
with $p$.
