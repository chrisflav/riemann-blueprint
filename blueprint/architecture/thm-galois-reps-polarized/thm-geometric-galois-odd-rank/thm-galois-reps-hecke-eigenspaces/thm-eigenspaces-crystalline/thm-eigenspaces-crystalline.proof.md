+++
kind = "proof"
of   = "thm-eigenspaces-crystalline"
uses = ["thm-etale-finiteness", "thm-fontaine-bcris", "thm-projective-bundle-formula",
        "thm-proper-base-change"]
+++
Since the deck transformations act on $V_\theta$ trivially, $V_\theta$ lies in the
image of the injective pull-back from $H^*(Y_{\bar E_w}, \Q_l)$, compatibly with
Galois. The crystalline comparison theorem for smooth projective schemes over
$\mathcal O_w$ (Fontaine–Messing, Faltings), which the proof derives from a
comparison on the étale side, makes that cohomology crystalline. Subobjects
and graded pieces of crystalline representations are crystalline, by the
properties of $B_{\mathrm{cris}}$. Finiteness comes from [thm-etale-finiteness].
