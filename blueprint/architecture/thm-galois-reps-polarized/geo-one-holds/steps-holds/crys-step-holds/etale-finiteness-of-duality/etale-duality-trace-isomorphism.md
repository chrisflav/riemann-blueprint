+++
kind  = "theorem"
title = "Additive characteristic classes"
lean  = ["GlobalTheory.EtC.D2", "LateralTheory.E.EtaleChapterDTwo", "LateralTheory.Fix.EtaleChapterDTwo.s57",
         "UpperTheory.Et.D2.a0", "UpperTheory.Et.D2.intersectionNumber_baseChange",
         "UpperTheory.Et.etale_duality_trace_isomorphism"]
uses  = ["projective-bundle-formula-vector-bundle-any-space"]
order = 10
+++
For $q \ge 1$ and $k > 0$ there are classes $s_k(V) \in H^{2k}(X, \Z/q(k))$ for
vector bundles $V$ on spaces $X$ where $q$ is invertible, such that
$s_k$ commutes with pull-back, $s_k(V \oplus W) = s_k(V) + s_k(W)$, and
$s_k(L) = c_1(L)^k$ for a line bundle $L$. These are the power sums of the
Chern roots (Newton classes). The statement also shows that this follows
from the earlier basic theorems of étale cohomology, and that intersection
numbers do not change under base change.
