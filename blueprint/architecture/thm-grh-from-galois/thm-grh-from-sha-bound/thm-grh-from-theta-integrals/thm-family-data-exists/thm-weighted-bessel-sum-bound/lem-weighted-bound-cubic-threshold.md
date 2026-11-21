+++
kind  = "lemma"
title = "The weighted bound from a cubic threshold"
provenance = "new"
lean  = ["CompanionTheory.WaveGrid.uniform_bessel_rank_three_of_inputs",
         "CompanionTheory.WaveGrid.weighted_bound_rotated_uniform_of_cubic_threshold"]
uses  = ["thm-weighted-bessel-sum-bound"]
order = 1
+++
Suppose:

* every discrete series parameter satisfying the size conditions belongs to
  a family of parameters obtained by branching, and the derivatives of the
  Bessel transforms of discrete series coefficients along the big cell, and
  their moments, are bounded by powers of $b$;
* for some constant $C$, every Bessel transform of a $K$-finite coefficient,
  for parameters with gaps at least $C(2r+2)^{9/2}(3(r+1)n^2 + n^3)$, is
  carried to a nonzero multiple of itself, on the big cell and in the orbital
  integrals, by a rescaling of the torus coordinates.

Then the weighted bound of [thm-weighted-bessel-sum-bound] holds.

More generally the conclusion holds for any threshold $t(n, \varepsilon) \le
C_t n^3$ for which Zuckerman's gap bound and its dual hold.
