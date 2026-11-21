+++
kind  = "theorem"
title = "Projective bundle formula"
provenance = "published"
source = "SGA 5 [sga-5]"
lean  = ["GlobalTheory.EtC.D1", "GlobalTheory.EtC.projectiveBundleFormula_vectorBundle_any_space"]
order = 3
+++
Let $V$ be a vector bundle of rank $N$ on a base $X$ on which $q$ is invertible,
$\pi : \mathbb P(V) \to X$ its projective bundle and $\xi = c_1(\mathcal O(1))$.
Then
$$\bigoplus_{j=0}^{N-1} H^{n-2j}\big(X, \Z/q(i-j)\big) \to H^n\big(\mathbb P(V), \Z/q(i)\big), \qquad (a_j) \mapsto \sum_j \pi^* a_j \cup \xi^j$$
is bijective for all $n$ and $i$.
