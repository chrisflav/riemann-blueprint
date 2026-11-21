+++
kind  = "theorem"
title = "Discrete series of U(J) do not depend on the diagonalisation"
provenance = "modified"
lean  = ["GlobalTheory.Published.DiscreteSeriesHermitianUnique", "PositivityTheory.Prw.discreteSeriesHermitianUnique_holds"]
order = 14
+++
Let $J$ be a non-degenerate hermitian $n \times n$ matrix and $P, P'$
invertible with $P^*J_\varepsilon P = P'^*J_\varepsilon P' = J$, where
$J_\varepsilon$ is the diagonal form of signature $\varepsilon$. Transport
two discrete series representations of $\U(J_\varepsilon)$ with the same
parameter $\lambda$ to $\U(J)$ along $P$ and along $P'$. The two
representations of $\U(J)$ are unitarily equivalent. This follows from the
uniqueness in [thm-discrete-series-lowest-k-type], since $PP'^{-1}$ lies in
$\U(J_\varepsilon)$.
