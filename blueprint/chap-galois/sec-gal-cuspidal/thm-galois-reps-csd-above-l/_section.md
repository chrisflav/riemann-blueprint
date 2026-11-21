+++
id    = "thm-galois-reps-csd-above-l"
kind  = "theorem"
title = "Galois representations of conjugate self-dual representations, with compatibility above l"
provenance = "modified"
source = "after Harris–Taylor [harris-taylor-2001]; Shin [shin-2011]; Chenevier–Harris [chenevier-harris-2013]; Caraiani [caraiani-2012], [caraiani-2014]; Barnet-Lamb–Gee–Geraghty–Taylor [barnet-lamb-2012], [barnet-lamb-2014a]"
lean  = ["UpperTheory.GalS.CarUAlt", "UpperTheory.GalS.carU_of_finite_gl_recT", "UpperTheory.GalS.ofDual_star_alt"]
uses = ["def-local-parameters"]
order = 1
+++
Let $E$ be a CM field, $l$ a prime, $\iota : \Qlbar \cong \C$, $a \ge 2$, and
$\pi$ a regular algebraic cuspidal automorphic representation of
$\GL_a(\A_E)$ that is conjugate self-dual. Then there is a continuous
semisimple $r : G_E \to \GL_a(\Qlbar)$ and an integer $m$ such that:

* the Hodge–Tate weights at $\tau$ are $(a-1)/2 - z$ for $z$ in the
  infinitesimal character of $\pi$ at $\iota\tau$, and those at $\tau c$
  are $m$ minus those at $\tau$;
* at places $w \nmid l$, $r$ is compatible with the local parameters
  ([def-local-parameters]) of $\pi_w|\det|^{(1-a)/2}$ in the sense of the
  definition of Galois representations for polarized pairs;
* at places above $l$ the de Rham, Hodge–Tate and crystalline conditions of
  that definition hold;
* in addition, at every place $w \mid l$ where the local parameter of $\pi_w$
  is abelian with $N = 0$, the Weil–Deligne representation of $r|_{G_w}$
  is compatible with it.

This is the conjugate self-dual case of the existence of Galois
representations for polarized pairs, with the compatibility above $l$.
