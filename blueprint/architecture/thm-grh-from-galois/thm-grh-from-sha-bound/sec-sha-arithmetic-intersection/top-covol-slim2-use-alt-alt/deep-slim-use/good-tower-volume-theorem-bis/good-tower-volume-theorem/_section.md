+++
id    = "good-tower-volume-theorem"
kind  = "theorem"
title = "Good towers and the volume theorem"
lean  = ["GlobalTheory.CompanionTheory.Ar.Top.goodTower_and_volume", "GlobalTheory.T.good_tower_volume_theorem"]
uses  = ["ar-calc", "semi-abelian-hom-extension"]
order = 10
+++
Let $E$ be a CM field with a unitary Shimura datum of signature $(p, q)$,
$p, q \ge 1$, with CM type $\Phi$, and let $Y$ be a global integral model of the
unitary Shimura variety over the ring of integers of its coefficient field
(one that descends and dominates the local models of
[part-i-of-semistable-reduction]) with split components. Assume the inputs
of [final-theorem-of-inputs-left], integrability of Green functions at
points, prime avoidance for multihomogeneous sections, the properties of the
Weil pairing on polarised abelian schemes, the families of Dieudonné
lattices of [model-on-hodge-from-family], and invariance of arithmetic
intersection numbers under Galois twists of the datum. Then:

1. *Good towers exist*: there is a tower $T$ of flag bundles of the Hodge
   bundles over $Y$, with line bundles indexed by $\Phi \times \{1, \dots,
   p+q\}$ (the Chern roots), and a smooth and flat realisation of it with an
   ample reference model.
2. *Volume theorem*: there is $C \ge 0$ such that, if $E$ is abelian over $\Q$,
   $p \ge 2q + 1$ and $T$ has at most $4|\Phi|(p+q)^2$ bad primes, then all
   components of $Y$ have the same volume, the arithmetic intersection
   numbers of the root line bundles are proportional to their geometric
   intersection numbers up to an error term, and for every regular weight
   $u$ the mean over components of the slopes of arithmetic volumes is at
   least $-C$ times an error built from $\log \mathrm{rd}_E$, the value of
   $L'/L$ at $1$, the number of bad primes and $u$.
