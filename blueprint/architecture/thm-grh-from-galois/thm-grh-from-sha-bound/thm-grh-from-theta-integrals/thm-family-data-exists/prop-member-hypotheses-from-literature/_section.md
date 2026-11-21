+++
id    = "prop-member-hypotheses-from-literature"
kind  = "proposition"
title = "The published inputs give the hypotheses on the members"
lean  = ["GlobalTheory.MemberClose.exists_hyp_n_of_geometric_galois_compat",
         "GlobalTheory.T.hyps_e_third_layer_ser_n_of_geometric_galois"]
uses  = ["thm-hc-finiteness-gl", "thm-labesse-base-change", "thm-bernstein-unitary-product",
         "thm-bz-finiteness", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal",
         "thm-p-adic-monodromy", "def-local-parameters", "thm-depth-zero-jacquet-injective",
         "thm-zelevinsky-segments", "thm-tadic-generic-unitary-dual", "def-theta-analytic-inputs",
         "thm-geometric-lemma", "thm-artin-reciprocity", "thm-tate-global-euler-characteristic", "thm-tate-global-finiteness", "thm-green-parametrisation",
         "thm-greenberg-wiles", "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-character-local-parameter-above-l",
         "thm-jacquet-shalika", "thm-tate-euler-characteristic-global-places", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness", "thm-tate-local-finiteness-padic",
         "thm-tate-local-duality-global-places", "thm-tate-local-duality-l-adic", "def-non-endoscopic-package", "thm-ray-class-characters-galois",
         "thm-ray-class-field", "thm-clozel-regular-algebraic", "thm-disjoint-support-product-irreducible", "thm-unramified-annihilators"]
order = 122
+++
Assume the published results on local representation theory of $\GL_n$,
on automorphic forms and their Galois representations, on Galois
cohomology, and the functional equation of Hecke $L$-functions, collected
in [def-non-endoscopic-package], and the compatibility of geometric
Galois representations [def-theta-analytic-inputs]. Then:

1. the Galois-cohomological inputs hold together: Chebotarev density,
   Poitou–Tate duality over totally complex fields, cohomological dimension
   two, the tame local theory, local finiteness, Tate duality and the Euler
   characteristic formula, global finiteness and the global Euler
   characteristic formula, orthogonality of unramified characters, the
   matching of archimedean signatures and the Greenberg–Wiles formula;
2. the published inputs on theta lifts, cusp forms, Green's
   characters, ray class fields, base change for definite unitary groups and
   the unitary dual of $\GL_n$ hold together;
3. the rationality and integrality statements for Hecke operators on the
   members hold ([prop-hecke-integrality-transformation]);
4. there is a system of local parameters ([def-local-parameters]) that is
   compatible with the archimedean local Langlands correspondence and with
   the parameters and points of the members.

This is a collecting statement: it assembles the hypotheses of the later
steps from the literature.
