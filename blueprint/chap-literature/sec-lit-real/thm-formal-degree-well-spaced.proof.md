+++
kind = "proof"
of   = "thm-formal-degree-well-spaced"
uses = ["thm-discrete-series-exist-upq", "thm-godement-schur-orthogonality"]
+++
Schur orthogonality [thm-godement-schur-orthogonality] shows that the left
side does not depend on $w$; call it $d(\lambda)$. *We read* the rest of the
argument as follows. One moves $\lambda$ by integer steps that keep it well
spaced, takes discrete series with the shifted parameters
[thm-discrete-series-exist-upq], realises them through explicit functions on
their lowest $K$-types, and compares $d$ along the steps with the Weyl
dimension polynomial; the two agree. Two Haar measures differ by a constant,
which gives $c$.
