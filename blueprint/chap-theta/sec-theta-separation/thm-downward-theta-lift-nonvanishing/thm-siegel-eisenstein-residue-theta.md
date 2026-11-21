+++
kind  = "theorem"
title = "The residue of the Siegel Eisenstein series is a theta integral"
provenance = "modified"
source = "after Kudla–Rallis [kudla-rallis-1994]; Ichino [ichino-2004]"
lean  = ["PositivityTheory.Rg.Rsw.ResCore", "PositivityTheory.Rg.Rsw.resCore"]
order = 1
+++
Let $B$ and $W$ be hermitian spaces with $\dim W + t = n$, $1 \le \dim W <
t$ and $\dim W + 2 < 2t$, and let $\psi$, $\chi$ and the archimedean data be
as in the Weil representation of $\U(n, n)$ on Schwartz functions on $B^n$
and $W^n$. For a Schwartz function $\Phi$ on $B^n$, consider the Siegel
Eisenstein series attached to $\Phi$ near $s = t/2$, with Laurent
coefficients $c_k(g)$. Then:

* $c_k = 0$ for $k \ge 2$, so the pole at $s = t/2$ is at most simple;
* for every finite measure $\kappa$ on a compact set of $\U(n,n)$, if
  $\int\theta_\Psi(g, h)\,d\kappa(g) = 0$ for all theta functions of $W$, then
  $\int c_1\,d\kappa = 0$.

So the residue lies in the closed span of theta integrals from the smaller
space $W$. This is the first term identity of the regularised Siegel–Weil
formula of Kudla and Rallis, proved by Ichino for unitary groups, in a
special form.
