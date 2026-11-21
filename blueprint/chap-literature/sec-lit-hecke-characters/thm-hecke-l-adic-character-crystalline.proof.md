+++
kind = "proof"
of   = "thm-hecke-l-adic-character-crystalline"
uses = ["thm-chevalley-congruence-units", "thm-artin-reciprocity", "thm-hecke-character-wd-above-l", "thm-hecke-l-adic-character-de-rham", "thm-p-adic-monodromy", "def-local-parameters"]
+++
The restriction is de Rham [thm-hecke-l-adic-character-de-rham], hence
potentially semistable by Berger's theorem [thm-p-adic-monodromy]. By
[thm-hecke-character-wd-above-l] its Weil–Deligne representation is
$\xi \circ \mathrm{Art}_{E_w}^{-1}$, which is unramified because $\chi$ is
unramified at $w$; [thm-artin-reciprocity] and
[thm-chevalley-congruence-units] enter through the local Artin map. A
potentially semistable character whose Weil–Deligne representation is
unramified with $N = 0$ is crystalline. We give a second version of the
argument that reads the Weil–Deligne representation through a system of
local parameters ([def-local-parameters]).
