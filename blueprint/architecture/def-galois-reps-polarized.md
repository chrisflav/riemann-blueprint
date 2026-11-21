+++
kind  = "definition"
title = "Galois representations of polarized representations"
provenance = "modified"
lean  = ["UpperTheory.GalStar.Row0b", "UpperTheory.One.M.Row", "UpperTheory.GalStar.Row0"]
uses  = ["def-local-parameters"]
order = 2
+++
Let $E$ be a CM field, $l$ a prime and $\iota : \Qlbar \cong \C$. A
*polarized pair* $(\pi, \chi)$ on $\GL_a(\A_E)$ is a regular algebraic
cuspidal representation $\pi$ and a character $\chi$ with
$\pi^\vee \cong \pi^c \otimes (\chi \circ N)$ and $\chi_v(-1) = (-1)^a$ at the
real places.

We say that *polarized pairs have Galois representations* if every such
pair has a semisimple $r : G_E \to \GL_a(\Qlbar)$ with:

* Hodge–Tate weights $(a-1)/2 - z$ at each embedding $\tau$, read off the
  infinitesimal character of $\pi$, and the dual weights at $\tau c$;
* at a place $w \nmid l$: $\mathrm{WD}(r|_{G_w})$ has the dimension of the
  local parameter ([def-local-parameters]) of $\pi_w|\det|^{(1-a)/2}$, and
  is isomorphic to it when the parameter is abelian with $N = 0$. In the
  tamely ramified square-free case the monodromy vanishes and the
  characteristic polynomials of Frobenius agree;
* at a place $w \mid l$: $r$ is crystalline with the right weights when
  $\pi_w$ is unramified, and potentially semistable with the right
  Weil–Deligne representation in the tame or abelian case.

This is the theorem of Harris–Taylor, Shin, Chenevier–Harris,
Barnet-Lamb–Gee–Geraghty–Taylor and Caraiani, with local–global
compatibility weakened as stated.
