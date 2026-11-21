+++
id    = "close-sph"
kind  = "lemma"
title = "Step identities from local inputs"
lean  = ["PositivityTheory.Sph.Tr.closeSph"]
uses  = ["eis-bl", "siegel-set-unitary", "siegel-weil-std-of-literature"]
order = 10
+++
Assume, for the Weil representations of the dual pairs in theta towers:

* coinvariants at finite places are determined by dictionaries of
  $K$-types, and $\mathrm{SO}$-coinvariants by $K$-finiteness;
* local theta lifts have multiplicity one at ramified places, and the
  relevant spaces are finite-dimensional at ramified, split and inert
  places;
* spherical vectors match in triples;
* the archimedean Lie algebra statements and the $K$-type statement at real
  places;
* reduction theory on Siegel sets ([siegel-set-unitary]), the bound on
  Eisenstein series ([eis-bl]), the Siegel–Weil formula for definite spaces
  ([siegel-weil-std-of-literature]) and existence of the Weil
  representation.

Then theta towers have step identities ([def-theta-tower-step]).
