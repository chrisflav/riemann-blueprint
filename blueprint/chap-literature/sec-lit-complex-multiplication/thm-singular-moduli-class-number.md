+++
kind  = "theorem"
title = "Singular moduli and the class number"
provenance = "published"
source = "Weber [weber-1908]; Hasse [hasse-1927]; see Silverman [silverman-1994]"
lean  = ["GlobalTheory.Laid.hcfj_holds", "GlobalTheory.Published.HilbertClassFieldJ",
         "GlobalTheory.Published.IdealInvariantsOneOrbitSt", "PositivityTheory.Prw.idealInvariantsOneOrbitSt_holds"]
order = 2
+++
Let $K \subset \C$ be an imaginary quadratic field with class number $h$.
Then $K(j(\mathcal O_K))$ is the Hilbert class field of $K$ and has degree
$h$ over $K$; for fractional ideals $\mathfrak a, \mathfrak b$ one has
$j(\mathfrak a) = j(\mathfrak b)$ exactly when $\mathfrak a$ and
$\mathfrak b$ lie in the same class; there are exactly $h$ values
$j(\mathfrak a)$, and they are the conjugates of $j(\mathcal O_K)$ over $K$.

In particular, for every fractional ideal $\mathfrak a$ the number
$j(\mathfrak a)$ is algebraic, and its orbit under $\mathrm{Aut}(\C/K)$ is the
set of all $j(\mathfrak b)$, $\mathfrak b$ a fractional ideal of $\mathcal O_K$.
