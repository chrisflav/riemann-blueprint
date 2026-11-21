+++
kind  = "theorem"
title = "Grothendieck–Messing deformation theory of abelian schemes"
source = "Messing [messing-1972]; Mazur–Messing [mazur-messing-1974]"
lean  = ["GlobalTheory.Published.GrothendieckDeformation", "GlobalTheory.Published.grothendieckDeformation_of_lifting"]
order = 3
+++
Let $R$ be a ring, $I \subseteq R$ an ideal with nilpotent divided powers,
and $R_0 = R/I$. For abelian schemes over $R_0$ and their lifts to $R$:

* the crystalline comparison identifies the de Rham cohomology of a lift
  with the value of the crystal of the reduction, and the Hodge filtration
  of a lift is an admissible filtration;
* lifts of an abelian scheme $A_0$ correspond to admissible lifts of its
  Hodge filtration;
* a homomorphism $f_0 : A_0 \to B_0$ lifts to lifts $A \to B$, uniquely,
  if and only if it carries the Hodge filtration of $A$ into that of $B$.

It is stated without the hypothesis that a prime be
nilpotent in $R$, as in Mazur–Messing's treatment through the universal
vector extension.
