+++
kind  = "theorem"
title = "The Weil representation of the real metaplectic group"
source = "Segal; Shale [shale-1962]; Weil [weil-1964]"
lean  = ["GlobalTheory.Published.MetaplecticRepresentation", "GlobalTheory.metaplecticRepresentation_holds"]
order = 2
+++
For each $n$ there is a two-fold covering $\mathrm{Mp}_{2n}(\R) \to \mathrm{Sp}_{2n}(\R)$
and a unitary representation $\Omega$ of $\mathrm{Mp}_{2n}(\R)$ on
$L^2(\R^n)$ such that:

* $\Omega$ is strongly continuous, preserves the Schwartz space and acts
  continuously on it;
* $\Omega(g)\rho(w)\Omega(g)^{-1} = \rho(gw)$ for the Schrödinger
  representation $\rho$ of the Heisenberg group;
* the non-trivial element of the kernel acts by $-1$;
* for the Gaussian $\varphi_0(x) = e^{-\pi x\cdot x}$,
  $\langle \Omega(g)\varphi_0, \varphi_0\rangle^2 \det(A + iB) = \langle\varphi_0,\varphi_0\rangle^2$,
  where $A + iB$ is the holomorphic part of the image of $g$, and elements
  over the maximal compact subgroup $\U(n)$ act on $\varphi_0$ by a scalar
  $c$ with $c^2\det(A+iB) = 1$.
