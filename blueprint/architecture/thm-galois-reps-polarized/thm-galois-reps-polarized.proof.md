+++
kind = "proof"
of   = "thm-galois-reps-polarized"
uses = ["thm-theta-lift-nonvanishing"]
+++
We build the representations from definite unitary groups and theta lifts
([thm-theta-lift-nonvanishing]).

1. *Odd rank* ([geo-one-holds]). Let $a$ be odd. Transfer an automorphic
   representation of a definite unitary group in $a$ variables to a Hecke
   eigensystem on a compact unitary Shimura variety of Harris–Taylor type,
   of signature $(1, a-1)$ at one infinite place. This needs a cuspidal
   type at one place above $l$ and lacunary weights at another. Look for
   the eigensystem in the $l$-adic cohomology of Kuga–Sato varieties over
   it, the fibre powers of the universal abelian scheme.
   * The Eichler–Shimura congruence relation controls Frobenius.
   * The crystalline comparison theorem and the Hodge–Tate decomposition
     give the properties at $l$.
   * The holomorphic Lefschetz formula of Atiyah and Bott, compared with
     the fixed points of Hecke correspondences at CM points, gives the
     Hodge numbers.

   The result is a representation of unknown dimension on which the
   Satake polynomial kills Frobenius. The lacunary Hodge–Tate weights and
   the determinant cut out a piece of dimension $a$.
2. *Congruences.* Congruences between weights and a limiting argument in
   the style of Chenevier reach the remaining weights.
3. *Even rank.* Lift a representation of an even-rank unitary group in two
   ways to an odd-rank group. The Galois representations of the two lifts
   are $\rho \otimes \kappa \oplus \psi_1$ and $\rho \otimes \kappa \oplus \psi_2$,
   with disjoint sets of characters, and comparing them isolates $\rho$.
4. *To $\GL_a$* ([galois-local-global-strong-of-geometry-lift]). Descend a
   conjugate-self-dual $\pi$ to a definite unitary group, and pass to all
   polarized pairs by the cyclic base change of Arthur and Clozel.
   Solvable base change turns depth-zero components into principal series,
   which gives compatibility at the ramified places.

The transfer in step 1 cites only the Hasse norm theorem among published
results. *It is not clear* how it is proved without a trace formula.
