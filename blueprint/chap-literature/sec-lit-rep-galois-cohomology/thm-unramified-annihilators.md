+++
kind  = "theorem"
title = "Unramified classes are exact annihilators"
source = "Tate [tate-1963]; see Milne [milne-1986]"
lean  = ["GlobalTheory.unramifiedOrthogonality_holds", "ReciprocityTheory.Gal.UnramifiedOrthogonality"]
order = 3
+++
Let $F$ be a number field, $v$ a finite place not above the prime $l$,
$G_v$ a decomposition group with inertia $I_v$, and $M$ a finite
$\Z/l^r$-module with a continuous action of $G_v$ trivial on $I_v$. Under the
local Tate pairing
$$
H^1(G_v, M) \times H^1(G_v, M^\vee(1)) \to \Z/l^r ,
$$
the unramified subgroups $H^1_{\mathrm{ur}}(G_v, M)$ and
$H^1_{\mathrm{ur}}(G_v, M^\vee(1))$ are exact annihilators of each other.
