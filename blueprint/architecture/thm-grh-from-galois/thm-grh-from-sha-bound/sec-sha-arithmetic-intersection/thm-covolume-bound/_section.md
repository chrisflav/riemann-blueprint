+++
id    = "thm-covolume-bound"
kind  = "theorem"
title = "The covolume bound"
provenance = "new"
lean  = ["SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt", "SelfIntersectionVolumeEstimates.topCovolG_alt_alt",
         "GlobalTheory.CovTop.PublishedHodgeBundleTheorems.toClassicalTheorems", "GlobalTheory.Proportionality.mumfordProportionality_of_goodChernWeil",
         "GlobalTheory.T.toroidalFlagProportionality_of_goodChernWeil"]
uses  = ["def-family-data"]
order = 14
+++
The lattices of the families of [def-family-data] have bounded covolume.
That is, for every class of families satisfying the family hypotheses there
is $C_0 \ge 0$ such that for every large $x$, every member at scale $x$ and
every admissible choice of its data, the lattices $M_j$ of rank $D$ on the
indefinite side satisfy
$$\frac{2}{D\,[K:\Q]}\log \mathrm{covol}(M_j) \le \ell_j(C) \qquad \text{for all } j \text{ and all } C \ge C_0,$$
where $K$ is the field of definition and $\ell_j(C)$ is the bound that the
size parameters of the family prescribe. *We have not unfolded* the
bound $\ell_j(C)$.
