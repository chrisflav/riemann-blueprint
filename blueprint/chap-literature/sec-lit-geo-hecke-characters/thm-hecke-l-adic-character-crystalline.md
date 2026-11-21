+++
kind  = "theorem"
title = "The l-adic character is crystalline where the Hecke character is unramified"
lean  = ["GlobalTheory.Published.HeckeLAdicCharacterCrystalline",
         "UpperTheory.Lit.heckeLAdicCharacterCrystalline_of_deRham",
         "UpperTheory.Lit.hecke_ladic_char_crystalline_of_de_rham_pst_wd_llc"]
uses  = ["thm-hecke-character-wd-above-l", "thm-p-adic-monodromy", "def-local-parameters",
         "thm-hecke-l-adic-character-de-rham"]
order = 4
+++
Let $\chi$ be an algebraic Hecke character of $E$ and $w$ a place above $l$
at which $\chi$ is unramified. Then $r_{\chi,\iota}|_{G_{E_w}}$ is
crystalline.

We derive it in two ways: from [thm-hecke-l-adic-character-de-rham],
[thm-p-adic-monodromy] and [thm-hecke-character-wd-above-l] alone, and
from these together with the existence of a system of local parameters
([def-local-parameters]). An unramified $\xi$ gives a Weil–Deligne
representation on which inertia acts trivially, so the potentially
semistable character is crystalline.
