+++
kind  = "theorem"
title = "Hasse norm theorem"
provenance = "published"
source = "Hasse [hasse-1931]"
lean  = ["GlobalTheory.Published.HasseNorm", "GlobalTheory.CNorm.hasseNorm",
         "GlobalTheory.T.hasseNormPrinciple_of_isCyclic"]
order = 8
+++
Let $L/K$ be a cyclic extension of number fields and $a \in K^\times$. If $a$
is a norm from $K_v \otimes_K L$ for every place $v$ of $K$, finite or
infinite, then $a$ is the norm of an element of $L$.

The quadratic case is [thm-hasse-norm-quadratic].
