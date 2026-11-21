+++
kind  = "theorem"
title = "Good twists for all powers of a ray class character"
lean  = ["GlobalTheory.TwExportTop.twistAllPowers_of_galoisCohomology_classField"]
uses  = ["cheb", "global-euler-char-full", "global-finiteness", "greenberg-wiles", "local-euler-char", "local-euler-char-k", "local-finiteness", "local-finiteness-k", "local-tate-duality", "local-tate-duality-k", "ray-character-artin", "unramified-orthogonality"]
order = 1
+++
Assume the Galois-cohomological results of
[automorphy-of-hypotheses-alt-alt]. Let $D$ be a construction over a CM
field $E$, with exponent data, and let $i$ be a twisting index with prime
$\ell = \ell_i$ that has a non-zero place. Suppose the admissibility
conditions of Bloch–Kato type hold at $i$, together with conditions on
signs, supports and the action of Hecke operators (they commute and act
semisimply). Suppose further that the theta forms attached to $i$ have full
rank, with chosen bases.

Then for every finite set $A$ of places of $E$ and every $\varepsilon' > 0$
there are a finite set $Q$ of places, an integer $k'$ and a character $\psi'$
of the ray class group of conductor $Q$, with values in the units of the
coefficient ring modulo $\ell^{k'}$, such that $\psi'^a$ is a good twist
avoiding $A$ for every integer $a$ prime to $\ell$.
