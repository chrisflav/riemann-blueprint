+++
id    = "thm-family-conditions-from-basic"
kind  = "theorem"
title = "The full list of family conditions from the basic ones"
provenance = "new"
lean  = ["GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt"]
uses  = ["def-local-parameters"]
order = 40
+++
Fix a system of local parameters ([def-local-parameters]), construction data
$p$ for the families, and a condition $\mathcal N$ on classes of families.
Suppose that at every admissible datum of the families built from $p$, for
all large auxiliary fields:

* the twelve basic conditions hold ([thm-basic-conditions-from-local-parameters]);
* the covolume condition and the functional condition hold;
* the class of families satisfies $\mathcal N$.

Then the full list of family conditions holds there, with the definite-side
condition. The list has 26 entries. We have checked in detail only those proved in
the nodes below:

* the twelve basic conditions themselves (primitivity, a condition on
  $\lambda'$, divisors, decomposition points, jumps of the selection, a compatibility condition
  between periods, labels, goodness, weak geometric compatibility,
  multiplicities, a condition on $\kappa$, and defects);
* bounds on class numbers, a condition on $j$-invariants, ranks, and
  divisibility of complements at the constructed points;
* valuations at the level primes, an arithmetic condition, the values and
  periods at the reference point and at the twisted point, and the compatibility condition
  between them ([prop-periods-valuations-good-data]);
* a size bound and a twist condition;
* the bound on small terms, the off-diagonal bound and the lower bound on
  levels ([prop-small-terms-offdiag-level]);
* the reciprocity condition on the selection ([prop-chosen-data-serve-families]);
* a condition on zero loci;
* the counting constants for irreducible constituents ([prop-counting-constants-constituents]);
* the definite-side condition and the condition $\mathcal N$.
