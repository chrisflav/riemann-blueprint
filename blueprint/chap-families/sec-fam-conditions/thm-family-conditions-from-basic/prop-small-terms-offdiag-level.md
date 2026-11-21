+++
kind  = "proposition"
title = "Small terms, the off-diagonal bound and the level bound"
provenance = "new"
lean  = ["GlobalTheory.LocalRows.at_choice_alt", "GlobalTheory.LocalRows.lg1_sLp_sO_hTF",
         "GlobalTheory.LocalRows.sLp_sO_hTF_of_siegelWeil"]
order = 2
+++
For every choice of admissible data along a class of families, the
following hold for large auxiliary fields. Here a datum $D$ at a point of a
family carries types $u$, each with a finite-dimensional representation of
dimension $d_u$, an integer $T_u$, a normalising mass $D^*$, a size
parameter $b$, and for $u \ne u'$ an off-diagonal term $K_0(u, u')$
([thm-offdiagonal-bound]).

1. *Small terms.* In the expansion of $K_0(u,u')$, the large terms and the
   non-scalar terms each contribute at most $\varepsilon_D\, d_u d_{u'}/D^*$.
2. *The off-diagonal bound* of [thm-offdiagonal-bound].
3. *Level bound.* $T_u\,\kappa^{2r} \ge 1$ for every type $u$, where $\kappa$
   and $r$ are invariants of $D$.
