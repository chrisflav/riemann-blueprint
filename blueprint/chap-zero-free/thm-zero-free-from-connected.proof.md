+++
kind = "proof"
of   = "thm-zero-free-from-connected"
uses = ["thm-zero-free-from-windows", "thm-core-inequality", "def-slope-data"]
+++
Fix a primitive $\psi$ and a small $\varepsilon > 0$.

1. *Slope data.* The fields of hypothesis 2 satisfy the Tate–Shafarevich
   bound, so the members of every family built on them satisfy it too.
   Hypothesis 1 then gives constants $e_D, e_L$, independent of
   $\varepsilon$, and a family built on these fields that carries slope
   data ([def-slope-data]) at every large $x$ of its windows.
2. *The core inequality.* At each such $x$, [thm-core-inequality] gives
   $$G_m(x) \le x^{1/2 + (e_D + e_L + 7)\varepsilon}.$$
3. *Landau's theorem.* These are bounds on windows $[Y, Y^\lambda]$ of
   arbitrarily large $Y$, with $c = e_D + e_L + 7$ independent of
   $\varepsilon$, so [thm-zero-free-from-windows] applies.

Hypothesis 2 comes from the Tate–Shafarevich bound by
[thm-auxiliary-fields], and hypothesis 1 from the family hypotheses by
[thm-families-connected].
