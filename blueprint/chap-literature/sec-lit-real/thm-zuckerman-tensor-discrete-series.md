+++
kind  = "theorem"
title = "Tensoring discrete series with the standard representation"
provenance = "modified"
source = "special case of Zuckerman's tensor product theorem [zuckerman-1977]"
lean  = ["ReciprocityTheory.ChartRestriction.DS.G2.zuckerman_tensor_exists",
         "ReciprocityTheory.ChartRestriction.DS.G2.zuckerman_dual_tensor_exists"]
order = 17
+++
Let $G = \U(p, q)$ with $n = p + q$, and call a Harish-Chandra parameter $\mu$
*well spaced* if $|\mu_a - \mu_b| \ge h$ whenever $a$ and $b$ lie on different
sides of the signature, for some $h$ larger than an explicit constant
depending on $p$ and $q$. Let $\sigma$ be a discrete series representation of
$G$ with well-spaced parameter $\mu$, and $e_1, \dots, e_n$ the standard basis
of $\R^n$.

Then the $K$-finite matrix coefficients of $\sigma \otimes \C^n$, with $\C^n$
the standard representation, are finite sums of matrix coefficients of
pairwise inequivalent discrete series representations $\sigma_s$ with
parameters $\mu + e_s$, where $s$ runs over exactly those indices for which
$\mu + e_s$ is again a Harish-Chandra parameter. The same holds for the dual of
the standard representation, with $\mu - e_s$ in place of $\mu + e_s$.
