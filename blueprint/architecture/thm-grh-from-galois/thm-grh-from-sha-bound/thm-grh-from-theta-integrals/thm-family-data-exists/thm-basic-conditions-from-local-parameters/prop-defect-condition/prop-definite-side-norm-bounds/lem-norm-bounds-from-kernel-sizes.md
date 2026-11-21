+++
kind  = "lemma"
title = "Norm bounds from the sizes of kernel data"
provenance = "new"
lean  = ["GlobalTheory.ColRows.rowsBody_of_kerTies", "GlobalTheory.ColRowsTopS.rowsBody_colFace",
         "GlobalTheory.T.columnsMemberRows_of_logLevel_le", "GlobalTheory.T.memberRows_of_kernelDatum_sizes"]
order = 1
+++
For constants $C_Y$ and $C_T \ge 0$ there is $C_0$ with the following
property. Take kernel data for a member over a totally complex field $K$,
with sizes bounded in terms of $C_Y$ and $C_T$ and with height constant at least $C_0$. Suppose
that the hermitian form at the base point is positive definite at every
infinite place, and that the inner products of evaluated vectors are at
most the squared norms in any frame. Then the chain of theta lifts built
from the kernel data satisfies the norm bounds of
[prop-definite-side-norm-bounds], and the frames at the
infinite places are invertible.
