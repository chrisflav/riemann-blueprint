+++
id    = "bessel-period-nonvanishing-ascent-of-depth-data"
kind  = "theorem"
title = "Bessel periods stay nonzero up the theta tower"
lean  = ["GlobalTheory.Asc.ascent_of_depFixed",
         "GlobalTheory.T.bessel_period_nonvanishing_ascent_of_depth_data"]
order = 1
+++
Suppose that the lattice-vacuum theta functions at the bottom of each
column of the grid are fixed by the level subgroups of the two groups
involved (*depth is fixed*). Let $\Psi_0, \dots, \Psi_m$ be a chain of
functions along the columns of the grid, and $u$ a rapidly decreasing
automorphic form on the bottom group whose period against $\Psi_0$ is
nonzero. Then there are a real test vector $\rho$ and a Schwartz datum
$\Phi$ such that the twisted theta lift of $u$ has nonzero Bessel period
against $\Psi_m$.

This is the inductive step of the Gan–Gross–Prasad type argument: a
nonzero period at the bottom of the tower gives a nonzero period at the
top. The depth condition is proved separately and used as stated.
