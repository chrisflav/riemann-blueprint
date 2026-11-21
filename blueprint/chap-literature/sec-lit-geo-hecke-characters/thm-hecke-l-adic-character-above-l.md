+++
kind  = "theorem"
title = "The l-adic character at the places above l"
lean  = ["GlobalTheory.HeckeAboveBridge.heckeLAdicCharacterAbove_of_potSemistable", "GlobalTheory.Published.HeckeLAdicCharacterAbove"]
uses  = ["thm-p-adic-monodromy", "thm-hecke-l-adic-character-crystalline", "thm-hecke-l-adic-character-de-rham"]
order = 5
+++
Let $\chi$ be an algebraic Hecke character of $E$ of type $n$ and $w$ a
place above $l$. Then $r_{\chi,\iota}|_{G_{E_w}}$ is de Rham with Hodge–Tate
weight $-n_{\iota\tau}$ at each $\tau$, potentially crystalline, and
crystalline if $\chi$ is unramified at $w$.

This collects [thm-hecke-l-adic-character-de-rham] and
[thm-hecke-l-adic-character-crystalline]; potential crystallinity follows from
Berger's theorem [thm-p-adic-monodromy], since the monodromy of a
character vanishes.
