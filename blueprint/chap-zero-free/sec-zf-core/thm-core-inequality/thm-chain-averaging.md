+++
kind  = "theorem"
title = "Averaging over a chain of length about the square root of x"
provenance = "new"
lean  = ["Deduction.ch_core", "Formalism.LFunctionChainParameters.LChain.RestSize"]
uses  = ["def-chebyshev-weighted", "def-slope-data", "def-auxiliary-field-data", "def-family-scale"]
order = 1
+++
Let $E$ be an auxiliary CM field at scale $x$
([def-auxiliary-field-data]), with Galois group $\Gamma = \{\pm1\}^2\times A$,
$n = |A|$, CM type $\Phi$ and complex conjugation $c$, and let $A_0 \subset A$
be a subgroup. For $a > 0$, $t \in A$ and a weight $w : \Gamma \to \R_{>0}$ put
$$S(a, t, w) = \sum_{p:\ \mathrm{Frob}_p \notin \Phi} 2\log p
\sum_{i \ge 1,\ i\,\mathrm{Frob}_p \notin \Phi} \Big(\frac{a}{p^i} - w(c + i\,\mathrm{Frob}_p + t)\Big)_+
\ +\ (\text{a similar term at the ramified prime } d),$$
$$M(a, w) = a\Big(\log a - 1 - \gamma + \frac{L'}{L}(1, \chi_K)
- \frac{1}{|\Phi|}\sum_{\rho \in \Phi}\log w(\rho)\Big),$$
where $\chi_K$ is the quadratic character of $K = \Q(\sqrt{-d})$. Take an
integer $m \ge 1$, a set $T \subset A$ of twists with scales $a_t$,
$|a_t/b - x| \le 1$, a set $T_2 \subset A_0$ of thick elements, and weights
$w_{u,j}$ for $u \in A_0$ and $0 \le j < m$. Call
$$\Delta(u) = \sum_{t \in T}\sum_{j < m}\big(S(a_t, t, w_{u,j}) - M(a_t, w_{u,j})\big)$$
the *gap* at $u$. Suppose that the size conditions of the slope data hold
([def-slope-data]), among them
$$x^{1/2 - \varepsilon} \le m \le x^{1/2 + \varepsilon/2}, \qquad xm \le k \le n^2 x^{1/2-\varepsilon},
\qquad a \le 2xb$$
(in the families $a = xb$, [def-family-scale]), and that for every $u \in A_0$
$$\Delta(u) \le x^{C\varepsilon}\Big(|T|\,a\Big(1 + \frac{m^2}{k}\Big)
+ m\Big(2nmb\,x^{\varepsilon} + \frac{|T_2|\,k\,b\,x^{2\varepsilon}}{n^2}\Big)\Big).$$
Then the weighted sum $G_m$ of [def-chebyshev-weighted], formed with the
characters of $\Gamma$ that correspond to $\langle\psi\rangle$, satisfies
$$G_m(x) \le x^{1/2 + (C+3)\varepsilon} + \sum_{\xi}|g_\xi(x)|,$$
where $\xi$ runs over the other characters of $\Gamma$ trivial on $A_0$, and
$g_\xi$ is the sum $g_\chi$ of [def-chebyshev-weighted] for the character
$\chi$ of $E$ attached to $\xi$.

Each of the $m|T|$ terms of $\Delta(u)$ is a von Mangoldt sum of length about
$a_t/w \approx x$, scaled by $w \approx b$. Divided by $m|T|b$, the allowed
error is about $2x/m + 2mn\,x^{\varepsilon}/|T|$: the first term falls as the
chain grows, the second rises, and they balance when $m$ is about $x^{1/2}$.
This is the square root of the announcement [alpoge-2026]: the chain of
theta lifts has length about $\sqrt x$.
