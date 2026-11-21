+++
kind  = "theorem"
title = "The Jacquet–Rallis fundamental lemma"
provenance = "published"
source = "Yun [yun-2011] (large residue characteristic); Beuzart-Plessis [beuzart-plessis-2021]"
lean  = ["GlobalTheory.JR.unitMatch_all", "GlobalTheory.T.jacquetRallisUnitMatch_all_ranks",
         "GlobalTheory.JR.unitMatch_of_weilField", "GlobalTheory.T.jacquetRallisUnitMatch_of_weilRep_quadratic"]
order = 1
+++
Let $E/F$ be an unramified quadratic extension of $p$-adic fields of
characteristic $0$, with Haar measures giving the integral points volume $1$. For
every $r$, the characteristic function of the integral points of
$\mathfrak{gl}_r(F) \times F^r \times F^r \times F$ and that of the integral points of
$\mathrm{Herm}_r(E) \times E^r \times F$ *match*: for every regular semisimple
invariant $a$, the orbital integral over $\GL_r(F)$ with the transfer factor
$\eta(\det(\text{Krylov matrix}))$ equals the orbital integral over $\U_r$ at any
$X$ with invariant $a$, and it vanishes when no such $X$ exists.
