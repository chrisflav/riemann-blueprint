+++
kind = "proof"
of   = "kato-euler-system-integrality"
uses = ["abelian-de-rham", "algebraic-character-wd", "automorphic-forms-finite-gl",
        "bernstein-unitary-product-irreducible", "bernstein-zelevinsky-finiteness", "borel-casselman",
        "brauer-degree-zero", "cheb", "chebotarev-degree-one", "chevalley-units", "clozel-cohomological",
        "clozel-purity", "cusp-rapid-decay", "cuspidal-spectrum-gl", "de-rham-potentially-semistable",
        "depth-zero-induction", "depth-zero-support", "dual-abelian-scheme", "elliptic-main-theorem-cm",
        "ess-square-integrable-segments", "gelfand-kazhdan-dual", "geometric-lemma", "global-artin-reciprocity",
        "green-regular-characters", "grothendieck-deformation", "harish-chandra-finite", "hasse-norm-st",
        "hecke-l-adic-character-above", "hecke-tate-functional-equation", "hilbert-class-field-j",
        "jacquet-shalika", "lit-coh", "local-converse-gl", "moy-prasad-jacquet-iso",
        "partial-zeta-functional-equation", "ray-class-field-st", "siegel-klingen-deligne-ribet",
        "square-integrable-segment", "tempered-product-of-square-integrable"]
+++
Take the Kummer classes of Siegel units in the étale cohomology of the tower
of modular curves, cup them in pairs, project to the part cut out by the
Hecke eigenvalues of $g$, and corestrict along $\Q(\mu_{l^r})$. The
distribution relations of Siegel units give norm compatibility, and
integrality comes from the choice of $c, d$. The Euler system relations at
primes $w \equiv 1 \bmod l^n$ come from the same distribution relations,
with [Chebotarev's theorem](@cheb) to choose the primes. The many published
inputs enter through the Galois representations attached to $g$ and their
local properties. *We read* this outline from the statements of the steps.
