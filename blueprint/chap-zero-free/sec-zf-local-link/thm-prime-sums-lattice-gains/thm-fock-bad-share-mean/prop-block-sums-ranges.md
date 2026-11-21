+++
kind  = "proposition"
title = "Block sums over ranges of exponents"
provenance = "new"
lean  = ["Formalism.MainNotions.G.SymmetricFormBlocks.restTM_closed", "Formalism.MainNotions.G.SymmetricFormBlocks.restTM_exists"]
order = 2
+++
There is $C_M \ge 1$ with the following property. Let $X$ be a local datum
satisfying the size hypotheses on its ranges of exponents, with the lower
bounds on their constants that the construction uses. For each class $\delta$ of the
segment data, each product $P$ of ranges of top exponents for $\delta$ and
each index $x$,
$$\sum_{a \in P} \beta(a, x) \le \frac{30 + C_M}{Y}\sum_{i}\sum_{a \in P}\dim Y_i(a, x),$$
where $\beta(a, x)$ counts the bad basis vectors of the block at depth
$D_1(C_M)$, and $Y_i(a, x)$ is the block obtained by updating the $i$-th
exponent.
