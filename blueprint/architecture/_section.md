+++
id    = "architecture"
kind  = "chapter"
title = "Outline of the proof"
uses  = ["chap-foundations", "chap-literature"]
order = 2
+++
This chapter proves [thm-half-plane] down to the level at which the
individual steps are standard results or long computations. Each later
node refines the step of the proof it belongs to.

The argument has the following shape.

1. To every polarized regular algebraic cuspidal representation of $\GL_a$
   over a CM field we attach a Galois representation, compatible with a
   weak form of the local Langlands correspondence
   ([thm-galois-reps-polarized]).
2. These Galois representations bound the Tate–Shafarevich groups of the
   Tate twists $\Q_l/\Z_l(-e)$ over the abelian fields cut out by a
   Dirichlet character inside a 2-power cyclotomic tower ([thm-sha-bound]).
3. For each primitive character $\psi$ and each large $x$ we build an
   auxiliary CM field of degree about $x^2$, and on it families of definite
   unitary groups of growing rank linked by theta lifts. The theta lifts,
   the Siegel–Weil formula and a slope inequality for hermitian lattices
   bound a weighted von Mangoldt sum $G_m(x)$ by $x^{1/2 + O(\varepsilon)}$
   ([thm-core-inequality]). The Tate–Shafarevich bound controls one error
   term.
4. Landau's theorem turns this bound, which holds on windows $[Y, Y^{3/2}]$
   of arbitrarily large $Y$, into a zero-free half-plane
   ([thm-landau-windows]).

Steps 1 and 4 are of known type. Step 2 combines known methods in a new
way. Step 3 carries the whole strength of the theorem.

The published results the proof uses are listed in [chap-literature]. All
of them are proved, not assumed.
