+++
id    = "prop-period-identity-from-diagonal-estimate"
kind  = "proposition"
title = "The period identity from a diagonal estimate"
lean  = ["GlobalTheory.T.main_theorem_published_inputs_variant_alt_alt", "GlobalTheory.miStarRowClosing_alt_alt"]
uses = ["def-local-parameters"]
order = 1
+++
Assume a *diagonal estimate*: at every scale with bounded constant
$C_\Gamma$, a two-term bound
$$4\big(e^{C m_L} + 1\big), \qquad 4e^{-k/2} + 2e^{-k}$$
on the diagonal terms, and the rank identity
$d_0 = d^*\,(T^{k} - 1)^{f}$ for each member. Let $p$ be construction data
built from a system of local parameters ([def-local-parameters]), such that
every good point carries real data. Then the isometric period identity of
[prop-isometric-period-identity] holds at every good admissible datum of
the families built from $p$.
