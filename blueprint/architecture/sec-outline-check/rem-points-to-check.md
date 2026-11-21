+++
kind  = "remark"
title = "Points a reader should check"
order = 1
+++
Writing this blueprint turned up statements that are weaker than their
names suggest, or whose role we could not settle. None of them is an error
we have found. They are where a careful reader should look first.

*Local and global compatibility.*
* The local parameters are not the local Langlands correspondence
  ([rem-local-parameters-weak]), and the Galois representations are
  compatible with them only where the parameter is determined
  ([def-galois-reps-polarized]).
* In odd rank, the geometric construction gives a representation of
  unknown dimension on which the Satake polynomial kills Frobenius
  ([thm-geometric-galois-odd-rank]). The transfer to Shimura varieties
  cites no trace formula ([thm-transfer-unitary-shimura]).
* The dual of an abelian scheme is asked to be a scheme over every base
  ([thm-dual-abelian-scheme]); classically it is in general only an
  algebraic space.

*Steps with internal hypotheses.* Some steps take as hypotheses results
proved elsewhere in the argument. The slope bound on the indefinite side
([thm-indefinite-slope-bound]) uses five statements on $L$-values, gathered
in [thm-non-endoscopic-hypotheses-hold]. The ratios of square constants
along a Witt tower ([thm-witt-tower-square-ratios]) assume that certain
Hecke $L$-values do not vanish, which the estimates for square terms
([thm-square-term-estimates]) are to supply. The construction of the family
members ([thm-family-membership-admissible-data]) assumes that cuspidal
multiplicities agree on inner forms, which
[thm-inner-form-multiplicities-equal] proves. A reader should check that
each is discharged where the argument says it is.

*The auxiliary fields.* The bound $|L'/L(1,\chi)| \le C\log x$ for the
characters of the auxiliary fields is not easy for real characters. The
proof gets it, together with a square-root bound for the twisted von
Mangoldt sums on the window, by choosing the auxiliary primes $q, d$
outside a small exceptional set found by a mean-square estimate
([lem-good-auxiliary-primes]). A reader should check this averaging step.

*Published results in special forms.* Among the results of
[chap-literature]:
* Chebotarev's theorem gives only one prime of degree one
  ([thm-chebotarev-degree-one]);
* the Hasse norm theorem is proved for quadratic extensions only
  ([thm-hasse-norm-quadratic]);
* semistable reduction is proved for principally polarised abelian
  varieties over $p$-adic fields ([thm-semistable-reduction]);
* GAGA is proved for sections of line bundles ([thm-gaga-sections]);
* the functional equation of Hecke $L$-functions is proved for CM fields
  ([thm-hecke-functional-equation-cm]);
* the global theorems on $\GL_n$ (Jacquet–Shalika, multiplicity one,
  Gelfand–Kazhdan) are proved over totally complex fields
  ([thm-jacquet-shalika]).

Each of these may be all the argument needs. Two nodes collect other
results under one name ([def-non-endoscopic-package],
[def-automorphic-galois-inputs]), and one entry in the list of published
results is the statement "true" ([def-trivial-statement]).
