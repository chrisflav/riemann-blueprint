+++
kind  = "theorem"
title = "A mean value theorem for bad shares"
provenance = "new"
lean  = ["Formalism.CountingSumsFrames.TheoremMV7", "Formalism.InvariantFactorPaths.MC.Top.theoremMV7",
         "Formalism.InvariantFactorPaths.MC.theoremMV7",
         "Formalism.MainNotions.G.CountingStatementReduction.alternative_mean_value_theorem"]
order = 10
+++
*Mean value theorem.* Let $p$ be an odd prime, $r \ge 2$, and consider
lattices $Y(n)$ of polynomials with the Fock pairing attached to a system of
letters with ties $n = (n_i)$ in the chain order. Let $1 \le a$, $1 \le E$,
and for each tie $i$ let $n_i$ run over an arithmetic progression
$n_{0,i} + d_i j$, $0 \le j < Y_i$, with $d_i$ prime to $p$; let $P$ be the product
of these progressions. Under the size
hypothesis,
$$\frac{1}{|P|}\sum_{n \in P}\operatorname{bad}_D\big(Y(n)\big) \le \sum_i \varepsilon_i,$$
where $\operatorname{bad}_D$ is the number of bad vectors at depth
$D = \lfloor t(E + \kappa) + \kappa\rfloor$ and $\varepsilon_i$ is an
explicit function of the tie size, $Y_i$ and $\kappa$.
