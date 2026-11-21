+++
kind  = "theorem"
title = "Bessel transforms of compactly supported functions lie in the radial space"
provenance = "new"
lean  = ["Formalism.FourierDecayAlt.P.CutSE.actual_compact_theorem",
         "Formalism.FourierDecayAlt.P5.ThmPActualCpt",
         "Formalism.FourierDecayAlt.P.CutSE.thmPActualCpt_of_R"]
uses  = ["def-archimedean-bessel-data"]
order = 100
+++
Let $G$ be the real unitary group of a hermitian form in $n = 2r + k + 1$
variables, $k \ge 1$, as in [def-archimedean-bessel-data]. Fix two vectors $z, z'$ with stabilisers $W_z, W_{z'}$,
finite-dimensional unitary representations $\pi$ of $W_z$ and $\pi'$ of
$W_{z'}$, a unipotent subgroup $N$ with a character $\psi$, and Haar
measures. For a smooth function $F$ on $G$ with values in
$\mathrm{Hom}(\pi', \pi)$, its *Bessel transform* is, as we read it,
$$J_F(g) = \int \psi(n)\overline{\psi(n')}\,\pi(w)\,F(w^{-1}n^{-1}g\,n'w')\,\pi'(w')^{-1},$$
the integral over $w \in W_z$, $w' \in W_{z'}$ and $n, n' \in N$.

Then there are subspaces $K_0, \dots, K_r$ of the space of smooth functions
on the open set $\Omega$ of big-cell coordinates where an invariant
$G_{z,z'}$ is positive, satisfying the recursion and composite formulas of
the radial system, with this property: if $F$ is smooth, compactly
supported, and $G_{z,z'} \ge \varepsilon > 0$ on the support of $F$, then
$J_F$, restricted to $\Omega$ and multiplied by explicit powers of the
coordinate norms, lies in $K_0$.

*We read* $K_0 \subset \dots \subset K_r$ as the space cut out by the radial
parts of invariant differential operators, so that the theorem says the
Bessel transform of a test function satisfies the radial equations. *It is
not clear* which system of equations the recursion encodes.
