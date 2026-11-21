+++
id    = "thm-counting-automorphic-forms-unitary"
kind  = "theorem"
title = "Counting automorphic forms on unitary groups"
provenance = "new"
lean  = ["GlobalTheory.CountBridge.count_typed_of_volumeStep", "GlobalTheory.CountFinal.countingTheorem_of_volumeStep", "GlobalTheory.T.unitaryAutomorphicCounting_of_compactDualVolumeRatio"]
order = 1
+++

Suppose the *volume step* holds: every hermitian space of dimension $n \ge 3$
with an anisotropic vector of norm $\pm1$ splits off a space of dimension
$n - 1$, and the normalised Haar volumes of the two unitary groups differ by
the Siegel mass ratio. Then for every $A$ there are $n_0$ and $C_0 \ge 0$ such
that for $n \ge n_0$ the space of automorphic forms of a given type on a
unitary group in $n$ variables over a totally real field of degree $f$ is
finite-dimensional, and its dimension $D$ satisfies
$$|D - M| \le e^{-\frac1{16}nf\log n}\,M,$$
where $M$ is the main term: a volume times a formal degree.
