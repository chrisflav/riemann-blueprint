+++
kind  = "theorem"
title = "Tate local duality over l-adic fields"
source = "special case of Tate [tate-1963]; see Serre [serre-1994]"
lean  = ["CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate", "Formalism.GaloisCohomology.LocalTateDualityK"]
order = 1
+++
Let $K/\Q_l$ be a finite extension, $r \ge 1$, and $M$ a finite discrete
$\Z/l^r$-module with a continuous action of $G_K$. Write
$M^\vee(1) = \mathrm{Hom}(M, \mu_{l^r})$. Then
$H^2(G_K, \mu_{l^r}) \cong \Z/l^r$, and the cup product pairings
$$ H^i(G_K, M) \times H^{2-i}(G_K, M^\vee(1)) \to H^2(G_K, \mu_{l^r}) \cong \Z/l^r, \qquad i = 0, 1, 2, $$
are perfect.

It is stated for modules of $l$-power order over a field of residue
characteristic $l$.
