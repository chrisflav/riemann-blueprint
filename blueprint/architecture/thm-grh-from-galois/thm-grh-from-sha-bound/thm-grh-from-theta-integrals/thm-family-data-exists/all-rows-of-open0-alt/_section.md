+++
id    = "all-rows-of-open0-alt"
kind  = "theorem"
title = "The full list of family conditions from the basic ones"
lean  = ["GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt"]
uses  = ["casselman-wallach", "cusp-rapid-decay", "def-local-parameters",
         "discrete-series-classification", "discrete-series-cover",
         "global-artin-reciprocity", "harish-chandra-modules",
         "siegel-weil-unitary-convergent"]
order = 40
+++
Assume global Artin reciprocity, the convergent Siegel–Weil formula for
unitary groups, the theorems of Harish-Chandra and Casselman–Wallach, the
classification and covering theorems for discrete series, and rapid decay of
cusp forms. Assume also the surjectivity statement and the lower bound on
weights of [onto-x-and-lam-low-of-unitary-group-hypotheses].

Fix a system of local parameters ([def-local-parameters]), construction data
$p$ for the families, and a condition $\mathcal N$ on classes of families.
Suppose that at every admissible datum of the families built from $p$, for
all large auxiliary fields:

* the twelve basic conditions hold ([open0-of-unitary-group-hypotheses]);
* the covolume condition and the functional condition hold;
* the class of families satisfies $\mathcal N$.

Then the full list of family conditions holds there, with the definite-side
condition. The list has 26 entries. *We read* them from their names, and have
unfolded only those proved in the nodes below:

* the twelve basic conditions themselves (primitivity, a condition on
  $\lambda'$, divisors, decomposition points, jumps of the selection, a compatibility condition
  between periods, labels, goodness, weak geometric compatibility,
  multiplicities, a condition on $\kappa$, and defects);
* bounds on class numbers, a condition on $j$-invariants, ranks, and
  divisibility of complements at the constructed points;
* valuations at the level primes, an arithmetic condition, the values and
  periods at the reference point and at the twisted point, and the compatibility condition
  between them ([period-entries-tie-and-level-valuations-at-built]);
* a size bound and a twist condition;
* the bound on small terms, the off-diagonal bound and the lower bound on
  levels ([lg1-s-lp-s-o-h-tf]);
* the reciprocity condition on the selection ([h-serv-of-link-r]);
* a condition on zero loci;
* the counting constants for irreducible constituents ([row-counts-of-labels-alt]);
* the definite-side condition and the condition $\mathcal N$.
