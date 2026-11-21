+++
kind = "proof"
of   = "prop-chosen-data-serve-families"
uses = ["thm-chebotarev-degree-one-frobenius", "lem-inert-theta-admissibility-cm",
        "thm-artin-reciprocity", "lem-kernel-conditions-standard-data",
        "lem-local-models-constructed-points"]
+++

Global Artin reciprocity [thm-artin-reciprocity], through Artin symbols of
ideal classes and Chebotarev's theorem for primes of degree one
[thm-chebotarev-degree-one-frobenius], gives good models of CM elliptic
curves at primes $l \ge 5$ prime to $d$. From these good models we get six
facts about elliptic curves $\C/\mathfrak c$ with complex multiplication by
$O_K$, each with a twelfth root $\delta$ of its discriminant:

* the Taylor coefficients of the normalised theta functions at torsion
  translates are algebraic;
* at every prime $l \ge 5$ inert in $K$ there is a genus-one model over
  $\C_l$ with good reduction, carrying the same lattice;
* such models come with a dictionary to the Weierstrass invariants and the
  $l$-adic sigma function;
* the theta data are integral at inert primes;
* the theta data at inert primes are admissible
  ([lem-inert-theta-admissibility-cm]);
* the needed $l$-adic curves exist.

The reciprocity data of $p$ say that each chosen datum comes from a
standard construction and has a standard kernel. The two parts of "serves"
are then proved separately. Local lattice models come from
[lem-local-models-constructed-points], which uses the last two facts. The
kernel conditions come from [lem-kernel-conditions-standard-data], which
uses the first four.
