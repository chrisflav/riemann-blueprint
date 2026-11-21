+++
id    = "thm-membership-with-origin"
kind  = "theorem"
title = "Membership for the construction data with origin"
lean  = ["GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_prime_alt", "GlobalTheory.T.member_exists_baseLattice_alt"]
uses  = ["thm-hc-finiteness-gl", "thm-labesse-base-change", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-galois-reps-csd-above-l", "thm-casselman-wallach", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-gross-cm-curves", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal", "thm-p-adic-monodromy", "def-local-parameters", "thm-depth-zero-jacquet-injective", "thm-discrete-series-parametrisation", "thm-discrete-series-exist", "thm-doubling-method", "thm-zelevinsky-segments", "thm-tadic-generic-unitary-dual", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-tate-global-euler-characteristic", "thm-tate-global-finiteness", "thm-green-parametrisation", "thm-greenberg-wiles", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-character-local-parameter-above-l", "thm-hecke-l-nonvanishing-line-one", "thm-jacquet-shalika", "thm-tate-euler-characteristic-global-places", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness", "thm-tate-local-finiteness-padic", "thm-tate-local-duality-global-places", "thm-tate-local-duality-l-adic", "thm-siegel-weil-convergent-doubling", "thm-ray-class-characters-galois", "thm-ray-class-field", "thm-clozel-regular-algebraic", "thm-godement-schur-orthogonality", "thm-siegel-main-theorem-hermitian", "thm-disjoint-support-product-irreducible", "thm-unramified-doubling-gl", "thm-unramified-annihilators", "thm-weber-ray-class-field", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range"]
order = 2
+++
Assume the published results on representations of unitary groups listed
below, the Galois-cohomological results of
[prop-twisting-property-constructed-points], and that every starting configuration
has a saturated refinement with no local conditions. Let $\rec$ be a system of
local parameters ([def-local-parameters]) satisfying the local Langlands
hypotheses of [prop-intermediate-constructions-exist], and let $c$ be
real. Let $p$ be the construction data obtained from $\rec$ by restricting to
origin data for $c$.

Suppose the *multiplicity condition* holds for $p$: at every point of the
families, for inner forms $G_0, G_i$ of the definite unitary groups involved
that are isomorphic at the finite adèles by $\Phi$, every irreducible
admissible representation $\sigma$ occurs in the cuspidal spectrum of $G_0$
with the same multiplicity as $\sigma \circ \Phi^{-1}$ in that of $G_i$.

Then the families built from $p$ satisfy the membership conditions of
[thm-family-membership-admissible-data], and at every good constructed
point there is an admissible datum compatible with $p$.

The results assumed include Jacquet–Shalika, Bernstein–Zelevinsky
finiteness, the geometric lemma, Green's classification, base change for
definite unitary groups, purity of regular algebraic representations, the
doubling method, the Siegel–Weil formula, local Tate duality, the local and
global Euler characteristic formulas and the Greenberg–Wiles formula.
