+++
kind  = "theorem"
title = "Singular moduli are integral and CM curves have good reduction"
provenance = "published"
source = "Weber [weber-1908]; Hasse [hasse-1927]; see Silverman [silverman-1994]"
lean  = ["Formalism.L2.Th1.CM.JInvariantIntegrality", "ReciprocityTheory.ChartRestriction.L1.cm1",
         "Formalism.L2.Th1.CM.cm1", "Formalism.L2.Th1.CM.CM2",
         "ReciprocityTheory.ChartRestriction.L1.goodReduction_of_integral_unramified"]
order = 4
+++
Let $d$ be a squarefree positive integer with $d \equiv 3 \pmod 4$,
$K = \Q(\sqrt{-d})$, and $\Lambda \subset \C$ a lattice stable under the ring
of integers of $K$, with Weierstrass invariants $g_2, g_3$. Then:

* $j(\Lambda) = 1728\, g_2^3/(g_2^3 - 27 g_3^2)$ is an algebraic integer;
* for every prime $l \ge 5$ not dividing $d$ and every isomorphism
  $\iota : \C \cong \C_l$, there is $\lambda \in \C_l^\times$ such that
  $\lambda^4\iota(g_2)$ and $\lambda^6\iota(g_3)$ lie in the completion of the
  maximal unramified extension of $\Q_l$, are integral there, and have
  discriminant $g_2^3 - 27 g_3^2$ of absolute value $1$. In other words the
  elliptic curve $\C/\Lambda$ has good reduction at $l$ over that field.
