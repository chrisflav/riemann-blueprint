+++
id    = "thm-galois-reps-polarized"
kind  = "theorem"
title = "Galois representations of polarized representations"
provenance = "modified"
source = "after Harris–Taylor [harris-taylor-2001]; Shin [shin-2011]; Chenevier–Harris [chenevier-harris-2013]; Barnet-Lamb–Gee–Geraghty–Taylor [barnet-lamb-2012]; [barnet-lamb-2014a]; Caraiani [caraiani-2012]; [caraiani-2014]"
lean  = ["UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter",
         "UpperTheory.Gal.Int.galoisRepresentations_of_thetaLift"]
uses  = ["def-galois-reps-polarized", "def-local-parameters"]
order = 3
+++
Polarized pairs have Galois representations ([def-galois-reps-polarized])
for the system of local parameters of [thm-local-parameters-exist].

The published theorem has full local–global compatibility. Here it is
asked for only where the local parameter is determined
([rem-local-parameters-weak]).
