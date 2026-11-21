+++
kind  = "theorem"
title = "Tate local duality at the places of a number field"
lean  = ["GlobalTheory.LocalDualityAll.localTateDuality", "ReciprocityTheory.Gal.LocalTateDuality"]
order = 3
+++
Let $F$ be a number field, $v$ a finite place, $G_v \subset \Gal(\bar F/F)$
the decomposition group of a place above $v$, $r \ge 1$, and $M$ a finite
discrete $\Z/l^r$-module with a continuous action of $G_v$. Then
$H^2(G_v, \mu_{l^r}) \cong \Z/l^r$ and the cup product pairings
$H^i(G_v, M) \times H^{2-i}(G_v, M^\vee(1)) \to \Z/l^r$ are perfect, whether
or not $v$ lies above $l$.

This is Tate's local duality (1962) for decomposition groups, which are
the absolute Galois groups of the completions $F_v$.
