+++
kind  = "theorem"
title = "p-adic measures from CM theta functions"
lean  = ["GlobalTheory.MomFin.moments_fin", "GlobalTheory.T.unitPeriodTranslates_moments_finite"]
order = 1
+++

Consider CM data $(\mathfrak c, \delta, \chi)$ as in
[kernel-jets-level-place-integral-moments], and assume that the normalised
theta functions satisfy their equivariance law and that their Taylor
coefficients at torsion translates are algebraic. Let $p$ be an odd prime
split in $K$, prime to $N\mathfrak c$, and $\lambda : \Qbar \to \C_p$. Then
there is a $p$-adic period $\Omega$ with $|\Omega|_p = 1$ such that, for every
admissible pair of lattices and every torsion point $t$ of order prime to
$p$, there is $N_0$ prime to $p$ with the following property. For every
basis $b$ of rank $r$ there is a measure $\mu$ on $\Z_p^r$ of norm at most $1$
whose moments are the Taylor jets, normalised by $\Omega$, of the translates
of the theta function by $t$ and by good lifts $y$ of level $p^n$.

This is a form of Katz's construction of $p$-adic measures from CM theta
functions at ordinary primes (1978).
