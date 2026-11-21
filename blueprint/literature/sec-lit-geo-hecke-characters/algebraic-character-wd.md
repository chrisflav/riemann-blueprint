+++
kind  = "theorem"
title = "Local-global compatibility above l for Hecke characters"
lean  = ["GlobalTheory.Published.AlgebraicCharacterWD", "UpperTheory.Lit.CharWD.algebraicCharacterWD"]
uses  = ["de-rham-potentially-semistable", "global-artin-reciprocity", "hecke-l-adic-character-de-rham"]
order = 3
+++
Let $\chi$ be an algebraic Hecke character of $E$ of type $n$, $w$ a place
above $l$, and $\xi$ the smooth character of $E_w^\times$ that agrees with
$\chi$ on $E^\times$ (the finite part of $\chi_w$). Then the Weil–Deligne
representation attached by Fontaine's functor $D_{\mathrm{pst}}$ to
$r_{\chi,\iota}|_{G_{E_w}}$ is $\iota^{-1}\xi \circ \mathrm{Art}_{E_w}^{-1}$,
the character $\xi$ composed with the local Artin map.

We derive it from Artin reciprocity [global-artin-reciprocity], the de Rham
property [hecke-l-adic-character-de-rham] and Berger's theorem
[de-rham-potentially-semistable].
