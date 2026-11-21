+++
kind  = "lemma"
title = "Assembly of twisted jets"
lean  = ["GlobalTheory.RowClaim.JetsAssembly.twistedJet_succ_eq_assembly",
         "GlobalTheory.RowClaim.JetsAssembly.twisted_jet_one_of_all",
         "GlobalTheory.T.twisted_jets_assemble", "GlobalTheory.T.twisted_pairing_identity"]
uses  = ["thm-grh-from-theta-integrals"]
order = 2
+++
Assume the published results of [thm-grh-from-theta-integrals] and that
the finite sums defining the test vectors are well defined. Then for all
large scales and every choice of test data:

* every term of the expansion of a test vector has an associated volume;
* for every finitely supported coefficient vector $\sigma$ there is
  $\kappa \in \C$ such that, for every term $\beta$ of the expansion, every
  volume and expansion attached to it and every point $y$, the definite
  period of the column function against the top form at $y$ equals
  $\kappa$ times the class sum of the test functional over the cosets of
  $\beta$.

*We read* a jet as a term in the expansion of the test vector along the
tower.
