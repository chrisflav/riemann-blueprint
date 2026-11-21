+++
id    = "lem-step-identities-from-local-inputs"
kind  = "lemma"
title = "Step identities from local inputs"
lean  = ["PositivityTheory.Sph.Tr.closeSph"]
uses  = ["def-theta-tower-step"]
order = 10
+++
Suppose that the Weil representations of the dual pairs in theta towers
satisfy the following local statements:

* coinvariants at finite places are determined by dictionaries of
  $K$-types, and $\mathrm{SO}$-coinvariants by $K$-finiteness;
* local theta lifts have multiplicity one at ramified places, and the
  relevant spaces are finite-dimensional at ramified, split and inert
  places;
* spherical vectors match in triples;
* the archimedean Lie algebra statements and the $K$-type statement at real
  places hold.

Then theta towers have step identities ([def-theta-tower-step]).
