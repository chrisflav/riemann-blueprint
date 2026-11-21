+++
kind = "proof"
of   = "thm-siegel-weil-definite-k"
uses = ["thm-hasse-norm-quadratic", "thm-landherr-cm", "thm-reduction-theory-unitary"]
+++
*We read* the argument as the classical one. First, for $\Re z$ large, the
Fourier coefficients of Siegel Eisenstein series along a parabolic subgroup
split as the Fourier coefficient of an Eisenstein series on a smaller group
plus a term that transforms by $e^{\tau(n - 2z)}$ under dilations. Poisson
summation for Schwartz functions on $m \times n$ matrices over the adeles says
that, for an invariant measure,
$$\sum_X \int \psi\big(\varepsilon\,\mathrm{tr}\langle X, Z\rangle\big) f(Z)\, dZ = \sum_X f(X), \qquad \varepsilon = \pm 1.$$
It makes the theta integral invariant under the Weyl element, so the theta
integral is an automorphic form, and the splitting of Fourier coefficients
shows that it has the same constant terms as the Eisenstein series. Their
difference has vanishing constant term and is of moderate growth on Siegel
sets ([reduction theory](@thm-reduction-theory-unitary)), hence zero.
[Landherr's classification](@thm-landherr-cm) of hermitian forms and the
[Hasse norm theorem](@thm-hasse-norm-quadratic) identify the global spaces that
occur.
