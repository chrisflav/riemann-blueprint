+++
id    = "thm-sha-error-from-congruence-bounds"
kind  = "theorem"
title = "From congruence bounds to the error bound"
lean  = ["UpperTheory.GalC.linkN_of_boundAtTwoThree_slot", "UpperTheory.GalC.linkN_of_twGood_galoisPreconditions", "UpperTheory.GalC.linkedAt_linkN_of_boundAtTwoThree"]
uses  = ["def-local-parameters"]
order = 1
+++
Let $\mathcal F$ be a family with good twists whose members can be cut down
to their good eigensystems, as in the cutting hypothesis of
[thm-sha-error-from-local-bounds], and satisfy, from some scale on, the
Galois conditions and the character conditions at $g_0, g_1$. Suppose
$\mathcal F$ satisfies the bound at $2$ and $3$. Then $\mathcal F$ satisfies
the Tate–Shafarevich error bound ([def-sha-error-term]). The same holds for
the classes of families of [def-family-data] built from a system of local
parameters ([def-local-parameters]).
