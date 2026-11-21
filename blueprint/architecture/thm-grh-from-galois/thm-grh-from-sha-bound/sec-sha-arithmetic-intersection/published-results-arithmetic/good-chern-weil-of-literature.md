+++
kind  = "theorem"
title = "Mumford's good metrics compute Chern numbers"
lean  = ["GlobalTheory.GoodMetric.goodChernWeil", "GlobalTheory.Published.GoodChernWeil", "UpperTheory.LiteratureTheorems.good_chern_weil_of_literature"]
uses  = ["def-local-parameters"]
order = 11
+++
Let $X$ be a variety over a field embedded in $\C$, $E$ a vector bundle on an
open part of $X$ with a hermitian metric that is *good* along the boundary in
the sense of Mumford. Then the Chern forms of the metric are integrable, and
their integrals compute the Chern numbers of Mumford's canonical extension;
the same holds after pushing forward from a flag bundle.

This is Mumford's theorem (1977) on good metrics. It holds under the
hypotheses of [thm-grh-from-sha-bound] ([def-local-parameters]).
