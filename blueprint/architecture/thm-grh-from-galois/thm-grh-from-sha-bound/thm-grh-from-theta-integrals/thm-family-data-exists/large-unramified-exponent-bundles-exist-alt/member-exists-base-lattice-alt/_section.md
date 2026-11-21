+++
id    = "member-exists-base-lattice-alt"
kind  = "theorem"
title = "Membership for the construction data with origin"
lean  = ["GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_prime_alt", "GlobalTheory.T.member_exists_baseLattice_alt"]
uses  = ["automorphic-forms-finite-gl", "base-change-definite-unitary-group", "bernstein-unitary-product-irreducible", "bernstein-zelevinsky-finiteness", "car-u-alt", "casselman-wallach", "cheb", "chebotarev-degree-one", "cm-curve-good-outside-prime-st", "cusp-rapid-decay", "cusp-u-alt", "de-rham-potentially-semistable", "def-local-parameters", "depth-zero-jacquet-injective", "discrete-series-cover", "discrete-series-exists", "doubling-method-local-zeta-integrals", "ess-square-integrable-segments", "generic-unitary-dual-gl", "geometric-lemma", "global-artin-reciprocity", "global-euler-char-full", "global-finiteness", "green-cuspidal", "greenberg-wiles", "harish-chandra-finite", "harish-chandra-modules", "hecke-l-adic-character-above", "hecke-l-adic-parameter-above-alt", "hecke-l-partial-continuation", "jacquet-shalika", "local-euler-char", "local-euler-char-k", "local-finiteness", "local-finiteness-k", "local-tate-duality", "local-tate-duality-k", "published-siegel-weil-unitary-convergent", "ray-character-artin", "ray-class-field-st", "regular-algebraic-purity", "schur-orthogonality-square-integrable", "siegel-weil-unitary-convergent", "unlinked-product-irreducible", "unramified-doubling-gl", "unramified-orthogonality", "weber-ray-field-st", "weil-representation-unitary-pair", "weil-unitary"]
order = 2
+++
Assume the published results on representations of unitary groups listed
below, the Galois-cohomological results of
[automorphy-of-hypotheses-alt-alt], and that every starting configuration
has a saturated refinement with no local conditions. Let $\rec$ be a system of
local parameters ([def-local-parameters]) satisfying the local Langlands
hypotheses of [all-stages-at-member-of-specializations-alt], and let $c$ be
real. Let $p$ be the construction data obtained from $\rec$ by restricting to
origin data for $c$.

Suppose the *multiplicity condition* holds for $p$: at every point of the
families, for inner forms $G_0, G_i$ of the definite unitary groups involved
that are isomorphic at the finite adèles by $\Phi$, every irreducible
admissible representation $\sigma$ occurs in the cuspidal spectrum of $G_0$
with the same multiplicity as $\sigma \circ \Phi^{-1}$ in that of $G_i$.

Then the families built from $p$ satisfy the membership conditions of
[large-unramified-exponent-bundles-exist-alt], and at every good constructed
point there is an admissible datum compatible with $p$.

The results assumed include Jacquet–Shalika, Bernstein–Zelevinsky
finiteness, the geometric lemma, Green's classification, base change for
definite unitary groups, purity of regular algebraic representations, the
doubling method, the Siegel–Weil formula, local Tate duality, the local and
global Euler characteristic formulas and the Greenberg–Wiles formula.
