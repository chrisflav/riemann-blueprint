+++
kind  = "proposition"
title = "Good twists from theta series"
provenance = "new"
lean  = ["GlobalTheory.ExportClose.exportAt_of_bundles_alt", "GlobalTheory.ExportClose0.exportAt_bundles_alt", "GlobalTheory.T.realization_of_published_alt", "GlobalTheory.T.series_realization_of_published_alt"]
order = 2
+++
Let $D$ be a construction over a CM field, with a choice of norms and theta
data. Let $X$ be real data, $Y$ theta series attached to $X$, and $G$
Galois data for $D$. Suppose that:

* the field of $D$ is Galois over $\Q$ and contains the roots of unity of
  order $g(g-1)$ for the two residue sizes $g$;
* the Galois representations of $G$ have the Hodge numbers predicted by $D$;
* the choice of norms is tied to $D$, and
  $Y$ has base vectors at every twisted place.

Then $D$ has the twisting property: at every twisting index good twists
exist for all powers prime to $\ell$
([thm-good-twists-all-coprime-powers]), and at every twisted
place the Bloch–Kato set hypothesis holds and the twisting input is good.
