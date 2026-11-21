+++
id    = "final-of-alt"
kind  = "theorem"
title = "The error bound from local bounds and Galois conditions"
lean  = ["UpperTheory.GalC.final_of_alt"]
uses  = ["automorphic-forms-finite-gl", "base-change-definite-unitary-group", "bernstein-unitary-product-irreducible", "bernstein-zelevinsky-finiteness", "car-u-alt", "cheb", "chebotarev-degree-one", "cusp-rapid-decay", "cusp-u-alt", "de-rham-potentially-semistable", "def-local-parameters", "depth-zero-jacquet-injective", "depth-zero-support", "ess-square-integrable-segments", "generic-unitary-dual-gl", "geometric-galois-rep-compatibility", "geometric-lemma", "global-artin-reciprocity", "green-cuspidal", "harish-chandra-finite", "hecke-l-adic-character-above", "hecke-l-adic-parameter-above-alt", "hypotheses2", "jacquet-shalika", "ray-character-artin", "ray-class-field-st", "regular-algebraic-purity", "unlinked-product-irreducible"]
order = 1
+++
Assume the $l$-adic inputs of [hypotheses2]: Fontaine's crystalline period
ring, global Artin reciprocity, the local theory of Bloch and Kato, local Tate
duality, the local Euler characteristic formula, local finiteness and the
integral comparison theorem of Bhatt and Scholze. Assume also, in the
notation of [final-alt-alt]:

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
