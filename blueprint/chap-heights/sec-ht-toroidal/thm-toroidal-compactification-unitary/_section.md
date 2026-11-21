+++
id    = "thm-toroidal-compactification-unitary"
kind  = "theorem"
title = "Toroidal compactifications of unitary Shimura varieties"
provenance = "modified"
source = "special case of Lan [lan-2013]"
lean  = ["GlobalTheory.Published.ToroidalForFanKS", "GlobalTheory.TorKSField.toroidalForFanKS"]
order = 1
+++
Let $E$ be a CM field and fix a unitary Shimura datum of signature $(p, q)$,
$p + q \ge 1$. Let $\varphi$ be a polarised cone decomposition for the
hermitian space of dimension $\min(p, q)$, without self-intersection. Then at
every level and over every coefficient field $F$ the unitary Shimura
variety $X$ has a toroidal compactification $\bar X$ over $F$ such that:

* $\bar X$ is smooth of the dimension of $X$, and the boundary is a divisor
  with simple normal crossings, disjoint from the abelian locus;
* every boundary point has a chart of Mumford type for $\varphi$;
* $\omega^k(-\Delta)$ is ample for some $k \ge 1$, where $\omega$ is the
  determinant of the Hodge bundle;
* the logarithmic Kodaira–Spencer map is an isomorphism.

It is the unitary case of the theorem on toroidal compactifications of
PEL-type Shimura varieties.
