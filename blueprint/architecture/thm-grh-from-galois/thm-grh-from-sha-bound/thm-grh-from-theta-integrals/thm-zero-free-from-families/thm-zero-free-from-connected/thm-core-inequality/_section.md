+++
id    = "thm-core-inequality"
kind  = "theorem"
title = "The core inequality"
provenance = "new"
lean  = ["UpperTheory.Comparison₂.core_gm", "UpperTheory.Comparison₂.level_gm_le_on_family_scales"]
uses  = ["def-chebyshev-weighted", "def-slope-data"]
order = 3
+++
If there are slope data at a large $x$, then
$$G_m(x) \le x^{1/2 + (e_D + e_L + 7)\varepsilon}.$$
The whole strength of the Riemann Hypothesis lies in this inequality.
