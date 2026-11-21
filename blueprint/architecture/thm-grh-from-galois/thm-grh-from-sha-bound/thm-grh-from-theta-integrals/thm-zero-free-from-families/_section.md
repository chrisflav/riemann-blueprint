+++
id    = "thm-zero-free-from-families"
kind  = "theorem"
title = "Zero-freeness from families"
lean  = ["UpperTheory.Top.zero_free_all_of_green_v_win", "UpperTheory.Top.every_character_of_green_v_win"]
uses  = ["def-sha-bound", "def-family-data", "def-zero-free-primitive",
         "def-nonvanishing-half-plane"]
order = 6
+++
Suppose that the Tate–Shafarevich bound holds with exponent $401$, and that
some class of families satisfies the family hypotheses
([def-family-data]). Then no $L$-function of a primitive character vanishes
right of the critical line ([def-zero-free-primitive]), and hence Dirichlet
$L$-functions do not vanish right of the critical line.
