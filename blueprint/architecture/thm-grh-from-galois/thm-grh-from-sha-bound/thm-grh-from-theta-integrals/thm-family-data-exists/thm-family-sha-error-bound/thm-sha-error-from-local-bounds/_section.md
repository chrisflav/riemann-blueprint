+++
id    = "thm-sha-error-from-local-bounds"
kind  = "theorem"
title = "The error bound from local bounds and Galois conditions"
lean  = ["UpperTheory.GalC.final_of_alt"]
uses  = ["thm-hc-finiteness-gl", "thm-labesse-base-change", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal", "thm-p-adic-monodromy", "def-local-parameters", "thm-depth-zero-jacquet-injective", "thm-depth-zero-support", "thm-zelevinsky-segments", "thm-tadic-generic-unitary-dual", "def-theta-analytic-inputs", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-green-parametrisation", "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-character-local-parameter-above-l", "def-padic-hodge-package", "thm-jacquet-shalika", "thm-ray-class-characters-galois", "thm-ray-class-field", "thm-clozel-regular-algebraic", "thm-disjoint-support-product-irreducible"]
order = 1
+++
Assume the $l$-adic inputs of [def-padic-hodge-package]: Fontaine's crystalline period
ring, global Artin reciprocity, the local theory of Bloch and Kato, local Tate
duality, the local Euler characteristic formula, local finiteness and the
integral comparison theorem of Bhatt and Scholze. Assume also, in the
notation of [thm-family-sha-error-bound]:

* (*cutting*) every member satisfying the conditions below has, at each
  local datum, a Hecke-equivariant endomorphism of its space of forms that
  acts by a fixed nonzero integer on the good eigensystems and by $0$ on the
  others, and the conditions survive the cut;
* (*Galois conditions*) from some scale on, every member satisfies about
  twenty conditions on its Galois representations: residual
  irreducibility, admissible tame eigenvalues, weight and block parameters,
  depth-zero conditions at the unramified places, uniqueness of
  localisation, and others;
* the bound at $2$ and $3$.

Then the classes of families built from the local parameters satisfy the
Tate–Shafarevich error bound ([def-sha-error-term]).
