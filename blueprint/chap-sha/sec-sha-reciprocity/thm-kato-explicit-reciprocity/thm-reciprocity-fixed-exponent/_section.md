+++
id    = "thm-reciprocity-fixed-exponent"
kind  = "theorem"
title = "The reciprocity law for zeta classes of fixed exponent"
provenance = "new"
lean  = ["UpperTheory.V.Z.Kato.K5.hco"]
order = 1
+++
Keep the setting of [thm-kato-explicit-reciprocity], with $l \nmid N$,
and let $\chi$ be a multiplicative function on integers prime to $N$, periodic
modulo $N$ with values in $\Z_l^\times$. Let $\lambda$ be a functional of the
same kind, attached to $\chi$ and weight $2e - 1$. Suppose $W$, twisted by
$\epsilon^{-e}$, is upper triangular with lower right entry $1$ on the part of
inertia at $l$ fixed by $\mu_l$. Then for every $c_0$ there are $c'$,
$\kappa_0 \ne 0$ and units $p_m$ with $p_{m+1} \equiv p_m \bmod l^m$ such that
for every system $(Y_r)$ of zeta classes of exponent $c_0$ attached to a
residue $x \bmod N$, every $m \ge 1$ and every unit $y \bmod l^m$, the
Hodge–Tate image of $Y_m$ at $y$ is congruent, modulo $l^{m - c'}$, to
$$p_m^{-1}\,l^{c_0}\,\kappa_0\sum_{\delta \in (\Z/N)^\times}\chi(\delta)^{-1}\,\lambda\big(l^m E_{m,x\delta^{-1}}\big),$$
with $E_{m,x}$ an explicit Eisenstein series of level $Nl^m$ attached to
$c, d$ and $x$.
