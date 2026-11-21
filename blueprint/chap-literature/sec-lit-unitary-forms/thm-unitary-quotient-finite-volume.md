+++
kind  = "theorem"
title = "Adelic quotients of unitary groups have finite volume"
provenance = "published"
source = "Borel and Harish-Chandra; see Borel [borel-1969]"
lean  = ["GlobalTheory.Mem.Vol.FiniteVolume₂", "GlobalTheory.Mem.VolFin.finVol",
         "GlobalTheory.T.finiteVolume_adelicUnitaryQuotient",
         "GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicCovolumeFinite.Statement",
         "GroundTheory.Heights₂.Heights.FiniteCovolume.AdelicCovolumeFinite.of_remaining",
         "CompanionTheory.SWFin.adelicCovolumeFinite"]
order = 1
+++
Let $E/F$ be a CM extension of number fields and $J$ a non-degenerate
hermitian matrix over $E$, with unitary group $\U(J)$. Then $\U(J)(F)$ is a
lattice in $\U(J)(\A_F)$: for every Haar measure $\mu$ on $\U(J)(\A_F)$, every
measurable fundamental domain of $\U(J)(F)$ has finite $\mu$-measure, and such
fundamental domains exist.
