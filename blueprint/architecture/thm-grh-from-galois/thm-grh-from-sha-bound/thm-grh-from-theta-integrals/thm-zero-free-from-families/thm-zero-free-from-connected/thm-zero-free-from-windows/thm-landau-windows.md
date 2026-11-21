+++
kind  = "theorem"
title = "Landau's theorem on windows"
provenance = "modified"
source = "after Landau [landau-1905]"
lean  = ["Formalism.HC.Level.FormB", "Formalism.HC.Level.FormBAt", "UpperTheory.Comparison₂.formB"]
uses  = ["def-chebyshev-weighted"]
order = 1
+++
Let $\lambda > 1$ and $0 < \theta < 1$. If for arbitrarily large $Y$
$$G_m(x) \le x^\theta \quad \text{for all } x \in [Y, Y^\lambda],$$
then $L(\chi, s) \ne 0$ for every $\chi \in \langle\psi\rangle$ and every $s$
with $\Re s > \theta$.

The argument is Landau's theorem on Dirichlet series with non-negative
coefficients. The bound is assumed only on the windows $[Y, Y^\lambda]$,
not for all large $x$.
