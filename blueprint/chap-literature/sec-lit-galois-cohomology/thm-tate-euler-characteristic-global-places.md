+++
kind  = "theorem"
title = "Tate's local Euler characteristic formula"
provenance = "published"
source = "Tate [tate-1963]; see Serre [serre-1994]"
lean  = ["GlobalTheory.Laid.loceuler_holds", "ReciprocityTheory.Gal.LocalEulerChar",
         "CompanionTheory.LocalTateOrthogonality.Gcoh.top_euler", "Formalism.GaloisCohomology.LocalEulerCharK"]
order = 3
+++
Let $K/\Q_l$ be a finite extension, $r \ge 1$, and $M$ a finite discrete
$\Z/l^r$-module with a continuous action of $G_K$. Then
$$ \# H^1(G_K, M) = \# H^0(G_K, M)\cdot \# H^2(G_K, M)\cdot (\# M)^{[K:\Q_l]}. $$

At the places of a number field: let $F$ be a number field, $v$ a finite
place with decomposition group $G_v$, and $M$ a finite discrete
$\Z/l^r$-module with a continuous action of $G_v$. Then
$$ \# H^1(G_v, M) = \# H^0(G_v, M)\cdot \# H^2(G_v, M)\cdot (\# M)^{[F_v:\Q_l]} $$
if $v$ lies above $l$, and $\# H^1 = \# H^0 \cdot \# H^2$ otherwise.
