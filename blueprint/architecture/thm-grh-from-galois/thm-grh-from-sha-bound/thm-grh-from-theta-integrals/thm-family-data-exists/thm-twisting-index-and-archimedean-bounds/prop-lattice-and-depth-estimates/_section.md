+++
id    = "prop-lattice-and-depth-estimates"
kind  = "proposition"
title = "Lattice and depth estimates at the points of a family"
lean  = ["GlobalTheory.BigOn.geoSt_of_pageSt_alt"]
order = 2
+++
Suppose that the basic size conditions hold at the points of the families:
bounds on the size, the scale, the bad primes, the level and a parameter
$Y$, and agreement of the error constant with its definition. Then at every
point at a large scale, and for every large enough constant $c$:

* the lattices $M_j$ are full and stable under the finite group that acts
  on them, and the lattices attached to the archimedean places are full;
* an index bound holds at pairs of places;
* for every $C$, four depth bounds hold: at good primes, at the ramified
  primes $q$ and $d$ of the auxiliary field ([def-sha-bound]), at $2$, and
  at the primes of the level.

For example, the bound at good primes says this. For every finite set $Q$ of
primes, auxiliary weights $\vartheta_p, a_p \ge 0$ satisfy
$\sum_{p \in Q}\vartheta_p\log p \le C/k$ and
$T\sum_{p \in Q}a_p\log p \le Cmb$. At a twisting place $w$ over a good prime,
the local exponents satisfy $e_0(w), e_0(\bar w) \le F_j(w) + a_j(p_w) + 1$
if $p_w \le Y$, and $e_0(w) = e_0(\bar w) = 0 \le F_j(w)$ if $p_w > Y$.
