+++
kind  = "theorem"
title = "Brauer's induction theorem, degree-zero form"
provenance = "modified"
source = "after Brauer [brauer-1947]"
lean  = ["GlobalTheory.BrauerZero.brauerDegreeZero", "GlobalTheory.Published.BrauerDegreeZero"]
order = 5
+++
Let $\rho$ be a finite-dimensional complex representation of a finite group
$G$. There are subgroups $H_1, \dots, H_r$, characters
$\chi_i : H_i \to \C^\times$ and integers $c_i$ such that
$$ \operatorname{tr}\rho - \dim\rho = \sum_{i=1}^r c_i\big(\operatorname{Ind}_{H_i}^G \chi_i - \operatorname{Ind}_{H_i}^G 1\big) $$
as functions on $G$.

This is the degree-zero form of the induction theorem: a virtual
character of degree zero is an integral combination of differences
$\operatorname{Ind}\chi - \operatorname{Ind} 1$ of characters induced from
linear characters.
