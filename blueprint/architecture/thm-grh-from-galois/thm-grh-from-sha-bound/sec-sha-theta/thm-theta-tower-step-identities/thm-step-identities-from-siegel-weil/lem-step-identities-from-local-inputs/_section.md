+++
id    = "lem-step-identities-from-local-inputs"
kind  = "lemma"
title = "Step identities from local inputs"
lean  = ["PositivityTheory.Sph.Tr.closeSph"]
uses  = ["thm-eisenstein-continuation-growth", "thm-reduction-theory-unitary", "thm-siegel-weil-definite"]
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
* reduction theory on Siegel sets ([thm-reduction-theory-unitary]), the bound on
  Eisenstein series ([thm-eisenstein-continuation-growth]), the Siegel–Weil formula for definite spaces
  ([thm-siegel-weil-definite]) and existence of the Weil
  representation.

Then theta towers have step identities ([def-theta-tower-step]).
