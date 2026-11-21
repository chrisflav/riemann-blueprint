+++
id    = "thm-local-estimate-inert-primes"
kind  = "theorem"
title = "The local estimate at inert primes"
provenance = "new"
lean  = ["Formalism.L2.G.loc_proved", "Formalism.MainNotions.TraceSpectra.stmtE"]
order = 10
+++
Every member $D$ of a family satisfies the *local estimate at inert primes*
in closed form: for all constants for which $D$ is admitted, there is $C_0$
such that for $C \ge C_0$ the following holds. Let $p \ge 13$ be a prime,
$\mathcal O' / \mathcal O$ an unramified quadratic extension of discrete
valuation rings of residue characteristic $p$ attached to $D$, and let the
orbit data $(T, r, L_1, L_2)$, weights $\lambda_0$ and scale parameters
$a, Y$ satisfy the explicit size conditions (among them
$256(m+1)^2|T|Y^2 \le p^{L_1 - 1}$ and an upper bound for $a$ in terms of
$C$, $p$ and the orbit data). Then for every $t$ beyond an explicit bound,
the lattice of polynomials attached to these data at level $t$ satisfies
the local lattice condition with defect $C|T|r^2(m+1)/Y$.

In particular the reduced form of the second local theorem holds for every
member. *It is not clear* from the statements what the local lattice
condition measures beyond this shape.
