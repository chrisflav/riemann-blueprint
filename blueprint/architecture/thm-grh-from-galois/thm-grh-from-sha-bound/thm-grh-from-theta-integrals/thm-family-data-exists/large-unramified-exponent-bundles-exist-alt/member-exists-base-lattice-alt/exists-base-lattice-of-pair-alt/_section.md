+++
id    = "exists-base-lattice-of-pair-alt"
kind  = "proposition"
title = "Membership from two choices of norms"
lean  = ["GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_pair_alt"]
uses  = ["automorphic-forms-finite-gl", "base-change-definite-unitary-group", "bernstein-unitary-product-irreducible", "bernstein-zelevinsky-finiteness", "car-u-alt", "casselman-wallach", "cheb", "chebotarev-degree-one", "cm-curve-good-outside-prime-st", "cusp-rapid-decay", "cusp-u-alt", "de-rham-potentially-semistable", "def-local-parameters", "depth-zero-jacquet-injective", "discrete-series-cover", "discrete-series-exists", "doubling-method-local-zeta-integrals", "ess-square-integrable-segments", "generic-unitary-dual-gl", "geometric-lemma", "global-artin-reciprocity", "global-euler-char-full", "global-finiteness", "green-cuspidal", "greenberg-wiles", "harish-chandra-finite", "harish-chandra-modules", "hecke-l-adic-character-above", "hecke-l-adic-parameter-above-alt", "hecke-l-partial-continuation", "jacquet-shalika", "local-euler-char", "local-euler-char-k", "local-finiteness", "local-finiteness-k", "local-tate-duality", "local-tate-duality-k", "published-siegel-weil-unitary-convergent", "ray-character-artin", "ray-class-field-st", "regular-algebraic-purity", "schur-orthogonality-square-integrable", "siegel-weil-unitary-convergent", "unlinked-product-irreducible", "unramified-doubling-gl", "unramified-orthogonality", "weber-ray-field-st", "weil-representation-unitary-pair", "weil-unitary"]
order = 2
+++
Let $\rec$ be a system of local parameters ([def-local-parameters]), and let
$N_g \subseteq N$ be two choices of norms for it: every choice allowed by
$N$ refines the choice with a Bloch–Kato law, and every choice allowed by
$N_g$ is allowed by $N$ and is good. Let $p$ and $p_g$ be the construction
data for $N$ and $N_g$. Assume the hypotheses of
[member-exists-base-lattice-alt] and:

* every starting datum extends to a depth-three partial construction for
  $p$, and the level-three upgrade holds for $p$ and for $p_g$;
* partial constructions for $p$ move with changes of the division data;
* at constructed points for $p$ one can pass to an enlarged base at which
  depth-three partial constructions for $p_g$ exist;
* the multiplicity condition of [member-exists-base-lattice-alt] holds
  for $p$.

Then the families built from $p$ satisfy the membership conditions, and at
every good constructed point there is an admissible datum compatible
with $p$.
