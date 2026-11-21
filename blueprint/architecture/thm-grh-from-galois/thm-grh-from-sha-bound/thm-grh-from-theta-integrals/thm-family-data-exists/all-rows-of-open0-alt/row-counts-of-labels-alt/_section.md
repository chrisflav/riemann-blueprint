+++
id    = "row-counts-of-labels-alt"
kind  = "proposition"
title = "Counting constants and irreducible constituents"
lean  = ["GlobalTheory.CountRow.row_counts_of_ties_alt", "GlobalTheory.CountRowByName.row_counts_of_labels_alt"]
uses  = ["siegel-weil-unitary-convergent"]
order = 4
+++

Assume the convergent Siegel–Weil formula for unitary groups
[siegel-weil-unitary-convergent]. Suppose that at every chosen datum the
space of automorphic forms of the member is identified isometrically with a
concrete space of forms, compatibly with a good Hecke operator and a
labelling. Then there are counting constants $(n_0, A, C, c, c_b)$, depending
only on the outer constants of the family, with $C \ge 0$,
$A \ge 2(C_{Y} + 1)$ and $c \ge c_I > 0$, such that, for all large auxiliary
fields:

1. the counting theorem of [count-constants-of-siegel-weil] holds at every
   point of every family with these constants;
2. eventually in $x$, every point carries a labelling of its irreducible
   constituents that is injective on good labels and whose count is bounded
   by $\varepsilon(c_I, r, f)$.
