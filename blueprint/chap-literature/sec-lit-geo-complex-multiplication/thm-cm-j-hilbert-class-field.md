+++
kind  = "theorem"
title = "The j-invariant generates the Hilbert class field"
source = "Weber [weber-1908]; Hasse [hasse-1927]; see Silverman [silverman-1994]"
lean  = ["GlobalTheory.CompanionTheory.Published.complexMultiplicationJ", "GlobalTheory.Published.ComplexMultiplicationJSt"]
order = 1
+++
Let $K \subset \C$ be an imaginary quadratic field. There is a field
$K \subset H \subset \C$, the Hilbert class field of $K$, with Artin
isomorphism $\mathrm{Art} : \mathrm{Cl}(K) \cong \Gal(H/K)$, such that for
every fractional ideal $\mathfrak a$, viewed as a lattice in $\C$:

* $K(j(\mathfrak a)) = H$;
* $\mathrm{Art}([\mathfrak b])\, j(\mathfrak a) = j(\mathfrak b^{-1}\mathfrak a)$
  for every fractional ideal $\mathfrak b$.

This is the first main theorem of complex multiplication, due to Weber,
Fueter and Hasse.
