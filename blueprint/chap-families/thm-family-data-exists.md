+++
kind  = "theorem"
title = "The families exist"
provenance = "new"
lean  = ["UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound",
         "GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt",
         "GlobalTheory.CovTop.CovolumeBoundOfX", "UpperTheory.N.boundAtTwoThree_linked_of_recT"]
uses  = ["def-family-data"]
order = 1
+++
Suppose that conjugate self-dual and polarized cuspidal representations of
$\GL_a$ over CM fields have Galois representations as in
[thm-galois-reps-csd-above-l] and [thm-galois-reps-polarized-cuspidal].
Then there is a class of families of definite unitary groups
([def-family]) that satisfies the family hypotheses ([def-family-data]).
