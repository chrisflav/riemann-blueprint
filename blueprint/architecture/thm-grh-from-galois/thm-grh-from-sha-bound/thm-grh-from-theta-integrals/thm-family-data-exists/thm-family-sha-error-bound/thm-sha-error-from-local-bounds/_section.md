+++
id    = "thm-sha-error-from-local-bounds"
kind  = "theorem"
title = "The error bound from local bounds and Galois conditions"
provenance = "new"
lean  = ["UpperTheory.GalC.final_of_alt"]
uses = ["def-local-parameters"]
order = 1
+++
Fix a system of local parameters ([def-local-parameters]) and use the
notation of [thm-family-sha-error-bound]. Suppose:

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
