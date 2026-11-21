+++
kind  = "theorem"
title = "Uniform rapid decay of cusp forms"
source = "Harish-Chandra [harish-chandra-1968]; see Moeglin–Waldspurger [moeglin-waldspurger-1995]"
lean  = ["GlobalTheory.CuspGeo.cuspDecayBound", "GlobalTheory.Published.CuspDecayBound"]
order = 6
+++
Let $E/F$ be a CM extension, $V$ a hermitian space over $E$, $G = \U(V)$,
$U$ an open subgroup of $G(\A_F)$, and $A, N \ge 0$. There are finitely many
monomials $X_l$ in the Lie algebra of $G(F_\infty)$ and a constant $C$ such
that for every smooth cuspidal function $\varphi$ on $G(F)\backslash G(\A_F)$,
right invariant under $U$, all of whose derivatives have moderate growth of
exponent $A$: if $|X_l\varphi(g)| \le c_l\,\|g\|^A$ for every $l$, then
$$
|\varphi(g)|\,\|g\|_{G(F)\backslash G(\A_F)}^{N} \le C\sum_l c_l ,
$$
where $\|g\|_{G(F)\backslash G(\A_F)} = \inf_{\gamma\in G(F)}\|\gamma g\|$ is
the height on the quotient. This is the quantitative form of the rapid decay
of cusp forms.
