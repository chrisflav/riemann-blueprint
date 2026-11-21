+++
kind  = "lemma"
title = "The Kodaira–Spencer isomorphism from rigid charts"
lean  = ["GlobalTheory.LogKSAssembly.hasLogKS", "GlobalTheory.RigChart.toroidalForFanKS_of_rigidForFan", "GlobalTheory.T.logKodairaSpencer_iso_smooth_snc_toroidalModel", "GlobalTheory.T.toroidalFanKodairaSpencer_of_rigidBoundaryCharts"]
uses  = ["thm-unitary-rigid-boundary-charts", "thm-toroidal-compactification-unitary"]
order = 11
+++
If unitary compactifications with rigid boundary charts exist
([thm-unitary-rigid-boundary-charts]), then the compactifications
of [thm-toroidal-compactification-unitary] exist: on a smooth toroidal model with boundary
of simple normal crossings, the logarithmic Kodaira–Spencer map
identifies the logarithmic tangent bundle $T_{\bar X}(-\log \Delta)$ with the bundle of
$\mathcal O_E$-balanced endomorphisms of $\mathrm{Lie}\,G$, where $G$ is the semi-abelian
scheme. *We read* "balanced" as compatible with the action of $\mathcal O_E$ and
its conjugation.
