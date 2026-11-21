+++
kind  = "theorem"
title = "Cuspidal convolution operators are trace class (Gelfand–Piatetski-Shapiro, Donnelly)"
lean  = ["GlobalTheory.Published.CuspTraceClass", "PositivityTheory.Prw.cuspTraceClass_of", "PositivityTheory.Prw.dixmierMalliavinFactorisation_holds"]
uses  = ["thm-dixmier-malliavin"]
order = 10
+++
Let $G = \U(V)$ for a hermitian space over a CM field. For every smooth
compactly supported function $f$ on $G(\A_F)$, the operator $R(f)$ on the
cuspidal subspace $L^2_{\mathrm{cusp}}(G(F)\backslash G(\A_F))$ is of trace
class. The proof writes $f$ as a sum of convolutions
([thm-dixmier-malliavin]).
