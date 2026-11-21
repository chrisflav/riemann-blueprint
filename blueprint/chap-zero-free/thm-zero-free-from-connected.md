+++
kind  = "theorem"
title = "Zero-freeness from slope data and auxiliary fields"
provenance = "new"
lean  = ["UpperTheory.Top.zeroFreeAll_of_topG"]
uses  = ["def-connected-families", "def-zero-free-primitive", "def-auxiliary-field-data"]
order = 1
+++
Let $\lambda > 1$. Suppose that

1. families have slope data ([def-connected-families]), and
2. for every primitive character $\psi$, auxiliary CM fields
   ([def-auxiliary-field-data]) with the properties listed in
   [thm-auxiliary-fields] for $\psi$, the Tate–Shafarevich bound among
   them, exist at the scales $x$ of windows $[Y, Y^\lambda]$ for
   arbitrarily large $Y$.

Then primitive $L$-functions do not vanish right of the critical line
([def-zero-free-primitive]).
