+++
kind = "proof"
of   = "thm-hecke-character-wd-above-l"
uses = ["thm-chevalley-congruence-units", "thm-fontaine-bcris", "thm-artin-reciprocity", "thm-hecke-l-adic-character-de-rham", "thm-p-adic-monodromy"]
+++
The restriction is de Rham [thm-hecke-l-adic-character-de-rham], so by
Berger's theorem [thm-p-adic-monodromy] it is potentially semistable, and
the monodromy of a character vanishes. By Artin reciprocity
[thm-artin-reciprocity] we know the character on inertia. We compute
$D_{\mathrm{pst}}$ from this description, using
[thm-chevalley-congruence-units] to pass to an open subgroup on which the
global units contribute nothing and the properties of $B_{\mathrm{cris}}$ in
[thm-fontaine-bcris].
