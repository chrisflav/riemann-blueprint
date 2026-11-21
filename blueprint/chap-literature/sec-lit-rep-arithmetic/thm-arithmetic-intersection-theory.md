+++
kind  = "theorem"
title = "Arithmetic intersection theory of hermitian line bundles"
source = "Gillet–Soulé [gillet-soule-1990]; Bost–Gillet–Soulé [bost-1994]"
lean  = ["GlobalTheory.ArithmeticHeightTower.ArakelovDirectHeights.arCalc_direct", "GlobalTheory.ArithmeticHeightTower.ArakelovDirectHeights.cycleHeights_direct", "GlobalTheory.CompanionTheory.Ar.Pub.PoincareLelong", "GlobalTheory.Published.ArCalc", "GlobalTheory.Published.ArDegree", "GlobalTheory.Published.ChernDegreeComplex", "GlobalTheory.Published.CycleHeights", "GlobalTheory.Published.CycleHeights.heightProjection", "PositivityTheory.Prw.arDegree_of", "PositivityTheory.ResPlug.FromRes.resK", "PositivityTheory.Tls2.Chern2.chernDegreeComplex", "PositivityTheory.Tls2.Pl.poincareLelong", "ReciprocityTheory.ChartRestriction.G.Geo.ResK.ResKStatement"]
order = 4
+++
Let $X$ be an arithmetic variety of relative dimension $D$ over $\operatorname{Spec} k$
(a ring with complex embeddings $\sigma$) and consider hermitian line
bundles $\bar L$ on $X$. Then:

* heights of points with respect to $\bar L$ exist, and arithmetic
  intersection numbers $\widehat{\deg}(\bar L_0\cdots\bar L_D)$ and the
  geometric degrees on the generic fibre exist and are multilinear;
* changing the metric by $e^{-u}$ changes the intersection number by
  $\tfrac12\int u\,c_1(\bar L_1)\cdots c_1(\bar L_D)$;
* scaling the metric by a constant $e^{-t}$ adds $(D+1)\,t\,\deg L$ to the
  self-intersection;
* the inductive formula: for a rational section $s$ of $L_0$,
  $\widehat{\deg}(\bar L_0\cdots\bar L_D)$ is the height of $\operatorname{div}(s)$
  minus the archimedean integral $\int\log\|s\|\,c_1\cdots c_1$;
* the projection formula for generically finite maps, with the degree as
  factor, and invariance under isometries.

We also record here
the Chern–Weil identity on complex varieties, the Poincaré–Lelong formula,
birational invariance, the projection formula for cycle heights, and
resolution of singularities in characteristic zero.
