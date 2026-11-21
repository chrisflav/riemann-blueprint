+++
kind  = "lemma"
title = "Theta lifts of cusp forms are smooth cusp forms"
provenance = "new"
lean  = ["GlobalTheory.CuspSmoothLift.cuspidal_lift_smooth_at_of_cuspidal_lift",
         "GlobalTheory.T.cuspidal_lift_smooth_at_cusps"]
order = 1
+++
Suppose that twisted theta lifts along the grid send cusp forms to cusp
forms for the chosen test functions. Then the same holds for every Schwartz
function in the Weil representation: for every member of a family, every
grid over its real data and every Schwartz function $\Phi$, the theta
integral
$$h \mapsto \int_{\U(A)(F)\backslash \U(A)(\A_F)} \theta_\Phi(h, g)\,\varphi(g)\,dg$$
of a cusp form $\varphi$ of the given type converges absolutely and is a
smooth cusp form of the given type on $\U(B)$. This holds for the
horizontal, vertical, upward and downward arrows of the grid and for the
column lifts.
