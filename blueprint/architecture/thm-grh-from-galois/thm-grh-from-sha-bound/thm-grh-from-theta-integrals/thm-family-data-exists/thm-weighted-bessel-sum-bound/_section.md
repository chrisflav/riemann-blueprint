+++
id    = "thm-weighted-bessel-sum-bound"
kind  = "theorem"
title = "Weighted bound for global Bessel sums"
lean  = ["CompanionTheory.WaveGrid.weighted_bound_rotated_uniform",
         "CompanionTheory.WaveGrid.weighted_bound_rotated_uniform_of_hypsG",
         "Formalism.MainNotions.RotatedPoints.WeightedBoundRotatedUniform"]
order = 103
+++
For all $A_w \ge 0$ and $C_h$ there are $C_b$ and $C_{g,0}$ such that for every
$C_g \ge C_{g,0}$ and every member of a family, of rank parameter $r$ with
archimedean index set $T$, the following holds. Take Bessel data at the
archimedean places whose Harish-Chandra parameters have all gaps at least
$C_g(2r+2)^4$, at levels $T_1, T_2$ and size $b$. Then the sum over the
rational points $\gamma$ of the local Bessel orbital integrals, weighted by
$\|\gamma\|^{A_w(r+1)^2}$, is at most
$$\exp\big(C_b\,(2r+2)^5\,|T|\log b\big)\cdot\|J\|^2,$$
where $\|J\|^2$ is the product of the squared $L^2$ norms of the local Bessel
transforms.

The bound is uniform in the member: the constants depend only on $A_w$ and
$C_h$.
