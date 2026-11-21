+++
kind  = "theorem"
title = "Theta lifts along the families"
provenance = "new"
lean  = []
uses  = ["def-local-parameters", "def-family-data", "def-theta-tower-step"]
order = 1
+++
Fix a system of local parameters ([def-local-parameters]) and the families
of definite unitary groups of [def-family-data] built from it. Then for all
large scales:

1. *Step identities.* Theta towers have step identities
   ([def-theta-tower-step]): matched theta integrals along a tower are
   proportional, and replacing $\U(\cdot, b+2)$ by $\U(\cdot, b)$ multiplies
   the constant by a partial Hecke $L$-value
   $L^S(\nu, \tfrac{a-(b+2)}{2} + 1)$, up to a unit and an explicit factor.
2. *Separation.* Theta integrals detect every nonzero vector on the bottom
   group of a theta tower at a member of a family.
3. *Downward lifts.* A nonzero Hecke eigenform whose Satake parameters at
   the good places contain a segment
   $q_w^{(t-1)/2}\nu, \dots, q_w^{-(t-1)/2}\nu$ has a nonzero downward theta
   lift, and theta pairings are injective on Hecke eigenspaces.
4. *Rational test vectors.* Up to one constant and roots of unity, the
   twisted theta lifts of the test vectors take values in the field of the
   family.
5. *Indefinite slope bound.* At every point of a family that carries a grid
   of evaluation points, the largest slope of the hermitian lattice on the
   indefinite side is at most its height minus the mean of $\log\kappa$ over
   the twists.
6. *Isometric period identity.* At every admissible datum there are an
   isometry $V$, unitary matrices $U_u$ and nonzero constants $a_u$,
   $\zeta_u(t)$ with
   $\zeta_u(t)\,\mathrm{ev}\big(P_{u,t}(\varphi, F)\big) = a_u\,\big\langle V\,\Theta_t(F),\ P_u(U_u\varphi)\big\rangle$;
   in particular the multiplicity condition of
   [thm-basic-conditions-from-local-parameters] holds.
7. *Off-diagonal bound.* For a class of families with the rank conditions
   and the small-terms bound of [prop-small-terms-offdiag-level], distinct
   types $u \ne u'$ of a datum $D$ satisfy
   $|K_0(u,u')|^2 \le (1 + b^{-6})\,d_u d_{u'}/D^*$.
8. *Counting.* The dimension $D$ of the space of automorphic forms of a
   given type on a unitary group in $n \ge n_0$ variables over a totally
   real field of degree $f$ satisfies $|D - M| \le e^{-\frac1{16}nf\log n}M$,
   where the main term $M$ is a volume times a formal degree; and the
   constant of the count of lattice points is the constant of Siegel's mass
   formula.
9. *Valuations.* At every place $w$ over the level prime of a member $u$,
   the twisted vectors of the reference chain have $w$-valuation at least
   $-m\,E_{u,w}$, where $m$ is the length of the lattice chain and $E_{u,w}$
   an explicit exponent.

Each item is the main theorem of one section of this chapter, where it is
stated with its exact hypotheses.
