+++
kind  = "theorem"
title = "Galois representations of polarized cuspidal representations"
lean  = ["UpperTheory.GalS.CuspUAlt", "UpperTheory.GalS.bridgeStar_alt"]
uses  = ["thm-galois-reps-csd-above-l", "thm-zelevinsky-segments", "thm-gelfand-kazhdan"]
order = 12
+++
Let $E$ be a CM field, $l$ a prime, $\iota : \Qlbar \cong \C$, $a \ge 1$, $\pi$
a regular algebraic cuspidal automorphic representation of $\GL_a(\A_E)$ and
$\chi$ a Hecke character of $E^+$ such that $(\pi, \chi)$ is polarized. Then
there is a Galois representation $r : G_E \to \GL_a(\Qlbar)$ with the
first three properties listed in [thm-galois-reps-csd-above-l].

Like [thm-galois-reps-csd-above-l], this is a form of the existence of Galois representations
for polarized pairs, not a separate theorem. It is derived from the version
for pairs with $\pi^\vee \cong \pi^c\otimes(\chi\circ N)$ by
[thm-gelfand-kazhdan], which turns the polarization condition stated
with the inverse transpose into a statement about $\pi^\vee$. The pair
version itself is among the statements collected in
[thm-zelevinsky-segments].
