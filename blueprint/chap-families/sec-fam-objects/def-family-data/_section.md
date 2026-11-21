+++
id    = "def-family-data"
kind  = "definition"
title = "Families of definite unitary groups"
provenance = "new"
lean  = ["GlobalTheory.Fc.HypsAlt"]
uses  = ["def-sha-error-term", "def-family"]
order = 1
+++
Fix a primitive character $\psi$ and a scale $x$. The families of the proof
([def-family]) consist of members ([def-family-member]): chains of definite
unitary groups over an auxiliary CM field ([def-auxiliary-field-data],
[thm-auxiliary-fields]) of ranks $N(j) = k + j(t+1)$, $0 \le j \le m$, with
$m^2 \le k + m(t+1)$ ([def-family-ranks]). Consecutive groups of a chain are
linked by theta lifts and carry lattices. A class of families *satisfies the
family hypotheses* if, in about fifty conditions:

* the lattices satisfy bounds, admissibility after twisting, and divisibility conditions;
* the class number formula holds for the standard lattices;
* gaps decay, and the spaces of automorphic forms involved are
  finite-dimensional with controlled counting constants;
* the Siegel mass formula holds in the form needed: masses at the prime
  2, mass ratios under change of volume, and independence of the signature;
* points and periods are admissible after twisting, the projections of the
  lattices are surjective, and the counts of irreducible constituents are
  bounded;
* the Tate–Shafarevich error bound holds ([def-sha-error-term]).

*It is not clear* how each condition is used. We list them as they stand.
