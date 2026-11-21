+++
kind  = "lemma"
title = "The Kodaira–Spencer isomorphism from rigid charts"
provenance = "new"
lean  = ["GlobalTheory.LogKSAssembly.hasLogKS", "GlobalTheory.RigChart.toroidalForFanKS_of_rigidForFan", "GlobalTheory.T.logKodairaSpencer_iso_smooth_snc_toroidalModel", "GlobalTheory.T.toroidalFanKodairaSpencer_of_rigidBoundaryCharts"]
uses  = ["thm-unitary-rigid-boundary-charts"]
order = 2
+++
Let $\bar X$ be a compactification with rigid boundary charts as in
[thm-unitary-rigid-boundary-charts]: a smooth toroidal model with boundary
$\Delta$ of simple normal crossings, carrying the semi-abelian scheme $G$.
Then the logarithmic Kodaira–Spencer map identifies the logarithmic tangent
bundle $T_{\bar X}(-\log \Delta)$ with the bundle of $\mathcal O_E$-balanced
endomorphisms of $\mathrm{Lie}\,G$. *We read* "balanced" as compatible with
the action of $\mathcal O_E$ and its conjugation.
