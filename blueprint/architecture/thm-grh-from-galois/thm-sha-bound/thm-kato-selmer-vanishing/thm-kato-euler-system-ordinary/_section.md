+++
id    = "thm-kato-euler-system-ordinary"
kind  = "theorem"
title = "Kato's Euler system for ordinary newforms"
provenance = "modified"
source = "after Kato [kato-2004]"
lean  = ["GlobalTheory.Ord2.ZetaUr", "UpperTheory.V.Z.Kato.Final.zetaUr",
         "UpperTheory.V.Z.Kato.Joint.kato_global_unit_law_of_smoothed_classes"]
order = 10
+++
Let $l$ be an odd prime, $e \ge 1$, $S$ a finite set of primes containing
$l$, and $W : G_\Q \to \GL_2(\Qlbar)$ continuous, with entries in the ring
of integers $\mathcal O$ of a finite extension of $\Q_l$, unramified outside
$S$, with $\det W$ quadratic and odd, and irreducible on the kernel of
$\epsilon$ and $\det W$. Suppose that on a decomposition group $D_l$ at $l$
the representation is upper triangular, its first diagonal entry is a power
of $\epsilon^e$ on inertia up to finite order and is not $\epsilon$ on all
of $D_l$. Let $g$ be a newform of weight $2e+1$ and level prime to $l$,
ordinary at $l$, such that $W \otimes \epsilon^{-e}\det W^{-1}\chi$ is
attached to $g$ for a character $\chi$ of order dividing $l$.

Then $W$ has an *Euler system*: a class $y \in H^1(\Q, W)$ with integral
values, unramified away from $l$ and not in the ordinary local condition at
$l$, and for each $n \ge 1$ and almost every prime $w \equiv 1 \bmod l^n$,
with $\psi$ a surjective character of conductor $w$ and order $l^n$, a
*derivative*: an integral cochain $Y$ on $G_\Q$ with values in functions on
$\Z/l^n$, twisted by $\psi$, unramified away from $w$, with
$$\sum_x Y(s, x) = P\,y(s) + (W(s) - 1)b,\qquad P \equiv u\det\big(W(\mathrm{Frob}_w) - 1\big) \bmod l^n$$
for a unit $u$.

This is Kato's Euler system in the form Kolyvagin's method needs.
