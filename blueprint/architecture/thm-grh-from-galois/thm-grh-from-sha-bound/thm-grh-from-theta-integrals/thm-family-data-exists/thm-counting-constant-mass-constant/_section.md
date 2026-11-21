+++
id    = "thm-counting-constant-mass-constant"
kind  = "theorem"
title = "The counting constant equals the mass constant"
provenance = "new"
lean  = ["Formalism.L2.SG.Pf.NcAllC.ncTieC_of_closed"]
order = 104
+++
Let $E/F$ be the CM extension of a family member, with unitary groups of
rank $r$, and fix two members $u, u'$ of the family whose levels agree modulo the
square of the level prime, a flag $F_0$ and a set of representative lattices.
Suppose that the additive character $\psi$ and the measures satisfy the
standard normalisations, and that the Gram matrices involved are
nonsingular. Then the normalising constant $c$ of the count of lattice
points satisfies
$$c = \frac{n_0\, n_G}{a\,\kappa_N},
\qquad
c = c_{\mathrm{mass}}(E, F, k-1)\;|d_F|^{-2r(r+1)(k-1)}\prod_{i=k}^{r} L(i, \eta_{E/F}^{\,i})\Big/ m(F_0),$$
where $n_0, n_G, a, \kappa_N$ are the volume factors of the count, $L(i,
\eta^i)$ the special values attached to $E/F$, and $m(F_0)$ the mass of the
representative lattices.

The proof uses the *reference covolume identity*: the product of the
reference volumes of the two fundamental domains is $|d_F|^{e(k,r)}$.

*We read* the second expression as the constant of Siegel's mass formula
for the hermitian lattices of the family, so that the statement matches
the count of lattice points with the mass formula. *It is not clear*
exactly which $L$-values the factors $L(i, \eta^i)$ denote.
