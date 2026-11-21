+++
kind = "proof"
of   = "prop-chosen-data-serve-families"
uses = ["prop-standard-data-serve-families", "thm-chebotarev-degree-one-frobenius", "lem-inert-theta-admissibility-cm", "thm-artin-reciprocity"]
+++

Global Artin reciprocity [thm-artin-reciprocity], through Artin symbols of ideal classes and
Chebotarev's theorem for primes of degree one [thm-chebotarev-degree-one-frobenius], gives good models of
CM elliptic curves at primes $l \ge 5$ prime to $d$. From these good models
we get algebraic Taylor coefficients of torsion translates, lattices of
genus-one models, a dictionary between curves and their $l$-adic models,
integrality at inert primes, and the admissibility of
[lem-inert-theta-admissibility-cm]. The reciprocity data
of $p$ say that each chosen datum comes from a standard construction. Apply
[prop-standard-data-serve-families].
