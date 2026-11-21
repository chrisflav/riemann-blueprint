+++
kind = "proof"
of   = "lem-good-auxiliary-primes"
uses = ["thm-pnt-progressions-exceptional-zero"]
+++
The proof rests on a mean-square estimate over the primes $q$ of the set:
$$\sum_q \Big|\sum_{n \le Z}\Lambda(n)\min(1, y/n)\,\kappa(n)\Big(\frac nq\Big)\Big|^2 \le C\,y\log y \cdot \#\{q\}$$
for all coefficients $|\kappa(n)| \le 1$. Chebyshev's inequality then bounds
the share of the $q$ for which some twisted sum is large at one of finitely
many test points of $[Y, X]$. The prime number theorem in progressions
([thm-pnt-progressions-exceptional-zero]) shows that the set of primes is
large, so the bad primes form a proportion at most $\eta$. The same argument
with $q$ fixed treats $d$. We have not unfolded how the zero-free region
($\Re s > 1 - 1/400$, $|\Im s| \le Q$) and the bound on $L'/L(1,\chi)$ follow from these sums.
