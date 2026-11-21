+++
kind  = "theorem"
title = "Galois representations compatible at unramified places"
provenance = "new"
lean  = ["UpperTheory.Gal.Int.coreAll_of"]
uses  = ["thm-theta-lift-nonvanishing"]
order = 10
+++
Assume the seed and congruence statements of steps 1 and 2 in the proof of
[thm-galois-reps-from-geometry-and-theta] for definite unitary groups of
odd rank, and that theta lifts do not vanish
([thm-theta-lift-nonvanishing]). Let $E$ be a CM field, $a \ge 1$, and $(\pi, \chi)$
a polarized regular algebraic cuspidal pair on $\GL_a(\A_E)$. Then there is a
continuous $r : G_E \to \GL_a(\Qlbar)$ attached to $\pi$ at almost all places, and
every such $r$ satisfies, at every place $w$ where $\pi_w$ is unramified with
Satake parameters $B$:

* if $w \nmid l$, $\iota\,\mathrm{charpoly}\, r(\mathrm{Frob}_w^{-1})$ has the roots $q_w^{(a-1)/2}B$;
* if $w \mid l$, $r$ is de Rham and crystalline at $w$ with the Hodge–Tate weights
  of $\pi$, and the characteristic polynomial of the crystalline Frobenius on
  the Weil–Deligne representation is that of the Satake parameters.
