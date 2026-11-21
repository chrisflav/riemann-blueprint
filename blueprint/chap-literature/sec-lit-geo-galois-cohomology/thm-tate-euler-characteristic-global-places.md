+++
kind  = "theorem"
title = "Tate's local Euler characteristic formula at the places of a number field"
provenance = "published"
source = "Tate [tate-1963]"
lean  = ["GlobalTheory.Laid.loceuler_holds", "ReciprocityTheory.Gal.LocalEulerChar"]
order = 4
+++
Let $F$ be a number field, $v$ a finite place with decomposition group $G_v$,
$r \ge 1$, and $M$ a finite discrete $\Z/l^r$-module with a continuous
action of $G_v$. Then
$$ \# H^1(G_v, M) = \# H^0(G_v, M)\cdot \# H^2(G_v, M)\cdot (\# M)^{[F_v:\Q_l]} $$
if $v$ lies above $l$, and $\# H^1 = \# H^0 \cdot \# H^2$ otherwise.
