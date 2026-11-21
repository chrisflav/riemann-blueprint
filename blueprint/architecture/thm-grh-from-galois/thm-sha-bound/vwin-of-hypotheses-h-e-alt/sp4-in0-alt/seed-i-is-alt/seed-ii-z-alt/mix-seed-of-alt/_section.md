+++
id    = "mix-seed-of-alt"
kind  = "theorem"
title = "Ordinary Hilbert modular forms with mixed weights"
lean  = ["UpperTheory.Esk.mixSeed_of_alt"]
uses  = ["abelian-de-rham", "algebraic-character-wd", "automorphic-forms-finite-gl",
         "bernstein-unitary-product-irreducible", "bernstein-zelevinsky-finiteness", "brauer-degree-zero",
         "chevalley-units", "clozel-cohomological", "clozel-purity", "cusp-rapid-decay", "cuspidal-spectrum-gl",
         "de-rham-potentially-semistable", "depth-zero-induction", "dual-abelian-scheme",
         "elliptic-main-theorem-cm", "ess-square-integrable-segments", "gelfand-kazhdan-dual", "geometric-lemma",
         "global-artin-reciprocity", "green-regular-characters", "grothendieck-deformation",
         "harish-chandra-finite", "hecke-l-adic-character-above", "hecke-tate-functional-equation",
         "hilbert-class-field-j", "jacquet-shalika", "lit-coh", "local-converse-gl", "moy-prasad-jacquet-iso",
         "partial-zeta-functional-equation", "ray-class-field-st", "siegel-klingen-deligne-ribet",
         "square-integrable-segment", "tempered-product-of-square-integrable", "thm-base-change-unitary"]
order = 10
+++
Assume the inputs of [seed-i-is-alt] and *Eisenstein congruences*: for a
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
