+++
kind = "proof"
of   = "lem-siegel-weil-from-poisson-k"
uses = ["thm-hasse-norm-quadratic", "thm-landherr-cm", "thm-reduction-theory-unitary"]
+++
*We read* the argument as the classical one. Poisson summation for Schwartz
functions on $m \times n$ matrices over the adeles says that, for an invariant
measure,
$$\sum_X \int \psi\big(\varepsilon\,\mathrm{tr}\langle X, Z\rangle\big) f(Z)\, dZ = \sum_X f(X), \qquad \varepsilon = \pm 1.$$
It makes the theta integral invariant under the Weyl element, so the theta
integral is an automorphic form with the same constant terms as the
Eisenstein series. Their difference has vanishing constant term and is of
moderate growth on Siegel sets ([reduction theory](@thm-reduction-theory-unitary)),
hence zero. [Landherr's classification](@thm-landherr-cm) of hermitian forms and
the [Hasse norm theorem](@thm-hasse-norm-quadratic) identify the global spaces that occur.
