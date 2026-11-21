+++
kind  = "definition"
title = "The Tate–Shafarevich bound"
provenance = "new"
lean  = ["UpperTheory.Top.VWin", "UpperTheory.Top.VWinAt", "UpperTheory.Top.VVle",
         "UpperTheory.Top.IsChiField", "UpperTheory.Top.WinPair", "UpperTheory.Top.PageN",
         "Formalism.GaloisCohomology.Sha", "Formalism.GaloisCohomology.shaLen"]
order = 4
+++
For a number field $E$, a prime $l$ and an integer $e$, let
$$Ш^1_l(E, e) = Ш^1\big(G_{E,S},\ \Q_l/\Z_l(-e)\big),$$
with $S$ the places above $l$ and the twist taken with a fixed extension
of the cyclotomic character. Write $\mathrm{len}$ for length as a
$\Z_l$-module.

Fix a primitive Dirichlet character $\psi$. An *auxiliary pair* at scale $Y$
is a pair of primes $q \equiv 3 \bmod 8$ and $d \equiv 7 \bmod 16$ with
$\log q \asymp Y^{\varepsilon/5}$ and $\log d \asymp Y^{\varepsilon/5}\log^2 Y$,
such that $q$ and every odd prime $p \le Y^{\varepsilon/5}$ divide $d + 1$.
For such a pair and $2^e \asymp x^{2+8\varepsilon}$, the *$\psi$-fields* are
the subfields $E$ of a cyclotomic field fixed by
$$\{a \equiv \pm 1 \bmod 2^{e+2},\ \psi(a) = 1,\ (a/q) = (a/d) = 1\}.$$

The *Tate–Shafarevich bound* with exponent $C$ is the following statement.
For every $\varepsilon < 1/52$ there are $J$ and $X_0$ such that for every
$X \ge X_0$ and every auxiliary pair at scale $X^{1/J}$ there is
$Y \in [X^{1/J}, X^{1/2}]$ with this property: for every $x \in [Y, Y^2]$,
every $\psi$-field $E$ and $t = \lfloor x^C \rfloor$, the groups
$Ш^1_l(E, e)$, $0 < e < t$, are finite, and
$$\sum_{l \in \Sigma}\log l\sum_{e=1}^{t-1}\mathrm{len}\,Ш^1_l(E, e) \le e^{x^\varepsilon/2}$$
for every finite set of primes $\Sigma$. The proof uses $C = 401$ for every
primitive $\psi$.
