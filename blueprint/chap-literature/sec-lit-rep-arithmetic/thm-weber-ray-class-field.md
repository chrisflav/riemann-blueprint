+++
kind  = "theorem"
title = "Ray class fields from Weber functions"
provenance = "published"
source = "Weber [weber-1908]; Hasse [hasse-1927]; see Silverman [silverman-1994]"
lean  = ["GlobalTheory.Published.WeberRayFieldSt", "PositivityTheory.Prw.weberRayFieldSt_holds"]
order = 2
+++
Let $K \subset \C$ be an imaginary quadratic field of discriminant less than
$-4$, $L = \mathcal O_K \subset \C$ its lattice of integers, and $n \ge 1$. The
field generated over $K$ by the values of the Weber function of the
elliptic curve $\C/L$ at its $n$-torsion points is a finite abelian extension
of $K$, and it is the ray class field of $K$ of conductor $n\mathcal O_K$.
This is a case of the second main theorem of complex multiplication.
