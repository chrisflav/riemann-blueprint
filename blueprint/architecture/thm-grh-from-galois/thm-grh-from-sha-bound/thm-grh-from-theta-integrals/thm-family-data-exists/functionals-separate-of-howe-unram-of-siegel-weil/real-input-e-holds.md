+++
kind  = "theorem"
title = "Matrix coefficients of discrete series under restriction"
lean  = ["UpperTheory.Lit.Branch.RealInputE", "UpperTheory.Lit.realInputE_holds"]
order = 1
+++
There is $C > 0$ with the following property. Let $\pi$ be a discrete series
representation of a real unitary group $\U(p, q)$ with $p + q = n + 1$ and
Harish-Chandra parameter $\lambda$, and $\sigma$ a discrete series
representation of a subgroup $\U(p', q')$, $p' + q' = n$, with parameter
$\mu$, the pair of parameters bounded by $B$ and satisfying the interlacing
condition of branching. Then there are a unit vector $v_0$ in the lowest
$K$-type of $\pi$, a group element $g_0$, the vector $v = \pi(g_0)v_0$, a
smooth unit vector $w'$ of $\sigma$ and $c > 0$ such that:

* $\displaystyle\int_{\U(p',q')}\overline{\langle v, \pi(h)v\rangle}\,\langle b, \sigma(h)w'\rangle\,dh = c\,\langle b, w'\rangle$ for every $b$;
* for every $g$ the function $h \mapsto \langle v, \pi(gh)v\rangle$ is integrable
  on $\U(p', q')$, with $L^1$ norm at most
  $c\,e^{C(n+1)^4\log(8(n+1)B)}\,\ell(g)^{-(2n+7)}$, where $\ell(g)$ is the length
  of the last column of $g$; the same bound without the factor $\ell(g)$
  holds after one derivative from the Lie algebra of $\U(p',q')$;
* $|\langle v, \pi(g)v\rangle| \le A\,\|g\|^{-20(n+1)^2}$ for some $A$.

So the restriction of $\pi$ to $\U(p', q')$ contains $\sigma$ with a
quantitative lower bound, and the relevant matrix coefficients decay. This
is a quantitative form of the discrete branching of discrete series from
$\U(n+1)$ to $\U(n)$; we do not know a published source for these constants.
