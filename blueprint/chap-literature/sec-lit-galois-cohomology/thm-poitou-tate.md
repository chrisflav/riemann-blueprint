+++
kind  = "theorem"
title = "Poitou–Tate duality"
provenance = "published"
source = "Poitou [poitou-1967]; Tate [tate-1963]"
lean  = ["GlobalTheory.Published.PoitouTateNormalised", "PositivityTheory.Lit1.PTN.poitouTateNormalised_holds"]
order = 10
+++
Let $F$ be a number field, $l$ a prime and $r \ge 1$, with $l$ odd or $F$
totally complex, and fix a primitive $l^r$-th root of unity $\zeta$. There
are local invariant isomorphisms
$\mathrm{inv}_v : H^2(G_v, \mu_{l^r}) \cong \Z/l^r$, normalised by $\zeta$,
such that for every finite set $S$ of places containing those above $l$ and
every finite $\Z/l^r$-module $M$ with a continuous action of $G_{F,S}$:

* the nine-term Poitou–Tate sequence
  $$ 0 \to H^0(G_{F,S}, M) \to \textstyle\prod_{v \in S} H^0(G_v, M) \to H^2(G_{F,S}, M^\vee(1))^\vee \to H^1(G_{F,S}, M) \to \cdots \to H^0(G_{F,S}, M^\vee(1))^\vee \to 0 $$
  is exact;
* $Ш^1(G_{F,S}, M)$ and $Ш^2(G_{F,S}, M^\vee(1))$ are dual;
* $H^n(G_{F,S}, M) = 0$ for $n \ge 3$.

The condition on $l$ and
$F$ removes the real places, where the cohomology need not vanish in high
degree.
