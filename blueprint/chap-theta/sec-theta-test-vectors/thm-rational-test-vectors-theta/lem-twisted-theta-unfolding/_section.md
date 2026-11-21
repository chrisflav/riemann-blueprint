+++
id    = "lem-twisted-theta-unfolding"
kind  = "lemma"
title = "Unfolding the twisted theta integral"
provenance = "new"
lean  = ["GlobalTheory.RowUnfLast.twisted_theta_integral_unfolding",
         "GlobalTheory.T.twisted_theta_integral_unfolds"]
order = 2
+++
Suppose that twisted theta lifts along the grid send cusp forms to cusp
forms, and that the finite sums defining the test vectors are well defined.
Then for all large scales and every choice of test data the following
holds. For every coefficient vector $\tau$ there are $\sigma$ and values
$z_t$ of the twisting characters such that, for every flip-finite $\tau'$,
every volume and every point $y$,
$$B^+\big(\Psi_a,\ \vartheta(\tau, \tau')(y)\big) = z_t^{-1}\,s\sum_\beta\Big(\prod_w c_{\beta, w}\Big)\,P_\beta(\sigma, y).$$
Here $B^+$ is the Bessel period against the column function $\Psi_a$,
$\vartheta(\tau,\tau')$ the theta lift along the opposite path of the
tower, $s$ a fixed constant, $\beta$ runs over the terms of the expansion,
$c_{\beta,w}$ are their local coefficients and $P_\beta$ the definite
periods attached to them.

So the Bessel period of a theta lift is a finite sum of periods over a
definite unitary group.
