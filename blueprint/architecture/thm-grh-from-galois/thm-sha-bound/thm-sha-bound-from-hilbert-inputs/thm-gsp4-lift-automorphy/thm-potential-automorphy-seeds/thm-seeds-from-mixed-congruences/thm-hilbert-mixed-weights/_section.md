+++
id    = "thm-hilbert-mixed-weights"
kind  = "theorem"
title = "Ordinary Hilbert modular forms with mixed weights"
lean  = ["UpperTheory.Esk.mixSeed_of_alt"]
uses  = ["thm-de-rham-abelian-schemes", "thm-hecke-character-wd-above-l", "thm-hc-finiteness-gl",
         "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-brauer-induction-degree-zero",
         "thm-chevalley-congruence-units", "thm-clozel-cohomological", "thm-clozel-purity", "thm-cusp-rapid-decay", "thm-cuspidal-spectrum-gl",
         "thm-p-adic-monodromy", "thm-depth-zero-from-support", "thm-dual-abelian-scheme",
         "thm-shimura-main-theorem-cm", "thm-zelevinsky-segments", "thm-gelfand-kazhdan", "thm-geometric-lemma",
         "thm-artin-reciprocity", "thm-green-regular-characters", "thm-grothendieck-messing",
         "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-functional-equation-cm",
         "thm-singular-moduli-class-number", "thm-jacquet-shalika", "def-galois-cohomology-inputs", "thm-henniart-local-converse", "thm-moy-prasad-jacquet",
         "thm-partial-zeta-functional-equation", "thm-ray-class-field", "thm-siegel-klingen-rationality",
         "thm-square-integrable-segment", "thm-tempered-products", "thm-base-change-unitary"]
order = 10
+++
Assume the inputs of [thm-potential-automorphy-seeds] and *Eisenstein congruences*: for a
totally real field $F$, an odd prime $l$ and a totally odd Hecke character
$\omega$ of finite order, of conductor prime to $l$, nontrivial modulo $l$ at
places in a set $P$ above $l$ and at places outside it, there are cuspidal
Hilbert eigenforms of weight $k + 1$, $k$ arbitrarily large and divisible by
$l - 1$, whose eigenvalues are congruent modulo $l$ to those of an explicit
Eisenstein series.

Let $F$ be a totally real field of even degree in which $l$ splits
completely, $\xi$ a character of $G_F$ of finite order, totally odd,
unramified above $l$, ramified at some place of norm $2$, with $\xi^2 \not\equiv 1$
and $\xi \not\equiv 1$ on each decomposition group above $l$, and $P$ a
proper nonempty set of places above $l$. Then there are $k, t \ge 2$
divisible by $l - 1$, a cuspidal representation $\pi$ of $\GL_2(\A_F)$ and
its Galois representation $r$ with open irreducible image, such that
$\det r = \epsilon^k\xi$, the semisimplified reduction of $r$ is
$1 \oplus \xi$, and at each $w \mid l$, $r$ is ordinary with weights
$(k+t, -t)$ and characters $(\xi, 1)$ if $w \in P$, and with weights $(k, 0)$
and characters $(1, \xi)$ if $w \notin P$, the infinity type of $\pi$
matching.
