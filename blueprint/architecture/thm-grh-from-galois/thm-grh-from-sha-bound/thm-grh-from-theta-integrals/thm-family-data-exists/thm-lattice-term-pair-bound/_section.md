+++
id    = "thm-lattice-term-pair-bound"
kind  = "theorem"
title = "Bound for sums over pairs of lattice terms"
provenance = "new"
lean  = ["Formalism.L2.SG.RowsPos.TypeP", "GlobalTheory.T.typeBound_of_largeGap_discreteSeries_bessel",
         "GlobalTheory.TypeAsm.TopGap.typeBound_of_gap", "GlobalTheory.rowsPos_typeP"]
order = 105
+++
For all constants $C_g, c_b, C_w, c_T, C_T, C_0$ with $c_b, c_T > 0$ there are
constants $C_H, C_h, C_p \ge 0$ such that for all large $C_s, C, C', C_l$ the
following holds. Let $D$ be a family member satisfying the hypotheses of the
second-order theorems with these constants, and $u$ one of its lattices. For indices
$1 \le j', j'' \le r$, labels $\delta', \delta''$ and any finite set $S$ of
relevant pairs of terms with these indices and labels,
$$\sum_{(t, t') \in S}\|v_t\|\,\|v_{t'}\| \le d_\pi\, m_u\,
A(j', \delta')A(j'', \delta''),$$
where $v_t$ is the vector attached to the term $t$, $d_\pi$ a formal degree,
$m_u$ a Siegel mass, and $A(j, \delta)$ an explicit product of two
amplitudes depending on the constants.

*It is not clear* what the terms are; *we read* them as the vectors
indexed by lattice points that occur in the expansion of the theta
integrals.
