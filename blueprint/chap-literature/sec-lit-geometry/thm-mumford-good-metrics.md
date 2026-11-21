+++
kind  = "theorem"
title = "Mumford's good metrics compute Chern numbers"
provenance = "modified"
source = "after Mumford [mumford-1977]"
lean  = ["GlobalTheory.GoodMetric.goodChernWeil", "GlobalTheory.Published.GoodChernWeil", "UpperTheory.LiteratureTheorems.good_chern_weil_of_literature"]
uses  = ["def-local-parameters"]
order = 14
+++
Let $X$ be a variety over a field embedded in $\C$, $E$ a vector bundle on an
open part of $X$ with a hermitian metric that is *good* along the boundary in
the sense of Mumford. Then the Chern forms of the metric are integrable, and
their integrals compute the Chern numbers of Mumford's canonical extension;
the same holds after pushing forward from a flag bundle.

Mumford's theorem is the statement on $X$; the form on flag bundles is
the one used here. It holds under the
hypotheses of [thm-grh-from-sha-bound] ([def-local-parameters]).
