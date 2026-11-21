+++
kind = "proof"
of   = "thm-fock-bad-share-mean"
uses = ["prop-block-bounds-from-four"]
+++
*Diagonalising.* For $p \ne 2$, every symmetric bilinear form $B$ on a
finitely generated $\Z_p$-lattice $L$ of polynomials, not identically zero,
has a *minimal vector* $x \in L$: $B(x, x) \ne 0$ and $B(u, x) \in \Z_p B(x, x)$
for all $u \in L$. Splitting off minimal vectors one at a time diagonalises
the form on each block (the Jordan splitting of $p$-adic lattices). If
$X\,\mathrm{diag}(c)\,Y^T = p^D\cdot 1_n$ with $X, Y$ integral $n \times m$
matrices, then at least $n$ of the $c_a$ are nonzero of valuation at most
$D$; this counts the basis vectors whose norm has valuation at most $D$, and
they span a good sublattice. The argument works equally from an orthogonal
basis of the lattice, from an orthogonal splitting or from a splitting
matrix.

*Bounds on blocks.* This reduces the claim to four bounds on the blocks of
the local construction, for every admitted local datum with the constants
chosen in order: a bound on the levels of the base blocks (which implies a
bound on their dimensions), an orthogonality bound, the range bound for the
exponents (which holds by counting), and a bound on the directions of the
blocks. With the bounds on positive parts, these are the hypotheses of
[prop-block-bounds-from-four], whose conclusion, with the freeness and ratio
conditions of the blocks, gives the remaining bounds; they add up to the
mean bound on the bad share.
