+++
id    = "architecture"
kind  = "chapter"
title = "The proof in outline"
uses  = ["chap-zero-free", "chap-families", "chap-sha", "chap-galois"]
order = 2
+++
This chapter sketches Alpöge's proof of [thm-half-plane]: no Dirichlet
$L$-function vanishes for $\Re s > 1/2$. The proof has an arithmetic half,
which builds Galois representations and uses them to bound Tate–Shafarevich
groups, and an analytic half, which turns that bound into a zero-free
half-plane through families of definite unitary groups. It runs in five
stages, and each later chapter carries out one of them.

1. *Galois representations* ([chap-galois]). To every polarized regular
   algebraic cuspidal representation of $\GL_a$ over a CM field we attach a
   Galois representation, compatible with a weak form of the local Langlands
   correspondence ([thm-galois-reps-polarized]).
2. *The Tate–Shafarevich bound* ([chap-sha]). These representations bound
   the Tate–Shafarevich groups of the twists $\Q_l/\Z_l(-e)$ over the
   abelian fields that a Dirichlet character $\psi$ cuts out of a 2-power
   cyclotomic tower ([thm-sha-bound]).
3. *Families* ([chap-families]). For each primitive $\psi$ and each large
   $x$, an auxiliary CM field of degree about $x^2$ carries families of
   definite unitary groups of growing rank, linked by theta lifts and
   carrying hermitian lattices ([thm-family-data-exists]). The theta lifts
   and the Siegel–Weil formula ([chap-theta]) and a covolume bound from
   arithmetic heights ([chap-heights]) give the families their properties;
   the Tate–Shafarevich bound controls one error term.
4. *Slope data and the core inequality* ([chap-zero-free]). The families
   give a slope inequality for the hermitian lattices at primes inert in the
   auxiliary field. Averaged along a chain of theta lifts, it bounds a
   weighted von Mangoldt sum $G_m(x)$ by $x^{1/2 + O(\varepsilon)}$
   ([thm-core-inequality]).
5. *Landau's theorem* ([chap-zero-free]). The bound holds on windows
   $[Y, Y^{3/2}]$ of arbitrarily large $Y$, and Landau's theorem on Dirichlet
   series with non-negative coefficients turns it into a zero-free
   half-plane ([thm-landau-windows]).

Stages 1 and 5 are of known type. Stage 2 combines known methods in a new
way. Stages 3 and 4 carry the strength of the theorem: the square root in
the core inequality is the Riemann Hypothesis.

The chapter has three sections. The first states the three statements that
pass between the stages. The second gives the chain of reductions from
[thm-grh-from-galois] down to [chap-zero-free], as theorems read in order,
each reducing to the next. The third lists the points a careful reader
should check first. [chap-literature] collects the published results the
proof uses.
