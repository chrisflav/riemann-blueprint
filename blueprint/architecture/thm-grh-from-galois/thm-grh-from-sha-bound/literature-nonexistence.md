+++
kind  = "theorem"
title = "The non-endoscopic hypotheses hold"
lean  = ["GlobalTheory.JoinFun.joinOut_of_five", "GlobalTheory.Mem.LiteralAutomorphy.JoinOut", "UpperTheory.LiteratureTheorems.join_out_of_literature", "UpperTheory.LiteratureTheorems.literature_nonexistence"]
uses  = ["def-local-parameters", "elliptic-main-theorem-cm", "hecke-tate-functional-equation", "hilbert-class-field-j", "non-endoscopic-hypotheses-alt", "partial-zeta-functional-equation", "siegel-klingen-deligne-ribet"]
order = 14
+++
Under the hypotheses of [thm-grh-from-sha-bound], with a system of local
parameters ([def-local-parameters]), the non-endoscopic hypotheses
([non-endoscopic-hypotheses-alt]) hold: the local representation theory of
$\GL_n$, the automorphy and Galois statements, the cohomology statements, the
transport statements for lattices and zeta denominators, and the
functional equation of Hecke $L$-functions ([hecke-tate-functional-equation]).
The proof uses the main theorem of complex multiplication for elliptic
curves ([elliptic-main-theorem-cm]), the theorem that $j$ of a CM point
generates the Hilbert class field ([hilbert-class-field-j]), the functional
equation of partial zeta functions ([partial-zeta-functional-equation]),
and the theorem of Siegel–Klingen and Deligne–Ribet
([siegel-klingen-deligne-ribet]).
