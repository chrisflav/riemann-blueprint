+++
kind  = "theorem"
title = "Tate local duality"
provenance = "published"
source = "Tate [tate-1963]; see Serre [serre-1994]"
lean  = ["GlobalTheory.LocalDualityAll.localTateDuality", "ReciprocityTheory.Gal.LocalTateDuality",
         "CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate", "Formalism.GaloisCohomology.LocalTateDualityK"]
order = 2
+++
Let $K/\Q_l$ be a finite extension, $r \ge 1$, and $M$ a finite discrete
$\Z/l^r$-module with a continuous action of $G_K$. Write
$M^\vee(1) = \mathrm{Hom}(M, \mu_{l^r})$. Then
$H^2(G_K, \mu_{l^r}) \cong \Z/l^r$, and the cup product pairings
$$ H^i(G_K, M) \times H^{2-i}(G_K, M^\vee(1)) \to H^2(G_K, \mu_{l^r}) \cong \Z/l^r, \qquad i = 0, 1, 2, $$
are perfect.

The same holds at every finite place $v$ of a number field $F$, whether or
not $v$ lies above $l$: for the decomposition group $G_v \subset \Gal(\bar F/F)$
of a place above $v$, which is the absolute Galois group of the completion
$F_v$, one has $H^2(G_v, \mu_{l^r}) \cong \Z/l^r$ and the pairings
$H^i(G_v, M) \times H^{2-i}(G_v, M^\vee(1)) \to \Z/l^r$ are perfect.
