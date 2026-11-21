+++
kind  = "theorem"
title = "Rational invariance of theta functions"
source = "after Weil [weil-1964]"
lean  = ["GlobalTheory.Published.ThetaRationalInvariance", "PositivityTheory.Stage1.PM.thetaRationalInvariance"]
order = 4
+++
Let $E$ be a CM field and $N, N'$ with $NN'$ even. For the theta functions
attached to a Weil representation of the dual pair $\U_N \times \U_{N'}$, there are integers $a_\tau, a'_\tau$ with
$2a_\tau = \epsilon'\,n'_\tau - N'$ and $2a'_\tau = \epsilon\,n_\tau + N$ such
that rational elements $\gamma \in \GL_N(E)$, $\gamma' \in \GL_{N'}(E)$ act on
theta functions $F$ by
$$
\Omega(\gamma, \gamma')F = \prod_\tau \tau(\det\gamma)^{-a_\tau}\,\tau(\det\gamma')^{-a'_\tau}\;(\gamma,\gamma')^*F .
$$
This is the invariance of theta functions under rational points that makes
theta series automorphic. *It is not clear* from the statement
which space of theta functions on which torus is meant, nor what the
characters $n_\tau, n'_\tau$ and signs $\epsilon, \epsilon'$ are.
