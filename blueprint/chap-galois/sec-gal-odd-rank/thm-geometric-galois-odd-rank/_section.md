+++
id    = "thm-geometric-galois-odd-rank"
kind  = "theorem"
title = "Geometric Galois representations in odd rank"
provenance = "new"
lean  = ["UpperTheory.Gal.Int.Geo.GeoOne", "UpperTheory.Gal.Int.Geo.geoOne_holds",
         "UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one"]
order = 1
+++
Let $E$ be a CM field with $E/E^+$ unramified at every finite place and
$[E^+ : \Q]$ even, let $d > 0$ be an integer with $\sqrt{-d} \in E$, and let $l$
be a prime such that $-d$ is a square in $\Q_l$, the places of $E$ that are not
split over $E^+$ lie over primes other than $l$, and they are unramified over
$E^+$. Call a place $w$ of $E$ *admissible* if it is split over $E^+$ and $-d$ is a
square in $\Q_q$ for the prime $q$ below $w$.

Let $a$ be odd and $U$ an automorphic representation of the definite unitary
group $\U_a$ over $E^+$ (Gram matrix $1$) with:

* $U$ is unramified at the non-split places outside a finite set $T$ of them;
* at a place $w_0 \mid l$, $U$ contains a vector on which a torsion-free open
  compact subgroup $J \subset \GL_a(E_{w_0})$ acts by a non-trivial character of
  $l$-power order, and every irreducible representation of $\GL_a(E_{w_0})$
  containing this character of $J$ is cuspidal (a *cuspidal type* at $w_0$);
* $U$ has Satake parameters at the split places away from $w_0$ and a finite set
  $S$;
* at a second place $v' \mid l$, over a different place of $E^+$ than $w_0$, $U$
  has Satake parameters, and for some embedding $\tau$ over $v'$ the numbers
  $k - \lambda_k$ ($1 \le k \le a$) attached to the highest weight $\lambda$ of $U$
  at $\tau$ form a *lacunary* set: no two disjoint non-empty subsets have the
  same mean.

Then there are continuous semisimple representations
$\rho : G_E \to \GL_N(\Qlbar)$, of some dimension $N$ not fixed by the statement,
such that, for $B_w$ the Satake parameters of $U_w$ multiplied by
$q_w^{(a-1)/2}$:

* at all but finitely many admissible $w \nmid l$, $\rho$ is unramified and
  $\iota^{-1}\prod_{b \in B_w}(X - b)$ kills $\rho(\mathrm{Frob}_w^{-1})$; and some
  Hodge–Tate weights of $\rho$ at a place above $l$ form a lacunary set of size
  $a$;
* for each admissible $w \nmid l$ there is such a $\rho$ with this property at
  $w$ as well;
* for each $w \mid l$ apart from $w_0$ and $v'$ (with a condition relating $w$,
  $v'$ and $\sqrt{-d}$), there is such a $\rho$ that is crystalline at $w$ and
  has the numbers $k - \lambda_k$ of the weights of $U$ at $w$ among its
  Hodge–Tate weights, and one for which the crystalline Frobenius at $w$ is
  killed by a power of the Satake polynomial of $U_w$.

Only containment of Frobenius eigenvalues in the Satake parameters is
asserted, not equality: the $a$-dimensional representation is cut out of $\rho$
later ([thm-galois-reps-unramified-compatible]).
