+++
kind  = "theorem"
title = "The Weil representation of the real metaplectic group"
provenance = "published"
source = "Segal; Shale [shale-1962]; Weil [weil-1964]; Howe [howe-1979]"
lean  = ["GlobalTheory.Published.RealMetaplecticRepresentation", "PositivityTheory.Stage1.PM.realMetaplecticRepresentation",
         "GlobalTheory.Published.MetaplecticRepresentation", "GlobalTheory.metaplecticRepresentation_holds"]
order = 3
+++
For each $n \ge 1$ there is a two-fold covering
$\mathrm{Mp}_{2n}(\R) \to \mathrm{Sp}_{2n}(\R)$, with non-trivial kernel
element $\epsilon$, and a unitary representation $\Omega$ of
$\mathrm{Mp}_{2n}(\R)$ on $L^2(\R^n)$ such that:

* $\Omega$ is strongly continuous, preserves the Schwartz space and acts
  continuously on it;
* $\Omega(g)\rho(w)\Omega(g)^{-1} = \rho(gw)$ for the Schrödinger
  representation $\rho$ of the Heisenberg group;
* $\epsilon$ acts by $-1$;
* for the Gaussian $\varphi_0(x) = e^{-\pi x\cdot x}$,
  $\langle \Omega(g)\varphi_0, \varphi_0\rangle^2 \det(A + iB) = \langle\varphi_0,\varphi_0\rangle^2$,
  where $A + iB$ is the holomorphic part of the image of $g$, and elements
  over the maximal compact subgroup $\U(n)$ act on $\varphi_0$ by a scalar
  $c$ with $c^2\det(A+iB) = 1$;
* (infinitesimal form) $\Omega$ is smooth along smooth families in the
  group, and on one-parameter subgroups $\exp(tX)$, $X \in \mathfrak{sp}$,
  it differentiates to the quadratic differential operator attached to $X$.
