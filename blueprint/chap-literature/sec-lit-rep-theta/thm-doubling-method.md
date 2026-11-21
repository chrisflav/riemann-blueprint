+++
kind  = "theorem"
title = "The doubling method"
source = "Piatetski-Shapiro–Rallis [piatetski-shapiro-rallis-1987]"
lean  = ["GlobalTheory.Published.DoublingMethodLocalZetaIntegrals", "ResidueKilled.dm_of_two"]
order = 9
+++
Let $V$ be a hermitian space of positive rank over a CM field, $\mu$ a
unitary Hecke character and $\varphi$ a section of the degenerate principal
series of $\U(V\oplus(-V))$. Then:

* the Siegel Eisenstein series of $\varphi$ continues meromorphically with
  poles of finite order;
* for cusp forms $f_1, f_2$ on $\U(V)$ with a fixed archimedean type
  and $\Re s > \dim V/2$, the doubling integral
  $$
  Z(s, f_1, f_2) = \iint f_1(g_1)\,\overline{f_2(g_2)}\;E\big((g_1, g_2), s\big)\,dg_1\,dg_2
  $$
  satisfies the basic identity, which unfolds it to an integral of a
  matrix coefficient against the section;
* $Z(s, f_1, f_2)$ continues meromorphically.

The statement contains one further clause that is trivially true.
