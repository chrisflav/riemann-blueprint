+++
id    = "top-covol-slim2-use-alt-alt"
kind  = "theorem"
title = "The covolume bound"
lean  = ["SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt"]
uses  = ["ar-calc", "fargues-exact", "grothendieck-deformation", "nef-rr", "poincare-lelong-inv", "point-separation-pair-of-literature", "principalisation-char-zero", "published-hodge-bundle-theorems", "resolution-char-zero", "semi-abelian-lie-seminegative", "siegel-toroidal-integral-of-literature", "thm-grh-from-theta-integrals", "toroidal-for-fan-ks", "zarhin-statement"]
order = 14
+++
Assume:

* resolution and principalisation in characteristic zero
  ([resolution-char-zero], [principalisation-char-zero]);
* the inverse Poincaré–Lelong formula ([poincare-lelong-inv]);
* the arithmetic Hilbert–Samuel inequalities and Moriwaki's bigness
  theorem, among the results [thm-grh-from-theta-integrals] assumes;
* Fargues' exact sequence ([fargues-exact]), Zarhin's theorem
  ([zarhin-statement]) and Riemann–Roch for nef bundles ([nef-rr]);
* toroidal compactifications of Siegel moduli
  ([siegel-toroidal-integral-of-literature]) and of unitary Shimura varieties
  ([toroidal-for-fan-ks]);
* seminegativity of the Lie algebras of semi-abelian schemes
  ([semi-abelian-lie-seminegative]), separation of points
  ([point-separation-pair-of-literature]) and arithmetic degrees
  ([ar-calc]);
* the published theorems on Hodge bundles
  ([published-hodge-bundle-theorems]) and Grothendieck's deformation theorem
  ([grothendieck-deformation]).

Then the lattices of the families of [def-family-data] have bounded
covolume. That is, for every class of families satisfying the family
hypotheses there is $C_0 \ge 0$ such that for every large $x$, every member at
scale $x$ and every admissible choice of its data, the lattices $M_j$ of rank
$D$ on the indefinite side satisfy
$$\frac{2}{D\,[K:\Q]}\log \mathrm{covol}(M_j) \le \ell_j(C) \qquad \text{for all } j \text{ and all } C \ge C_0,$$
where $K$ is the field of definition and $\ell_j(C)$ is the bound that the
size parameters of the family prescribe. *We have not unfolded* the
bound $\ell_j(C)$.
