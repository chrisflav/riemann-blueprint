+++
kind  = "theorem"
title = "The geometric lemma"
provenance = "published"
source = "Bernstein–Zelevinsky [bernstein-zelevinsky-1977]"
lean  = ["GlobalTheory.CompanionTheory.GeoLink.geometricLemma", "GlobalTheory.Published.GeometricLemma",
         "PositivityTheory.Exh.geometricLemmaGL",
         "UpperTheory.V.Z.Win.Extra.geo"]
order = 5
+++
Let $F$ be a non-archimedean local field. The geometric lemma holds for
$\GL_n(F)$ in two forms:

* the filtration of [thm-geometric-lemma-filtration];
* its consequence in the Grothendieck group: if $\rho_i$ are smooth
  representations of finite length of $\GL_{m_i}(F)$, then the
  Jordan–Hölder multiplicity of each irreducible $\tau$ in the cell
  $\mathcal F_b(\rho_1 \otimes \dots \otimes \rho_r)$ equals
  $$
  \sum_s \Big(\prod_i \operatorname{mult}\big(\textstyle\bigotimes_j s_{ij},\, r_{b,i}(\rho_i)\big)\Big)\,
  \operatorname{mult}\big(\tau,\, \textstyle\bigotimes_j \prod_i s_{ij}\big),
  $$
  a finite sum over families $s_{ij}$ of irreducible representations,
  where $r_{b,i}$ is the Jacquet module of type given by row $i$ of $b$.
