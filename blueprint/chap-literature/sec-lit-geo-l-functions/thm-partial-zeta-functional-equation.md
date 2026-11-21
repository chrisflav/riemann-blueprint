+++
kind  = "theorem"
title = "Hecke's functional equation for partial zeta functions"
source = "Hecke [hecke-1917]"
lean  = ["GlobalTheory.Published.PartialZetaFunctionalEquation", "PositivityTheory.Prw.partialZetaFunctionalEquation_holds"]
order = 2
+++
Let $F$ be a totally real field of degree $n$ and discriminant $d_F$, with
different $\mathfrak d$. For an ideal class $C$ let
$\zeta(s, C) = \sum_{J \in C} N J^{-s}$, continued to a holomorphic function
on $\C \setminus \{1\}$. If $C, C'$ are ideal classes with
$C C' = [\mathfrak d]$, then
$$ d_F^{s/2}\,\Gamma_\R(s)^n\,\zeta(s, C) = d_F^{(1-s)/2}\,\Gamma_\R(1-s)^n\,\zeta(1-s, C') $$
for every $s$ such that neither $s$ nor $1-s$ is a non-positive even integer.
