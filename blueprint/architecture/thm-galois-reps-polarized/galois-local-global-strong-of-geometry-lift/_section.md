+++
id    = "galois-local-global-strong-of-geometry-lift"
kind  = "theorem"
title = "Galois representations from odd-rank geometry and theta lifts"
lean  = ["UpperTheory.Gal.Int.galoisLocalGlobalStrong_of_geometry_lift",
         "UpperTheory.Gal.Int.galoisLocalGlobal_of_geometry_lift"]
uses  = ["geo-one-holds", "thm-theta-lift-nonvanishing"]
order = 11
+++
Suppose that definite unitary groups of odd rank have geometric Galois
representations as in [geo-one-holds], and that theta lifts from definite
unitary groups do not vanish as in [thm-theta-lift-nonvanishing]. Then
polarized pairs have Galois representations in the sense of
[def-galois-reps-polarized], for the system of local parameters of
[thm-local-parameters-exist]. The proof first gives the conclusion in a slightly
different form and then converts it.
