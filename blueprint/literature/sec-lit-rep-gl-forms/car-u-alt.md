+++
kind  = "theorem"
title = "Galois representations of conjugate self-dual representations, with compatibility above l"
lean  = ["GlobalTheory.CompanionTheory.CuspFinGL.cuspFormsBoundedGL", "PositivityTheory.PRW.GKD.gelfandKazhdanDual_of_multiplicityOne", "UpperTheory.GalS.CarUAlt", "UpperTheory.GalS.carU_of_finite_gl_recT", "UpperTheory.GalS.ofDual_star_alt"]
uses  = ["automorphic-forms-finite-gl", "cusp-forms-bounded-gl", "cuspidal-multiplicity-one", "def-local-parameters", "gelfand-kazhdan-dual", "jacquet-shalika-rigidity"]
order = 11
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

This is not a separate theorem of the literature: it is the conjugate
self-dual case of the statement that polarized pairs have Galois
representations (Harris–Taylor, Shin, Chenevier–Harris, Caraiani), with the
compatibility above $l$ of Caraiani and of Barnet-Lamb–Gee–Geraghty–Taylor.
It is derived from that statement: a conjugate self-dual $\pi$ forms a
polarized pair with $\chi = \eta^a$, $\eta$ the quadratic character of
$E/E^+$, once one knows $\pi^\vee \cong \pi\circ\theta$
([gelfand-kazhdan-dual]), which uses strong multiplicity one
([jacquet-shalika-rigidity]), multiplicity one
([cuspidal-multiplicity-one]) and boundedness of cusp forms
([cusp-forms-bounded-gl]). One step of the deduction takes the finiteness theorem
[automorphic-forms-finite-gl] and the existence of local parameters as
hypotheses and does not use them.
