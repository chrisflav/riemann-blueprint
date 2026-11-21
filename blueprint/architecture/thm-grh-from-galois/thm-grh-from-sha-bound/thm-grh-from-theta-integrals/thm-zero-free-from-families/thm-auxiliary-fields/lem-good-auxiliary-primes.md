+++
kind  = "lemma"
title = "Most auxiliary primes are good"
provenance = "new"
lean  = ["QH.pair_share", "QH.pair_exists"]
uses  = ["def-chebyshev-weighted"]
order = 1
+++
There is $C > 0$ such that for all $0 < \varepsilon < 1/52$, $\tau > 0$,
$K \ge 1$, $\eta > 0$, $N_0 \ge 1$ and all large $Y$ the following holds. Put
$z = Y^{\varepsilon/5}$, and let $X \le Y^K$ and
$z\log^2 Y \le z' \le K^2 z\log^2 Y$.

Call a primitive Dirichlet character $\chi$ *good* if $\chi \ne 1$, its
conductor is at most $Q$, $L(s,\chi) \ne 0$ for $\Re s > 1 - 1/400$ and
$|\Im s| \le Q$, $|L'/L(1,\chi)| \le C\log Y$, and
$$|g_\chi(y)| \le y^{1/2+\tau} \qquad (Y \le y \le X)$$
for the sum $g_\chi$ of [def-chebyshev-weighted]. Then:

* for a proportion at least $1 - \eta$ of the primes $q \equiv 3 \bmod 8$
  with $e^{z/2} < q \le e^z$, every primitive character inducing $\xi\cdot(\cdot/q)$ with
  $\xi$ a character modulo $N_0$ is good (with $Q = N_0e^z$);
* for each such $q$, for a proportion at least $1-\eta$ of the primes
  $d \equiv 7 \bmod 16$ with $e^{z'/2} < d \le e^{z'}$ and $d + 1$ divisible
  by $q$ and by the odd primes up to $z$, every primitive character inducing
  $\xi\cdot(\cdot/q)^a(\cdot/d)$ with $a \in \{0, 1\}$ is good (with
  $Q = N_0e^{z+z'}$).

In particular a pair $q < d$ with these properties exists.

The square-root bound for $g_\chi$ is the strength of the Riemann
Hypothesis for $\chi$, but only on $[Y, X]$, and it is obtained for most
$q$ and $d$ by averaging, not for each.
