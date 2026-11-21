+++
kind  = "theorem"
title = "Galois representations compatible at unramified places"
provenance = "new"
lean  = ["UpperTheory.Gal.Int.coreAll_of"]
uses  = ["thm-theta-lift-nonvanishing"]
order = 1
+++
Suppose that, for odd $a$, definite unitary groups $\U_a$ over CM fields
satisfy:

* (*seed*) every automorphic representation $U$ with a cuspidal type at a
  place $w_0 \mid l$ and lacunary weights at a second place $v' \mid l$ has a
  continuous semisimple $r : G_E \to \GL_a(\Qlbar)$ whose Frobenius
  characteristic polynomials at almost all admissible places (as in
  [thm-geometric-galois-odd-rank]) equal the
  Satake polynomials of $U$, on a dense open set of Frobenius elements;
* (*congruences*) the Hecke eigensystem of every automorphic representation
  is an $l$-adic limit of eigensystems of representations with such a type
  and such weights, of the same weight away from $w_0$ and $v'$;

and that theta lifts from definite unitary groups do not vanish
([thm-theta-lift-nonvanishing]). Let $E$ be a CM field, $a \ge 1$, and
$(\pi, \chi)$ a polarized regular algebraic cuspidal pair on $\GL_a(\A_E)$.
Then there is a continuous $r : G_E \to \GL_a(\Qlbar)$ attached to $\pi$ at
almost all places, and every such $r$ satisfies, at every place $w$ where
$\pi_w$ is unramified with Satake parameters $B$:

* if $w \nmid l$, $\iota\,\mathrm{charpoly}\, r(\mathrm{Frob}_w^{-1})$ has the roots $q_w^{(a-1)/2}B$;
* if $w \mid l$, $r$ is de Rham and crystalline at $w$ with the Hodge–Tate weights
  of $\pi$, and the characteristic polynomial of the crystalline Frobenius on
  the Weil–Deligne representation is that of the Satake parameters.
