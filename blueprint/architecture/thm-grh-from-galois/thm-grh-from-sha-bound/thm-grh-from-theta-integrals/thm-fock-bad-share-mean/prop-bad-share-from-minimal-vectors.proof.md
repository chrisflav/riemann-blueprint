+++
kind = "proof"
of   = "prop-bad-share-from-minimal-vectors"
uses = ["prop-bad-share-from-block-bounds"]
+++
Splitting off minimal vectors one at a time diagonalises the form on each
block (the Jordan splitting of $p$-adic lattices, $p \ne 2$). The diagonal
rank bound then counts the basis vectors whose norm has valuation at most
$D$; they span a good sublattice. This gives the restricted bounds on the
block dimensions and directions, so [prop-bad-share-from-block-bounds]
applies.
