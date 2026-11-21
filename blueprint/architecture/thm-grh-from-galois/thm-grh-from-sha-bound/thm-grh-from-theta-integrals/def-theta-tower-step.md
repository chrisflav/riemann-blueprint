+++
kind  = "definition"
title = "Steps in theta towers"
lean  = ["GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.ThetaIntegralsAgree",
         "GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.LocalMatching"]
order = 2
+++
Let $E/F$ be a CM extension and consider dual pairs of unitary groups of
hermitian spaces with given signatures. We say that *theta towers have
step identities* if the following hold.

* Every triple of representations related by theta lifts has matching
  local data.
* Matched global theta integrals decay, are proportional with a single
  constant, and factor through coinvariants.
* Replacing the second group $\U(\cdot, b+2)$ by $\U(\cdot, b)$ multiplies
  the constant by $C \cdot L^S(\nu, \tfrac{a-(b+2)}{2} + 1)$ up to a unit and
  an explicit factor. Here $L^S$ is a partial Hecke $L$-function. The same
  holds for the first group.

These are the identities of the Rallis inner product formula: each step up
a theta tower costs one special value of an $L$-function. They make
precise the chain of lifts $\U(X_0) \to \U(X_1) \to \dots \to \U(X_m)$
between definite unitary groups in the announcement. The proof uses the
Siegel–Weil formula.
