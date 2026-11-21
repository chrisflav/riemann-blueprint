+++
id    = "def-local-parameters"
kind  = "definition"
title = "Local parameters"
lean  = ["UpperTheory.Zero.LLC.IsRecT", "UpperTheory.Zero.LLC.RecTExists"]
order = 1
+++
Let $F$ be a non-archimedean local field. A *system of local parameters* for
$\GL_n(F)$, $n \ge 1$, assigns to every irreducible smooth representation $\pi$
a Weil–Deligne representation $\rec(\pi)$ of dimension $n$ such that:

* on characters, $\rec$ is the local Artin map;
* $\rec$ respects the Langlands classification by segments, sends cuspidal
  representations to irreducible ones, and commutes with twisting by
  $|\det|^s$;
* on *good* representations, $\rec$ also respects twists by characters,
  central characters and contragredients, is injective, and sends depth
  zero to tamely ramified;
* for a depth-zero cuspidal $\pi$ inflated from the Green character of a
  regular character $\theta$ of $\mathbb F_{g^n}^\times$, $\rec(\pi)$ has
  $N = 0$, and inertia acts with characteristic polynomial
  $\prod_j(X - \theta(z^{g^j}))$.
