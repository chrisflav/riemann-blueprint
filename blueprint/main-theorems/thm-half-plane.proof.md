+++
kind = "proof"
of   = "thm-half-plane"
uses = ["thm-grh-from-galois", "thm-galois-reps-polarized"]
+++
The proof has two halves, which [architecture] describes.

The first half is arithmetic. To a polarized regular algebraic cuspidal
representation of $\GL_a$ over a CM field we attach a compatible Galois
representation ([thm-galois-reps-polarized]). We build these from theta lifts
between definite unitary groups.

The second half derives the theorem from those Galois representations
([thm-grh-from-galois]). They bound Tate–Shafarevich groups along a 2-power
cyclotomic tower. That bound, with theta lifts and Siegel–Weil identities
for families of definite unitary groups, controls a weighted sum of the von
Mangoldt function over windows $[Y, Y^{3/2}]$ with square-root error.
Landau's theorem then turns the bound into a zero-free half-plane.
