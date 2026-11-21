+++
id    = "prop-twisting-property-constructed-points"
kind  = "proposition"
title = "The twisting property at constructed points"
lean  = ["GlobalTheory.ExportFirst.exportF_isBuiltE_alt_alt", "GlobalTheory.ExportFirst.exportF_isBuiltE_tyz", "GlobalTheory.Mem.Top.ExportTrue.exportF_prmR_alt_alt", "GlobalTheory.T.automorphy_of_hypotheses_alt_alt"]
uses  = ["thm-hc-finiteness-gl", "thm-labesse-base-change", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal", "thm-p-adic-monodromy", "def-local-parameters", "thm-depth-zero-jacquet-injective", "thm-zelevinsky-segments", "thm-tadic-generic-unitary-dual", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-tate-global-euler-characteristic", "thm-tate-global-finiteness", "thm-green-parametrisation", "thm-greenberg-wiles", "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-character-local-parameter-above-l", "thm-jacquet-shalika", "thm-tate-euler-characteristic-global-places", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness", "thm-tate-local-finiteness-padic", "thm-tate-local-duality-global-places", "thm-tate-local-duality-l-adic", "thm-ray-class-characters-galois", "thm-ray-class-field", "thm-clozel-regular-algebraic", "thm-disjoint-support-product-irreducible", "thm-unramified-annihilators"]
order = 1
+++
Assume the following results from Galois cohomology and class field theory:
Chebotarev's density theorem, Poitou–Tate duality for totally complex
fields, cohomological dimension two, tame local theory, local finiteness,
local Tate duality, the local and global Euler characteristic formulas,
global finiteness, unramified orthogonality, the Greenberg–Wiles formula and
Artin reciprocity for ray class characters. Assume also rationality,
integrality and Hecke-equivariance results for theta series, finite
dimensionality of spaces of automorphic forms on $\GL_n$, that de Rham
representations are potentially semistable, the existence of Galois
representations for cuspidal representations of unitary groups, and a
conclusion on the local situation at every construction.

Let $\rec$ be a system of local parameters ([def-local-parameters]) whose
cuspidal parameters are good at the points of the families. Then for every
choice of norms $N$ that refines the choice with a Bloch–Kato law, and all
further construction data, every constructed point with untwisted twisting
data has the twisting property of
[thm-family-membership-admissible-data].
