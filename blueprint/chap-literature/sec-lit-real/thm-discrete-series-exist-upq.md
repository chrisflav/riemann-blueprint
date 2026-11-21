+++
kind  = "theorem"
title = "Existence of discrete series of U(p,q)"
provenance = "published"
source = "Harish-Chandra [harish-chandra-1965], [harish-chandra-1966]; Schmid [schmid-1975]; Vogan [vogan-1981]"
lean  = ["CompanionTheory.RgDs.B.discreteSeriesUpqExists", "GlobalTheory.Published.DiscreteSeriesUpqExists",
         "CompanionTheory.RgDs.B.discreteSeriesExists", "GlobalTheory.Published.DiscreteSeriesExists"]
order = 8
+++
Let $G = \U(p,q)$, $N = p + q$, $K = \U(p)\times\U(q)$, and let
$\lambda \in \R^N$ be strictly decreasing with every
$\lambda_a - (N-1)/2$ an integer. There is an irreducible unitary
representation $\sigma$ of $G$ whose matrix coefficients are
square-integrable and which contains the $K$-type
$\lambda + \rho_n - \rho_c$; this $K$-type is minimal in the sense of
Vogan: every $K$-type $\mu$ of $\sigma$ satisfies
$\|\lambda + \rho_n - \rho_c + 2\rho_c\| \le \|\mu + 2\rho_c\|$.

In other words, for every Harish-Chandra parameter $\lambda$ a discrete
series representation of $\U(p,q)$ with parameter $\lambda$ exists.
