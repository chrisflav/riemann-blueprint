+++
kind = "proof"
of   = "thm-member-gap-bound"
uses = ["thm-chowla-selberg"]
+++
The slope data bound the same slope $\mu_{CC}(u)$ from both sides.

*From above*, the divisibility condition gives
$$\mu_{CC} + h - F \le \sum_{t \in T}\Big(m\,\big(a_t\log a_t - a_t - a_t\log\Omega\big) - a_t\log T_u\Big) + E_{\mathrm{div}},$$
where $h$ and $F$ are height terms, $T_u$ is the level, and
$\log\Omega = \gamma + \log(\pi/v) - \frac{L'}{L}(1,\chi_K)$ is the mean
logarithm of the periods that the Chowla–Selberg formula gives
([thm-chowla-selberg]).

*From below*, the slope inequality bounds $\mu_{CC}$ by the weighted mean of
the slopes $\mu_N - h$, less $\log|W|$ and a correction of the order of the
heights. The quotient slope bounds give
$\mu_N \ge \mu_M + \beta + F - R - L_o$, where the gain $\beta(u)$ differs from
the von Mangoldt sum $\sum_t\sum_j S(a_t, t, w_{u,j})$ by at most the loss
bound, and $R(u) = m\log(g_0g_1)\sum_t a_t + O(mB_0)$ with the auxiliary
primes $g_0, g_1$.

The counting condition bounds $\log T_u$ below by
$\sum_j |\Phi|^{-1}\sum_\rho \log(w_{u,j}(\rho)\,v/\pi) + m\log(g_0g_1)$, less an
error. Put together, the terms in $\log(\pi/v)$ and in $\log(g_0g_1)$ cancel,
and what remains is $\sum_t\sum_j S \le \sum_t\sum_j M$ plus the listed errors.
A last computation bounds those errors by $x^{(e_D+e_L+3)\varepsilon}$ times
the bracket.

*We read* this as the arithmetic form of Stepanov's method that the
announcement describes: the factor $m$ in the divisibility bound, one for
each step of the chain, plays the part of the multiplicity of the
auxiliary function, and the slope inequality plays the part of the degree
bound.
