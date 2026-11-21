+++
kind  = "theorem"
title = "Tate's local Euler characteristic formula over l-adic fields"
provenance = "modified"
source = "special case of Tate [tate-1963]; see Serre [serre-1994]"
lean  = ["CompanionTheory.LocalTateOrthogonality.Gcoh.top_euler", "Formalism.GaloisCohomology.LocalEulerCharK"]
order = 2
+++
Let $K/\Q_l$ be a finite extension, $r \ge 1$, and $M$ a finite discrete
$\Z/l^r$-module with a continuous action of $G_K$. Then
$$ \# H^1(G_K, M) = \# H^0(G_K, M)\cdot \# H^2(G_K, M)\cdot (\# M)^{[K:\Q_l]}. $$

It is stated for modules of $l$-power order over a field of residue
characteristic $l$.
