+++
id    = "closed-of-minimal-vector"
kind  = "proposition"
title = "Bad shares from minimal vectors"
lean  = ["Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_coefficient_function",
         "Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_minimal_vector",
         "Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_basis",
         "Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_lattice",
         "Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_splitting",
         "Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_splitting_matrix",
         "Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_symmetric_dims",
         "Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_symmetric_finite",
         "Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_symmetric_windows",
         "Formalism.MainNotions.G.SymmetricFormBlocks.integralityFromMetric_of_orthBasisLat",
         "Formalism.MainNotions.G.SymmetricFormBlocks.integrality_from_metric_of_orthogonality_window",
         "Formalism.MainNotions.G.SymmetricFormBlocks.theorem_A_closed_of_nine_open_bounds"]
order = 10
+++
The conclusion of [theorem-a-closed-form-holds] follows from three inputs:

* *minimal vectors*: for $p \ne 2$, every symmetric bilinear form $B$ on a
  finitely generated $\Z_p$-lattice $L$ of polynomials, not identically zero,
  has $x \in L$ with $B(x, x) \ne 0$ and $B(u, x) \in \Z_p B(x, x)$ for all
  $u \in L$;
* *diagonal rank*: if $X\,\mathrm{diag}(c)\,Y^T = p^D\cdot 1_n$ with $X, Y$
  integral $n \times m$ matrices, then at least $n$ of the $c_a$ are nonzero
  of valuation at most $D$;
* the *range bound* for the exponents of the admitted local data.

Several variants hold with the same conclusion: from an orthogonal basis of
the lattice, from an orthogonal splitting, from a splitting matrix, or from
bounds on the dimensions of the symmetric blocks.
