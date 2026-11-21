+++
id    = "lem-height-lower-bound-deep-covers"
kind  = "lemma"
title = "Height lower bound on deep covers"
provenance = "new"
lean  = ["SelfIntersectionVolumeEstimates.height_lower_bound_general_alt"]
uses  = ["thm-mean-arithmetic-volume-lower-bound"]
order = 11
+++
Suppose that the mean arithmetic volumes satisfy the lower bound of
[thm-mean-arithmetic-volume-lower-bound], that deep covers are good, and that
the size, cover-degree and flat-degree conditions hold. Then the heights on
deep covers are bounded below: for every class of families satisfying the
family hypotheses there is $C$ such that eventually, for every member, every
good deep cover $Y$ and every quotient weight $u_1$, there are
$c_s, c_c, X \ge 0$ and slopes $s_Z$ on the components with
$$h_{u_1}(Z) + c_s \ge 0, \qquad (1 - \rho(u_1))\max(0, s_Z + c_s) \le h_{u_1}(Z) + c_s + c_c,$$
$$\frac{1}{\#\pi_0}\sum_Z s_Z \ge -X,$$
and $X$, $c_c$ and $c_s$ times explicit dimensions are at most $C$ times the
unit error of the member, divided by the length of the tower.
