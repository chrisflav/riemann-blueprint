+++
kind  = "theorem"
title = "Dixmier–Malliavin factorisation for matrix groups"
provenance = "modified"
source = "after Dixmier–Malliavin [dixmier-malliavin-1978]"
lean  = ["GlobalTheory.Published.DixmierMalliavinFactorisation", "GlobalTheory.dixmierMalliavinFactorisation_fromLibrary"]
order = 16
+++
Let $G$ be a topological group with a closed embedding into $\GL_n(\C)$,
$\mu$ a Haar measure and $V$ a neighbourhood of $1$. Every smooth compactly
supported function $f$ on $G$ (smooth through the embedding) is a finite sum
$$
f = \sum_i g_i * h_i
$$
of convolutions of smooth compactly supported functions with
$\operatorname{supp} g_i \subseteq V$ and
$\operatorname{supp} h_i \subseteq \operatorname{supp} f$. It is stated for
such groups, with control of supports.
