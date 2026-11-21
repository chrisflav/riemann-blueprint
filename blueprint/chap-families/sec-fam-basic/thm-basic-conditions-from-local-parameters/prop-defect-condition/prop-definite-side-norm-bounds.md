+++
kind  = "proposition"
title = "Norm bounds on the definite side"
provenance = "new"
lean  = ["GlobalTheory.ColRows.rowsU_of_colPins_alt",
         "GlobalTheory.Fc.RL.DefSide.definiteSideCondition_of_nprimeDef_of_nuFull",
         "GlobalTheory.T.kernel_columns_from_ties_alt", "GlobalTheory.ColRows.rowsBody_of_kerTies",
         "GlobalTheory.ColRowsTopS.rowsBody_colFace",
         "GlobalTheory.T.columnsMemberRows_of_logLevel_le",
         "GlobalTheory.T.memberRows_of_kernelDatum_sizes"]
order = 1
+++
For constants $C_Y$ and $C_T \ge 0$ there is $C_0$ with the following
property. Let a member of a family carry an admissible datum, with scale
$c \ge C_0$, such that:

* point evaluation has the expected form, and the heights are bounded in
  terms of $C_Y$;
* the scale parameters satisfy $X' \ge 8$, $x \ge 2$, $4a < T_u$ and
  $\log T_u \le C_T\, m L$ for every $u$;
* the definiteness condition on $N'$ holds, and the modules $\nu_u$ are full
  with positive rank.

Then for every $u$ there are a chain of theta lifts from the first space
and, at each infinite place $v$, a frame $X_0(v)$ of the definite hermitian
form $H$ at the base point, that is, $X_0(v)^{-*}X_0(v)^{-1} = H$. The square of
the operator norm of point evaluation at the end of the chain, measured in
these frames, is at most $e^{h}$ for an explicit height bound $h$. The
logarithms of the squared norms at each step are bounded by sums of local
sizes. Finally $\nu_u$ is a lattice.
