+++
kind = "proof"
of   = "thm-weighted-bessel-sum-bound"
uses = ["thm-bessel-transform-radial-space", "lem-radial-operator-transfer"]
+++
Two inputs are needed. First, every discrete series parameter satisfying
the size conditions belongs to a family of parameters obtained by
branching, and the derivatives of the Bessel transforms of discrete series
coefficients along the big cell, and their moments, are bounded by powers
of $b$. Second, for some constant $C$, every Bessel transform of a
$K$-finite coefficient, for parameters with gaps at least
$C(2r+2)^{9/2}(3(r+1)n^2 + n^3)$, is carried to a nonzero multiple of
itself, on the big cell and in the orbital integrals, by a rescaling of the
torus coordinates. Zuckerman's bound on the gaps of the parameters that
occur in a tensor product with a finite-dimensional representation, and its
dual, give these with a threshold $t(n, \varepsilon)$ of cubic size in
$n = 2r + k + 1$; in fact $t(n, \varepsilon) \le 43 n^3$.

Uniqueness of discrete series with large gaps, the infinitesimal
characters of discrete series, smoothness of $K$-finite vectors and the
asymptotics of Bessel coefficients of equal and different types then give a
bound for Bessel periods on a grid of points. The continuity of Capelli
coefficients turns it into the weighted bound. The radial analysis of
[thm-bessel-transform-radial-space] and [lem-radial-operator-transfer]
enters through the asymptotics.
