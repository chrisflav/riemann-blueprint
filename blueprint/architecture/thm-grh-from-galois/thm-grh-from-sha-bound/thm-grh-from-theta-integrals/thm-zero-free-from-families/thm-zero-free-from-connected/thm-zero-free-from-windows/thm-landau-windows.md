+++
kind  = "theorem"
title = "Landau's theorem on windows"
lean  = ["Formalism.HC.Level.FormB", "Formalism.HC.Level.FormBAt", "UpperTheory.Comparison₂.formB"]
uses  = ["def-chebyshev-weighted"]
order = 1
+++
Let $\lambda > 1$ and $0 < \theta < 1$. If for arbitrarily large $Y$
$$G_m(x) \le x^\theta \quad \text{for all } x \in [Y, Y^\lambda],$$
then $L(\chi, s) \ne 0$ for every $\chi \in \langle\psi\rangle$ and every $s$
with $\Re s > \theta$.
