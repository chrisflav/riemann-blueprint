+++
kind  = "theorem"
title = "A principal polarisation has one section"
provenance = "published"
source = "Mumford [mumford-1970]"
lean  = ["GlobalTheory.AbLaw.principalPolarisation_unique_section", "GlobalTheory.Published.principalPolarisationOneSection"]
order = 4
+++
Let $(A, L)$ be a principally polarised abelian variety over an
algebraically closed field. Then $\dim H^0(A, L) = 1$.

This follows from the Riemann–Roch theorem for abelian varieties, which gives
$\dim H^0(A, L)^2 = \# K(L)$ for ample $L$.
