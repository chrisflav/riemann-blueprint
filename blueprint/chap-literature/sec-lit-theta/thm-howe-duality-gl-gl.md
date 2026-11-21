+++
kind  = "theorem"
title = "Howe duality for (GL_n, GL_n') on polynomials"
provenance = "published"
source = "Howe [howe-1989a]"
lean  = ["GlobalTheory.Published.GLHoweDuality", "PositivityTheory.Stage1.PM.gLHoweDuality"]
order = 10
+++
Let $n, n' \ge 1$ and let $\GL_n(\C) \times \GL_{n'}(\C)$ act on the
polynomial functions on $n' \times n$ matrices. Then
$$ \C[M_{n' \times n}] \cong \bigoplus_{\lambda} S_\lambda(\C^n) \otimes S_\lambda(\C^{n'}), $$
the sum over partitions $\lambda$ with at most $\min(n, n')$ parts, $S_\lambda$
the Schur functor; the $S_\lambda(\C^n)$ are irreducible and pairwise
non-isomorphic, and likewise for $n'$. The same holds for the compact
subgroup $\U(n) \times \U(n')$.

This is the representation-theoretic form of the Cauchy identity.
