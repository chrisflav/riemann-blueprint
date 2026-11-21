+++
id    = "thm-hecke-fixed-points-kuga-sato"
kind  = "theorem"
title = "Fixed points of Hecke correspondences on Kuga–Sato varieties"
provenance = "new"
lean  = ["UpperTheory.Gal.FixZ.FixK_holds", "UpperTheory.Gal.FixZ.tower_fixed_points_of_isogeny_data",
         "UpperTheory.Gal.LocalSmoothExtension.FixK"]
order = 1
+++
Let $G$ be as in [thm-kuga-sato-unitary-shimura], over $\C$, with levels
$N \mid N'$, and let $h \in G(\A_f)$ be such that the Hecke operator of $h$ is
supported on regular elements. Compose the Hecke correspondence of $h$ on the
$k$-th Kuga–Sato variety with translation by sections $\alpha_1, \dots, \alpha_k$
of $\mathcal O_F$, all non-zero and divisible by $2$. Then this correspondence and
the natural projection are finite étale, they have finitely many coincidence
points $x$, at each of which $1 - A_x$ is invertible on the tangent space, and for
every $y \in \C$
$$\sum_x \mathrm{Lef}(A_x, y) = [K_{N'} : K_{N'} \cap hK_Nh^{-1}] \cdot O(y),$$
where $\mathrm{Lef}$ is the fixed-point term of the holomorphic Lefschetz formula
and $O(y)$ is a weighted sum of orbital integrals of the Hecke function of $h$
over elliptic elements of $G$, with weights from the characters of $\lambda$ and
the $\alpha_s$.
