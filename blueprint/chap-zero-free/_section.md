+++
id    = "chap-zero-free"
kind  = "chapter"
title = "From prime sums to the zero-free half-plane"
uses  = ["chap-families", "chap-literature"]
order = 3
+++
This chapter proves [thm-zero-free-from-connected]: if families of definite
unitary groups carry slope data, and auxiliary CM fields exist at every
scale of long windows, then no primitive Dirichlet $L$-function vanishes
right of the critical line. It is the analytic half of the proof. Other
chapters supply the two hypotheses: [chap-families] builds the families,
and [chap-sha] proves the Tate–Shafarevich bound from which the auxiliary
fields are made.

Landau's theorem on Dirichlet series with non-negative coefficients
reduces zero-freeness to a bound $G_m(x) \le x^{1/2 + O(\varepsilon)}$ for a
weighted Chebyshev function, needed only on windows $[Y, Y^\lambda]$ of
arbitrarily large $Y$ ([sec-zf-windows]). For each primitive $\psi$ and
each such $x$ we take an abelian CM field $E$ of degree about
$x^{2+8\varepsilon}$ ([sec-zf-auxiliary-fields]). The characters of
$\Gal(E/\Q)$ split $G_m(x)$ into von Mangoldt sums over the primes in given
Frobenius classes, among them the primes inert in $E$.

The core inequality ([sec-zf-core]) bounds these sums. Each member of a
family is a chain of theta lifts of length $m$, and a slope inequality for
hermitian lattices bounds its von Mangoldt sums over the inert primes by
their main terms plus an error. Averaging over the chain divides one error
term by $m$ and multiplies another by $m$. The two balance when $m$ is
about $\sqrt x$, and this balance gives the exponent $1/2$.

The last two sections derive slope data from the family hypotheses
([thm-families-connected]). Their local input is an inequality at each
inert prime between the von Mangoldt sums and the gains of the theta lifts
([thm-prime-sums-lattice-gains]). It rests on three theorems about lattices
of polynomials over unramified quadratic extensions of discrete valuation
rings.
