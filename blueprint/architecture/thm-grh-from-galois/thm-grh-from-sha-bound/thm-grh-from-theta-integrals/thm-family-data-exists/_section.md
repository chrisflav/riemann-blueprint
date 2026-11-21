+++
id    = "thm-family-data-exists"
kind  = "theorem"
title = "The families exist"
lean  = ["UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound",
         "GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt",
         "GlobalTheory.CovTop.CovolumeBoundOfX", "UpperTheory.N.boundAtTwoThree_linked_of_recT"]
uses  = ["def-theta-tower-step", "def-local-parameters", "def-family-data"]
order = 5
+++
Under the hypotheses of [thm-grh-from-theta-integrals], and given local
bounds at the primes $2$ and $3$ for the representations involved, there is
a class of families satisfying the family hypotheses ([def-family-data]).
