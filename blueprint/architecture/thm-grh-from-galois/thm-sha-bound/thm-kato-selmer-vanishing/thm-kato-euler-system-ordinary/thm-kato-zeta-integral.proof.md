+++
kind = "proof"
of   = "thm-kato-zeta-integral"
uses = ["thm-de-rham-abelian-schemes", "thm-hecke-character-wd-above-l", "thm-hc-finiteness-gl",
        "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-borel-casselman",
        "thm-brauer-induction-degree-zero", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-chevalley-congruence-units", "thm-clozel-cohomological",
        "thm-clozel-purity", "thm-cusp-rapid-decay", "thm-cuspidal-spectrum-gl", "thm-p-adic-monodromy",
        "thm-depth-zero-from-support", "thm-depth-zero-support", "thm-dual-abelian-scheme", "thm-shimura-main-theorem-cm",
        "thm-zelevinsky-segments", "thm-gelfand-kazhdan", "thm-geometric-lemma", "thm-artin-reciprocity",
        "thm-green-regular-characters", "thm-grothendieck-messing", "thm-hc-finiteness-unitary", "thm-hasse-norm-quadratic",
        "thm-hecke-l-adic-character-above-l", "thm-hecke-functional-equation-cm", "thm-singular-moduli-class-number",
        "thm-jacquet-shalika", "def-galois-cohomology-inputs", "thm-henniart-local-converse", "thm-moy-prasad-jacquet",
        "thm-partial-zeta-functional-equation", "thm-ray-class-field", "thm-siegel-klingen-rationality",
        "thm-square-integrable-segment", "thm-tempered-products"]
+++
Take the Kummer classes of Siegel units in the étale cohomology of the tower
of modular curves, cup them in pairs, project to the part cut out by the
Hecke eigenvalues of $g$, and corestrict along $\Q(\mu_{l^r})$. The
distribution relations of Siegel units give norm compatibility, and
integrality comes from the choice of $c, d$. The Euler system relations at
primes $w \equiv 1 \bmod l^n$ come from the same distribution relations,
with [Chebotarev's theorem](@thm-chebotarev-degree-one-frobenius) to choose the primes. The many published
inputs enter through the Galois representations attached to $g$ and their
local properties. *We read* this outline from the statements of the steps.
