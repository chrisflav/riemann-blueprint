+++
kind  = "theorem"
title = "Base change from unitary groups to GL(n)"
source = "after Labesse [labesse-2011]"
lean  = ["GlobalTheory.Published.BaseChangeDefiniteUnitaryGroup", "UpperTheory.BaseChangeIdentities.definiteN_of"]
uses  = ["thm-base-change-unitary"]
order = 10
+++
Let $E$ be a CM field such that $E$ is unramified over its maximal totally
real subfield $E^+$ at every finite place, and $n \ge 1$. Every automorphic
representation $\pi$ of a definite unitary group in $n$ variables over $E^+$,
split by $E$, has a base change to $\GL_n(\A_E)$: there
are a partition $n = N_1 + \dots + N_c$ with all $N_i > 0$, discrete
automorphic representations $\Pi_i$ of $\GL_{N_i}(\A_E)$ that are
conjugate self-dual, and local components $\sigma_{i,w}$ such that:

* at a place where $\pi$ is unramified, the product of the $\sigma_{i,w}$ is
  spherical, and at inert places its Satake parameter is the base change of
  that of $\pi$;
* at split places the product of the $\sigma_{i,w}$ is the local component
  of $\pi$;
* the infinitesimal characters of the $\Pi_i$ add up to the one given by the
  weight of $\pi$.

This is base change for definite unitary groups, in the form used by
[thm-base-change-unitary].
