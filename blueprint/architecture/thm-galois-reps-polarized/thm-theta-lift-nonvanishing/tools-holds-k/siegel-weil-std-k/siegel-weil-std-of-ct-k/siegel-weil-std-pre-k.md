+++
kind  = "lemma"
title = "Siegel–Weil from Poisson summation"
lean  = ["PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_pre_k"]
uses  = ["siegel-weil-std-k"]
order = 10
+++
Suppose Poisson summation holds for Schwartz functions on $m \times n$ matrices
over the adeles: for an invariant measure,
$$\sum_X \int \psi\big(\varepsilon\,\mathrm{tr}\langle X, Z\rangle\big) f(Z)\, dZ = \sum_X f(X), \qquad \varepsilon = \pm 1,$$
and suppose the splitting of constant terms of [siegel-weil-std-of-ct-k]. Then
the Siegel–Weil formula [siegel-weil-std-k] holds.
