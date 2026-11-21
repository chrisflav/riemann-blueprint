+++
kind  = "theorem"
title = "Kummer classes of Siegel units under diamond operators"
provenance = "new"
lean  = ["UpperTheory.Kd.L.law", "UpperTheory.Kd.L.thcocd", "UpperTheory.Kd.L.thdiam", "UpperTheory.Kd.L.twist"]
order = 1
+++
Let $\mathcal F$ be the field of modular functions of all levels over
$\Qbar$, $l$ an odd prime, $N$ prime to $l$, and $c, d > 1$ prime to $6lN$.
Let $\gamma_r \in \mathrm{SL}_2(\Z)$, $r \in (\Z/l)^\times$, have bottom row
congruent to a multiple of $(r, -1)$ modulo $l$ and lower left entry
divisible by $N$. Then there are $c_1$ and $\kappa_0 \ne 0$ with the
following property. Let $1 \le m \le n$, and let $b$ be a cochain on
$G_\Q$ that lifts, modulo $l^n$, the Kummer classes of the Siegel units
$g_{c,d}$ translated by the $\gamma_r$, twisted to weight $2e - 1$. Then for
every unit $y \bmod l^m$ and $\delta \in (\Z/N)^\times$ there is a
$q$-expansion $g$ with integral coefficients such that, for every $s$ in
inertia at $l$ fixing $\mu_{l^m}$ and every coefficient $i$,
$$l^{c_1}\,\Theta\big(\langle\delta\rangle b\big)(s)_i \equiv l^{c_1}\Big(l^{c_0}\kappa_0\,t(s)\,l^m\,a_i\big(E_{m,x\delta^{-1}}\big) + s(g_i) - g_i\Big) \bmod l^n,$$
where $\Theta$ is the map from Kummer classes to $q$-expansions,
$t(s) \in \Z/l^n$ records the action of $s$ on $\mu_{l^{m+2n}}$, and $a_i$ is
the $i$-th coefficient.

*We read* $\Theta$ as the logarithmic derivative on $q$-expansions, so that
this is the classical fact that $\mathrm{dlog}$ of a Siegel unit is an
Eisenstein series, in an $l$-adic and twisted form.
