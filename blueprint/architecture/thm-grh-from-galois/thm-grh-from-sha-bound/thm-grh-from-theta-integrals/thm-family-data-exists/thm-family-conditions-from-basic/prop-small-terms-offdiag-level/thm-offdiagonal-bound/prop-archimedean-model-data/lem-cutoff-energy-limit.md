+++
kind  = "lemma"
title = "Energies of cut-off vectors in the archimedean model"
lean  = ["Formalism.FourierDecayAlt.MA.LemmaEModel", "Formalism.FourierDecayAlt.P.lemma_model"]
order = 2
+++
There are constants $C_2, C_6 > 0$ such that the following holds. Take
archimedean parameters $(k, r)$ with level data, eigenfunctions $j_\pi$
indexed by the $K$-types $\pi$ with eigenvalues $\lambda$, decaying and
self-adjoint to order $2N+2$ with $N \ge r+1$, and a cut-off interval
$[\alpha, \beta]$ with
$$\beta - \alpha \ge C_6\big(kN(r+1)^2 + N^2(r+1)^2\big).$$
For every admitted word $w$ of length at most $N$, the energy form of the
vector cut off at scale $\varepsilon$ tends, as $\varepsilon \to 0^+$, to
$$\operatorname{size}(w)\int\sum_\pi|j_\pi(q)|^2\,d\mu_0(q).$$
