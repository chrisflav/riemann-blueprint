+++
kind  = "theorem"
title = "The filtration of the geometric lemma"
provenance = "published"
source = "Bernstein–Zelevinsky [bernstein-zelevinsky-1977]"
lean  = ["GlobalTheory.Published.GeometricLemmaFiltration", "GlobalTheory.geometricLemmaFiltration_holds",
         "CompanionTheory.Geo.geometricLemmaFiltration",
         "GlobalTheory.geometricLemmaFiltration_unconditional"]
order = 4
+++
Let $F$ be a non-archimedean local field, and let $P = MN$ and $P' = M'N'$ be
standard parabolic subgroups of $\GL_n(F)$. There is a finite list of
matrices of block sizes $b$ (one for each double coset of the Weyl groups)
such that for every smooth representation $\rho$ of $M$ the Jacquet module
along $N'$ of the induced representation $\mathrm{Ind}_P^G\rho$ has a finite
filtration by subrepresentations whose successive quotients are the
representations $\mathcal F_b(\rho)$: restrict $\rho$ to the Jacquet module
of type $b$, conjugate by the Weyl element of $b$, and induce up to $M'$.
