+++
id    = "thm-covolume-bound"
kind  = "theorem"
title = "The covolume bound"
lean  = ["SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt"]
uses  = ["thm-arithmetic-intersection-theory", "thm-fargues-hodge-tate-sequence", "thm-grothendieck-messing", "thm-hilbert-samuel-nef", "thm-poincare-lelong-integrated", "thm-angehrn-siu-point-separation", "thm-principalisation-relative", "def-hodge-bundle-inputs", "thm-hironaka-resolution", "thm-hodge-bundle-semipositive", "thm-toroidal-compactification-siegel", "thm-grh-from-theta-integrals", "thm-toroidal-compactification-unitary", "thm-zarhin-trick"]
order = 14
+++
Assume:

* resolution and principalisation in characteristic zero
  ([thm-hironaka-resolution], [thm-principalisation-relative]);
* the inverse Poincaré–Lelong formula ([thm-poincare-lelong-integrated]);
* the arithmetic Hilbert–Samuel inequalities and Moriwaki's bigness
  theorem, among the results [thm-grh-from-theta-integrals] assumes;
* Fargues' exact sequence ([thm-fargues-hodge-tate-sequence]), Zarhin's theorem
  ([thm-zarhin-trick]) and Riemann–Roch for nef bundles ([thm-hilbert-samuel-nef]);
* toroidal compactifications of Siegel moduli
  ([thm-toroidal-compactification-siegel]) and of unitary Shimura varieties
  ([thm-toroidal-compactification-unitary]);
* seminegativity of the Lie algebras of semi-abelian schemes
  ([thm-hodge-bundle-semipositive]), separation of points
  ([thm-angehrn-siu-point-separation]) and arithmetic degrees
  ([thm-arithmetic-intersection-theory]);
* the published theorems on Hodge bundles
  ([def-hodge-bundle-inputs]) and Grothendieck's deformation theorem
  ([thm-grothendieck-messing]).

Then the lattices of the families of [def-family-data] have bounded
covolume. That is, for every class of families satisfying the family
hypotheses there is $C_0 \ge 0$ such that for every large $x$, every member at
scale $x$ and every admissible choice of its data, the lattices $M_j$ of rank
$D$ on the indefinite side satisfy
$$\frac{2}{D\,[K:\Q]}\log \mathrm{covol}(M_j) \le \ell_j(C) \qquad \text{for all } j \text{ and all } C \ge C_0,$$
where $K$ is the field of definition and $\ell_j(C)$ is the bound that the
size parameters of the family prescribe. *We have not unfolded* the
bound $\ell_j(C)$.
