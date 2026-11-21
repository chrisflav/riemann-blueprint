+++
kind  = "theorem"
title = "Reduction theory for unitary groups (Borel, Godement)"
lean  = ["GlobalTheory.Published.SiegelSetUnitary", "UpperTheory.Lit.siegelSetUnitary_of_core"]
order = 1
+++
Let $E/F$ be a CM extension of number fields, $V$ a non-degenerate hermitian
space over $E$ with Witt index $r$, $G = \U(V)$, and fix a Witt frame. Let
$P_0$ be the minimal parabolic subgroup of the frame and $A$ its split torus.
There are a compact subgroup $K \subseteq G(\A_F)$, a compact set
$\Omega \subseteq P_0(\A_F)^1$ and $c > 0$ such that:

* (Iwasawa) $G(\A_F) = P_0(\A_F)\,A\,K$;
* the Siegel set $\mathfrak S = \Omega\, A_c\, K$, with $A_c$ the elements of
  $A$ in the cone $t_1/t_2 > c, \dots$, is closed and
  $G(\A_F) = G(F)\,\mathfrak S$;
* $a^{-1}\Omega a$ stays in a fixed compact set for $a \in A_c$;
* $\mathfrak S$ has finite Haar measure, and the integral of $f$ over
  $\mathfrak S$ is bounded by $C\int_{A_c} h(t)\,\delta(t)^{-1}\prod_i t_i^{-1}\,dt$
  whenever $f(pak) \le h(t)$, where $\delta$ is the modulus character.

This is the reduction theory of Borel (1962) and Godement for $\U(V)$.
