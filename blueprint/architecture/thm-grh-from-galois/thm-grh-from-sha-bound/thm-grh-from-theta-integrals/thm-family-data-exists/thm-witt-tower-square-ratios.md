+++
kind  = "theorem"
title = "Ratios of square constants along a Witt tower"
lean  = ["GlobalTheory.SqTower.tower_alt_bis"]
uses  = ["thm-grh-from-theta-integrals"]
order = 112
+++
Assume the published results of [thm-grh-from-theta-integrals] and the
step identities of theta towers ([def-theta-tower-step]). Assume also that
the relevant Hecke $L$-functions do not vanish: for each node $(i, j)$ of
the grid, the completed Hecke $L$-function $\Lambda$ of the character at
$(i,j)$ satisfies $\Lambda(s) \ne 0$ for integers $1 - e_0 \le s \le h$, where
$h$ is half the rank at the node.

Then for all large scales the following holds. Let $c$ and $c_0$ be the
nonzero constants of the squared theta lifts at the node $(i, j)$ for a
twist $t$ and for the base twist $\mu_0$, and $\Lambda$, $\Lambda_0$ the
corresponding Hecke $L$-functions. There are numbers $u_1, \dots, u_{p+q}$,
each a ratio of local factors at the primes of a fixed set, and an element
$\zeta$ of the field of the family that is a unit away from those primes,
with
$$\frac{c}{c_0}\prod_{k=1}^{q}\frac{\Lambda(e + k)}{\Lambda_0(e + k)} = \zeta\,\prod_k u_k\cdot\frac{c_0(t)}{c_0(\mu_0)}\prod_{k=0}^{p-1}\frac{\Lambda(e + q - k)}{\Lambda_0(e + q - k)},$$
where $e$ is the top index of the tower at $(i, j)$, $p, q$ are the two
parts of the signature, and $c_0(\cdot)$ are the constants of the bottom
theta triple.

This is the Rallis inner product formula iterated along a Witt tower: going
up one step multiplies the norm of the theta lift by one special value of
a Hecke $L$-function.
