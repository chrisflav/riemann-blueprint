+++
kind  = "theorem"
title = "Lifting abelian schemes along nilpotent divided powers"
lean  = ["GlobalTheory.Published.AbelianLifting", "GlobalTheory.abelianScheme_hom_lifting_nilpotent_dividedPowers"]
order = 8
+++
Let $R \to R_0$ be a surjection of rings whose kernel $I$ carries nilpotent
divided powers. For an abelian scheme $A_0$ over $R_0$ write $D(A_0)$ for
its crystalline (Dieudonné) module evaluated on $R$.

* (Objects.) If $A_0$ has some lift $A'$ over $R$, then every admissible
  lift of the Hodge filtration to $D(A_0)$ is the Hodge filtration of some
  lift $A$ of $A_0$.
* (Morphisms.) A homomorphism $f_0 : A_0 \to B_0$ lifts to given lifts $A, B$
  if and only if $D(f_0)$ maps the Hodge filtration of $A$ into that of $B$,
  and the lift is then unique.

This is the deformation theorem of Grothendieck and Messing (1972), with
Mazur–Messing (1974), stated for abelian schemes. Unlike
[thm-grothendieck-messing-nilpotent-p], it does not ask $p$ to be nilpotent in $R$.
