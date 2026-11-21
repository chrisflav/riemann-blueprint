+++
kind  = "theorem"
title = "Schur orthogonality for square-integrable representations"
provenance = "published"
source = "Godement [godement-1947]"
lean  = ["GlobalTheory.Published.SchurOrthogonalitySquareIntegrable", "PositivityTheory.Stage1.PM.schurOrthogonalitySquareIntegrable"]
order = 6
+++
Let $G$ be a locally compact unimodular group with Haar measure $\mu$ and
$\pi$ an irreducible unitary representation of $G$ on $H$. If one matrix
coefficient $\langle w_0, \pi(g)v_0\rangle$ with $v_0, w_0 \ne 0$ is
square-integrable, then all matrix coefficients are, and there is a formal
degree $d > 0$ with
$$
\int_G \langle w, \pi(g)v\rangle\,\overline{\langle w', \pi(g)v'\rangle}\,d\mu(g)
= \frac{\langle v', v\rangle\,\langle w, w'\rangle}{d}
$$
for all $v, w, v', w' \in H$.
