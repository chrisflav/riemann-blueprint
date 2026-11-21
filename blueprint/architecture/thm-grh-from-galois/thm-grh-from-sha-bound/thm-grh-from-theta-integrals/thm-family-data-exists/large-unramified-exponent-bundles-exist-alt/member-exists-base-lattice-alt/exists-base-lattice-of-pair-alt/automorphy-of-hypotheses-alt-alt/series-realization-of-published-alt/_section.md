+++
id    = "series-realization-of-published-alt"
kind  = "proposition"
title = "Good twists from theta series"
lean  = ["GlobalTheory.ExportClose.exportAt_of_bundles_alt", "GlobalTheory.ExportClose0.exportAt_bundles_alt", "GlobalTheory.T.realization_of_published_alt", "GlobalTheory.T.series_realization_of_published_alt"]
uses  = ["cheb", "chebotarev-degree-one", "cusp-rapid-decay", "global-artin-reciprocity", "global-euler-char-full", "global-finiteness", "greenberg-wiles", "local-euler-char", "local-euler-char-k", "local-finiteness", "local-finiteness-k", "local-tate-duality", "local-tate-duality-k", "ray-character-artin", "unramified-orthogonality"]
order = 1
+++
Assume the results of [automorphy-of-hypotheses-alt-alt] on Galois
cohomology, theta series and Hecke operators. Let $D$ be a construction over
a CM field, with a choice of norms and theta data. Let $X$ be real data,
$Y$ theta series attached to $X$, and $G$ Galois data for $D$. Suppose that:

* the field of $D$ is Galois over $\Q$ and contains the roots of unity of
  order $g(g-1)$ for the two residue sizes $g$;
* the Galois representations of $G$ have the Hodge numbers predicted by $D$;
* the local conclusion holds for $D$, the choice of norms is tied to $D$, and
  $Y$ has base vectors at every twisted place.

Then $D$ has the twisting property: at every twisting index good twists
exist for all powers prime to $\ell$
([twist-all-powers-of-galois-cohomology-class-field]), and at every twisted
place the Bloch–Kato set hypothesis holds and the twisting input is good.
