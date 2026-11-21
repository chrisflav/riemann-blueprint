+++
id    = "prop-standard-data-serve-families"
kind  = "proposition"
title = "Standard data serve their families"
provenance = "new"
lean  = ["GlobalTheory.Svd.servH_row", "GlobalTheory.T.bundle_bothParts_of_standardKernel_and_six_hypotheses"]
order = 2
+++

Assume six facts about elliptic curves $\C/\mathfrak c$ with complex
multiplication by $O_K$, each with a twelfth root $\delta$ of its
discriminant:

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

Then any choice of admissible data, each of which comes from a standard
construction and has a standard kernel, serves its family in the sense of
[prop-chosen-data-serve-families].
