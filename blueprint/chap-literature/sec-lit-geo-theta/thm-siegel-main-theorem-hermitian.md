+++
kind  = "theorem"
title = "Siegel's main theorem for hermitian forms"
provenance = "published"
source = "Weil [weil-1965]"
lean  = ["GlobalTheory.CompanionTheory.SW.siegelWeilUnitaryConvergent", "HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent"]
order = 7
+++
Let $J$ be a non-degenerate hermitian $M \times M$ matrix over $E$. Then
$\U(J)(F)\backslash\U(J)(\A_F)$ has finite volume. If $2n < M$, then for every
non-degenerate hermitian $n \times n$ matrix $T$ and every factorisable
Schwartz function $\Phi = \Phi_\infty \otimes \bigotimes_v \Phi_v$ on
$M_{n \times M}(\A_E)$, the average over $\U(J)(F)\backslash\U(J)(\A_F)$ of
$\sum_{X : X J X^* = T}\Phi(g^{-1}X)$ equals the product of local densities
$$ \int_{[\U(J)]} \sum_{X J X^* = T} \Phi(g^{-1} X)\, dg = g_\infty(T) \prod_v g_v(T), $$
where $g_v$ is the density of the push-forward of $\Phi_v$ under
$X \mapsto X J X^*$, for suitably normalised measures.

This is Siegel's main theorem for hermitian forms, the Siegel–Weil formula
in the range where the Eisenstein series converges.
