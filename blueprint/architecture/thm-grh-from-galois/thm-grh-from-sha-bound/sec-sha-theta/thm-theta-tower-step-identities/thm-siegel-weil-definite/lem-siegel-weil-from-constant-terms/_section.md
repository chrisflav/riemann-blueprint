+++
id    = "lem-siegel-weil-from-constant-terms"
kind  = "lemma"
title = "The Siegel–Weil formula from constant terms"
provenance = "new"
lean  = ["PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_ct"]
uses  = ["thm-siegel-weil-definite"]
order = 10
+++
Suppose that the constant term of every Siegel Eisenstein series along a
maximal parabolic splits: for $\Re z$ large it is an Eisenstein series on the
Levi factor of smaller rank, plus a term $c_2$ that transforms under the
dilations $y_\tau$ of the parabolic by $c_2(y_\tau x) = e^{\tau(n - 2z)}c_2(x)$.
Then the Siegel–Weil formula for definite spaces
([thm-siegel-weil-definite]) holds.
