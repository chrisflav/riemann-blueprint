+++
kind = "proof"
of   = "thm-hilbert-mixed-weights"
uses = ["thm-hilbert-modular-inputs", "thm-de-rham-abelian-schemes", "thm-p-adic-monodromy", "thm-dual-abelian-scheme", "def-galois-cohomology-inputs", "thm-base-change-unitary", "thm-borel-casselman", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-geometric-lemma-filtration", "thm-hilbert-weight-change", "thm-jacquet-irreducible-admissible", "thm-local-parameters-exist", "thm-hecke-character-wd-above-l", "thm-hc-finiteness-gl", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-brauer-induction-degree-zero", "thm-chevalley-congruence-units", "thm-clozel-cohomological", "thm-clozel-purity", "thm-cusp-rapid-decay", "thm-cuspidal-spectrum-gl", "thm-depth-zero-from-support", "thm-shimura-main-theorem-cm", "thm-zelevinsky-segments", "thm-gelfand-kazhdan", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-green-regular-characters", "thm-grothendieck-messing", "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-functional-equation-cm", "thm-singular-moduli-class-number", "thm-jacquet-shalika", "thm-henniart-local-converse", "thm-moy-prasad-jacquet", "thm-partial-zeta-functional-equation", "thm-ray-class-field", "thm-siegel-klingen-rationality", "thm-square-integrable-segment", "thm-tempered-products"]
+++
The first step is an *Eisenstein congruence*: for a totally real field $F$,
an odd prime $l$ and a totally odd Hecke character $\omega$ of finite order,
of conductor prime to $l$ and nontrivial modulo $l$ at prescribed places,
there are cuspidal Hilbert eigenforms of weight
$k + 1$, $k$ arbitrarily large and divisible by $l - 1$, whose eigenvalues are
congruent modulo $l$ to those of an explicit Eisenstein series. It follows
from the published theorems on Hilbert Eisenstein series of weight one and
their $q$-expansions, and on Hilbert modular forms of level one and large
weight divisible by $p - 1$ congruent to $1$ modulo $p$ (lifts of the Hasse
invariant). The resulting cusp form has residual representation
$1 \oplus \xi$. Weight change ([thm-hilbert-weight-change]) raises the weight
by $2t$ at the embeddings belonging to $P$ while keeping the congruence and
ordinarity. The Galois representation of the result, from the results of
[thm-hilbert-modular-inputs] and [local parameters](@thm-local-parameters-exist),
has the stated local shape; [Chebotarev's theorem](@thm-chebotarev-degree-one-frobenius)
and the irreducibility of the residual characters give the open image.
