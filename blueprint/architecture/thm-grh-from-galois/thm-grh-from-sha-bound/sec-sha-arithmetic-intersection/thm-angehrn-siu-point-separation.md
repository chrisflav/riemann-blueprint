+++
kind  = "theorem"
title = "Separation of points by adjoint linear systems"
provenance = "modified"
source = "after Angehrn–Siu [angehrn-siu-1995]"
lean  = ["GlobalTheory.Published.PointSeparationPair", "GlobalTheory.pointSeparationPair_of_principalisation", "NadelVanishingSeparation.NSI.pointSeparationPair", "UpperTheory.LiteratureTheorems.point_separation_pair_of_literature"]
order = 12
+++
Let $X$ be a normal projective variety of dimension $n$ over $\C$, $\Delta$ an
effective $\Q$-divisor with $(X, \Delta)$ klt, and $M$ a line bundle
numerically equivalent to $G/m + N_0/r$, where $G$ is a Cartier divisor with
$G \equiv m(K_X + \Delta)$ and $N_0$ is nef and big. Let $x_1 \ne x_2$ be
closed points and $c_1, \dots, c_n > 0$ with
$$c_e^e < \frac{N_0^e \cdot Z}{r^e}$$
for every subvariety $Z$ of dimension $e$ through $x_1$ or $x_2$, and
$\sum_{e=1}^n 2^{1/e} e / c_e \le 1$. Then some section of $M$ vanishes at
exactly one of $x_1, x_2$.

Angehrn and Siu prove point separation on complex manifolds; this is the
form for klt pairs.
