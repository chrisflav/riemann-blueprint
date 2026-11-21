+++
id    = "thm-sha-bound"
kind  = "theorem"
title = "The Tate–Shafarevich bound"
provenance = "new"
lean  = ["UpperTheory.One.vwin_of_row", "UpperTheory.One.Join.automorphic_window_of_inputs",
         "UpperTheory.LiteratureTheorems.OpenImageCondition",
         "UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt"]
uses  = ["def-sha-bound"]
order = 1
+++
For every primitive Dirichlet character $\psi$ the Tate–Shafarevich bound
([def-sha-bound]) holds with exponent $401$. That is, for every
$\varepsilon < 1/52$ there are $J$ and $X_0$ such that for every $X \ge X_0$
and every auxiliary pair at scale $X^{1/J}$ there is
$Y \in [X^{1/J}, X^{1/2}]$ with the following property: for every
$x \in [Y, Y^2]$, every $\psi$-field $E$ and $t = \lfloor x^{401}\rfloor$,
the groups $Ш^1_l(E, e) = Ш^1\big(G_{E,S}, \Q_l/\Z_l(-e)\big)$, $0 < e < t$,
are finite, and
$$\sum_{l \in \Sigma}\log l\sum_{e=1}^{t-1}\mathrm{len}\,Ш^1_l(E, e) \le e^{x^\varepsilon/2}$$
for every finite set of primes $\Sigma$.
