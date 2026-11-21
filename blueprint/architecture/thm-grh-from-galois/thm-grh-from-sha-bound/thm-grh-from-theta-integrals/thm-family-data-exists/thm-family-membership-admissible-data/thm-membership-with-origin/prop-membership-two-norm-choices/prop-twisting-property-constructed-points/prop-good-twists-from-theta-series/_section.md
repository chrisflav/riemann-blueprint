+++
id    = "prop-good-twists-from-theta-series"
kind  = "proposition"
title = "Good twists from theta series"
lean  = ["GlobalTheory.ExportClose.exportAt_of_bundles_alt", "GlobalTheory.ExportClose0.exportAt_bundles_alt", "GlobalTheory.T.realization_of_published_alt", "GlobalTheory.T.series_realization_of_published_alt"]
uses  = ["thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-cusp-rapid-decay", "thm-artin-reciprocity", "thm-tate-global-euler-characteristic", "thm-tate-global-finiteness", "thm-greenberg-wiles", "thm-tate-euler-characteristic-global-places", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness", "thm-tate-local-finiteness-padic", "thm-tate-local-duality-global-places", "thm-tate-local-duality-l-adic", "thm-ray-class-characters-galois", "thm-unramified-annihilators"]
order = 1
+++
Assume the results of [prop-twisting-property-constructed-points] on Galois
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
([thm-good-twists-all-coprime-powers]), and at every twisted
place the Bloch–Kato set hypothesis holds and the twisting input is good.
