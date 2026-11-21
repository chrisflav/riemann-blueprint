+++
kind  = "remark"
title = "Points a reader should check"
order = 10
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

*Hypotheses passed up the argument.* Some steps take hypotheses that are
discharged higher up. Examples are statements about $L$-values on the
indefinite side ([thm-indefinite-slope-bound]), non-vanishing of Hecke
$L$-values ([thm-witt-tower-square-ratios]), and equality of multiplicities
on inner forms ([thm-inner-form-multiplicities-equal]). We have not traced
each one to the place where it is proved.

*The auxiliary fields.* The bound $|L'/L(1,\chi)| \le C\log x$ for the
characters of the auxiliary fields is not easy for real characters, and we
could not see how it is proved ([thm-auxiliary-fields]).

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

Each of these may be all the argument needs. Several nodes also collect
other results under one name ([def-non-endoscopic-package],
[def-automorphic-galois-inputs]), and one of them is the trivially true
statement ([def-trivial-statement]).
