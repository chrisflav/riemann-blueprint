+++
kind  = "theorem"
title = "The formal degree of well-spaced discrete series"
provenance = "modified"
source = "special case of Harish-Chandra's formal degree formula [harish-chandra-1966]"
lean  = ["ReciprocityTheory.ChartRestriction.DS.fdc_cd", "ReciprocityTheory.ChartRestriction.DS.fdCons_cd",
         "ReciprocityTheory.ChartRestriction.DS.fdCons_muG", "ReciprocityTheory.ChartRestriction.DS.G2.fdCons_cd",
         "ReciprocityTheory.ChartRestriction.DS.G2.formal_degree_constant_measure"]
order = 18
+++
Let $G = \U(p, q)$ with $p, q \ge 1$ and $n = p + q$, and fix a Haar measure
on $G$. There is a constant $c > 0$, depending on $p$, $q$ and the measure,
with the following property. Let $\sigma$ be a discrete series representation
of $G$ whose Harish-Chandra parameter $\lambda$ is well spaced in the sense of
[thm-zuckerman-tensor-discrete-series] (with the constant of that definition
replaced by a larger explicit one). Then for every non-zero vector $w$,
$$
\frac{\|w\|^4}{\int_G |\langle w, \sigma(g) w\rangle|^2\, dg}
= c \prod_{a < b}\frac{|\lambda_a - \lambda_b|}{b - a}.
$$
For the Haar measure normalised by the compact dual, $c = 1$ and the right
side is the Weyl dimension of the finite-dimensional representation with
parameter $\lambda$.

This is [thm-formal-degree-upq] restricted to well-spaced parameters, with
its own proof.
