+++
id    = "thm-hodge-tate-weights-eigenspaces"
kind  = "theorem"
title = "Hodge–Tate weights of Hecke eigenspaces"
provenance = "new"
lean  = ["UpperTheory.Gal.Int.Geo.JumpStep", "UpperTheory.Gal.Int.Geo.jumpStep_holds"]
order = 4
+++
Let $Z$ with its correspondences be a Hecke tower over a number field $E$,
$\theta$ a system of eigenvalues, $\rho$ a continuous subquotient of $V_\theta$, and
$w \mid l$ a place where the tower has a good model as in [thm-eigenspaces-crystalline].
Let $\tau : E \to \Qlbar$ induce $w$. If some $H^b(Z_\tau, \Omega^a)$ contains a
non-zero vector on which every correspondence $g$ acts by $\theta(g)$, then $a$
is a Hodge–Tate weight of $\rho$ at $\tau$.
