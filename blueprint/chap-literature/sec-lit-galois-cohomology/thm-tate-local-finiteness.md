+++
kind  = "theorem"
title = "Finiteness of local Galois cohomology"
provenance = "published"
source = "Tate [tate-1963]"
lean  = ["GlobalTheory.Laid.locfin_holds", "ReciprocityTheory.Gal.LocalFiniteness",
         "CompanionTheory.LocalTateOrthogonality.Gcoh.top_locfin", "Formalism.GaloisCohomology.LocalFinitenessK"]
order = 1
+++
Let $F$ be a number field, $v$ a finite place, $G_v \subseteq \Gal(\bar F/F)$
a decomposition group at $v$, $l$ a prime, $r > 0$, and $M$ a finite
$\Z/l^r$-module with a continuous action of $G_v$. Then $H^0$, $H^1$ and $H^2$
of $G_v$ with coefficients in $M$ are finite, and $H^n = 0$ for $n \ge 3$.
The place $v$ may lie above $l$.

The same holds for the absolute Galois group of a finite extension $K$ of
$\Q_l$ inside $\Qlbar$ and a finite $\Z/l^r$-module with a continuous
action of $G_K$.
