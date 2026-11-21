+++
kind  = "theorem"
title = "Grothendieck–Messing deformation theory"
lean  = ["GlobalTheory.Published.GrothendieckDeformation.grothendieckMessing", "GlobalTheory.Published.GrothendieckMessing"]
uses  = ["thm-grothendieck-messing"]
order = 9
+++
Let $p$ be a prime and $R \to R_0$ a surjection of rings with $p$ nilpotent
in $R$, whose kernel carries nilpotent divided powers. Then for abelian
schemes $A$ over $R$ lifting $A_0$:

* the crystalline module of $A_0$ evaluated on $R$ is canonically the de
  Rham cohomology of $A$, and the Hodge filtration of $A$ is admissible;
* lifts of $A_0$ correspond to admissible lifts of the Hodge filtration;
* homomorphisms lift exactly when they respect the Hodge filtrations, and
  then uniquely.

This is Grothendieck–Messing theory (Messing 1972). We derive it from the
deformation statement [thm-grothendieck-messing].
