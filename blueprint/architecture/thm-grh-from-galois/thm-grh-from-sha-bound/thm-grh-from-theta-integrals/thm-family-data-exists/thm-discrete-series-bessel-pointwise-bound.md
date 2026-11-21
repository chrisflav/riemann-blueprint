+++
kind  = "theorem"
title = "Pointwise bound for Bessel transforms of discrete series coefficients"
provenance = "new"
lean  = ["BpJoin.ThmBpDS", "GlobalTheory.BpDiscreteSeriesTwoInputs.pointwise_bound_discreteSeries",
         "GlobalTheory.BpEigen.pointwise_bound_eigenfunction", "GlobalTheory.T.pointwiseBound_capelli_eigenfunction",
         "GlobalTheory.T.pointwiseBound_discreteSeries_coefficients", "GlobalTheory.discreteSeriesCoef_pointwiseBound"]
uses  = ["thm-bessel-transform-radial-space"]
order = 102
+++
For all constants $C_h$ and $C_0 \ge 0$ there are $C_4 \ge 0$ and $C_{g,0}$
such that for $C_g \ge C_{g,0}$ the following holds. Let $f$ be a $K$-finite
matrix coefficient of a discrete series representation of the real unitary
group of [thm-bessel-transform-radial-space] with Harish-Chandra parameter $\lambda'$,
and suppose the parameter $\lambda$ of the Bessel datum satisfies the
standard size conditions with parameter $b$ and has all gaps at least
$200\,\|\lambda' - \lambda\|_1$. Let $p_0$ be an integer with
$3(r+1) \le 2p_0 \le 2C_0(r+1)^2$, and $n_0 = 30(r+1)^2 + 6$ or $0$
according as the two Bessel data agree or not. Then at every local point
$\gamma$ with $G(\gamma) > 0$,
$$E(\gamma) \le b^{C_4(2r+2)^4}\,G(\gamma)^{-(2p_0 + n_0)}\,\|J_f\|^2,$$
where $E(\gamma)$ is the energy of the Bessel transform of $f$ at $\gamma$
and $\|J_f\|$ its $L^2$ norm.
