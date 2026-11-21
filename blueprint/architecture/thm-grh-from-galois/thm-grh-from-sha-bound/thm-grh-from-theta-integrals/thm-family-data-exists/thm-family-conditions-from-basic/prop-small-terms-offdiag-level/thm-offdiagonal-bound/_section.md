+++
id    = "thm-offdiagonal-bound"
kind  = "theorem"
title = "The off-diagonal bound"
lean  = ["GlobalTheory.CarrierGap.offDiag"]
order = 2
+++
Let $D$ be a datum at a point of a family, $u \ne u'$ two of its types, $d_u$
the dimension of the representation attached to $u$, $D^*$ the normalising
mass of $D$ (a volume times an index times local formal degrees), and $b$
its size parameter. Write $K_0(u,u')$ for the off-diagonal term of the
pairing between $u$ and $u'$.

Assume the Siegel–Weil mass data, the bound on non-generic terms, and the
finite-dimensionality of the spaces of automorphic forms cut out by
discrete series at the real places. Let a class of families come with a
choice of data whose local components are isomorphic to the standard ones,
which satisfies the rank conditions and the small-terms bound of
[prop-small-terms-offdiag-level]. Then, for large auxiliary fields and every datum $D$ in
the class,
$$|K_0(u,u')|^2 \le \big(1 + b^{-6}\big)\,\frac{d_u\,d_{u'}}{D^*}\qquad (u \ne u').$$
