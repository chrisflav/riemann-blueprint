+++
id    = "prop-pair-coefficient-local-decomposition"
kind  = "proposition"
title = "Local decomposition of the pair coefficients"
provenance = "new"
lean  = ["Formalism.L2.SG.Pf.Coef.cutAt_of_deep", "Formalism.L2.SG.Pf.Coef.rowsDatumP_of_deep"]
order = 2
+++
Let $D$ be a datum, and suppose the three inputs of [lem-local-decomposition-inputs]
hold for $D$. Fix local models at the finite places, types $u, u'$ with
$T_u \equiv T_{u'} \bmod g^2$, a flag, representative lattices, uniformisers
$\varpi_p$ and a normalising constant $n_c$ satisfying the counting formula.
Then all local densities are non-negative, and the coefficient of the pair
$(u,u')$ decomposes as a sum over terms $\gamma$: each term receives a local
class at every place, compatible with the unramified data off a finite set,
and a density. The partner sums and fibre counts of this decomposition
satisfy the identities needed for [thm-offdiagonal-bound].
