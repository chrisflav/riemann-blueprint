+++
id    = "lem-counting-constants-siegel-weil"
kind  = "lemma"
title = "Counting constants from Siegel–Weil"
lean  = ["GlobalTheory.CountConstants.count_constants_of_siegelWeil"]
uses  = ["thm-siegel-main-theorem-hermitian"]
order = 1
+++

Assume the convergent Siegel–Weil formula for unitary groups. Then there are
constants $(n_0, A, C, 1/16, 1/16)$, depending only on the outer constants of
a family, with $C \ge 0$ and $A = 2(C_Y + 1)$, such that at every point of
every family the number of automorphic forms of each type is given by the
counting theorem of [thm-counting-automorphic-forms-unitary] with these constants.
