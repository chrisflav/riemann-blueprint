+++
kind = "proof"
of   = "prop-definite-side-norm-bounds"
uses = ["thm-hasse-norm-quadratic", "thm-chowla-selberg"]
+++
Identify the data of the admissible datum with kernel data of the member:
the fields, primes, characters, the choice of places above each prime and
the twisting characters all match. The kernel data have sizes bounded in
terms of $C_Y$ and $C_T$, the hermitian form at the base point is positive
definite at every infinite place, and the inner products of evaluated
vectors are at most the squared norms in any frame; we use the frame given
by the characters of the second coordinates. We first bound the norms of
the second coordinates and the
[mean logarithms of periods](@thm-chowla-selberg), then the vectors and
norms of the chain of theta lifts. These bounds are uniform because the
logarithm of the level is bounded by the sizes. The Hasse norm theorem
[thm-hasse-norm-quadratic] enters in comparing norms at the places above
each prime. The same estimates show that the frames at the infinite places
are invertible. We have not unfolded the estimates further.
