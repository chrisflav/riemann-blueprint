+++
kind  = "theorem"
title = "The non-endoscopic hypotheses hold"
lean  = ["GlobalTheory.JoinFun.joinOut_of_five", "GlobalTheory.Mem.LiteralAutomorphy.JoinOut", "UpperTheory.LiteratureTheorems.join_out_of_literature", "UpperTheory.LiteratureTheorems.literature_nonexistence"]
uses  = ["def-local-parameters", "thm-shimura-main-theorem-cm", "thm-hecke-functional-equation-cm", "thm-singular-moduli-class-number", "def-non-endoscopic-package", "thm-partial-zeta-functional-equation", "thm-siegel-klingen-rationality"]
order = 14
+++
Under the hypotheses of [thm-grh-from-sha-bound], with a system of local
parameters ([def-local-parameters]), the non-endoscopic hypotheses
([def-non-endoscopic-package]) hold: the local representation theory of
$\GL_n$, the automorphy and Galois statements, the cohomology statements, the
transport statements for lattices and zeta denominators, and the
functional equation of Hecke $L$-functions ([thm-hecke-functional-equation-cm]).
The proof uses the main theorem of complex multiplication for elliptic
curves ([thm-shimura-main-theorem-cm]), the theorem that $j$ of a CM point
generates the Hilbert class field ([thm-singular-moduli-class-number]), the functional
equation of partial zeta functions ([thm-partial-zeta-functional-equation]),
and the theorem of Siegel–Klingen and Deligne–Ribet
([thm-siegel-klingen-rationality]).
