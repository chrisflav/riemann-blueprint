+++
id    = "lem-local-models-constructed-points"
kind  = "lemma"
title = "Local models at constructed points"
provenance = "new"
lean  = ["GlobalTheory.Svd.modelsAt_bpt", "GlobalTheory.Svd.modelsAt_of_part", "GlobalTheory.T.tuplesHaveLocalModels_at_constructedPoint_over_trueColumns", "GlobalTheory.T.tuplesHaveLocalModels_of_standardColumnObjects"]
order = 1
+++

Assume the admissibility of theta data at inert primes
([lem-inert-theta-admissibility-cm]) and that the needed
$l$-adic CM curves exist. Let a point of a family come from a standard
construction. Then the twisted hermitian forms of the point have local
models: for every tuple $\mu$ in use, every member $u$ and every place $w$
over the level prime of $u$ outside the exceptional set of $\mu$, there is a
chain of lattices at $w$ that is compatible with the comparison maps and
admissible at $w$, provided the rank satisfies $2r_G \le k$.
