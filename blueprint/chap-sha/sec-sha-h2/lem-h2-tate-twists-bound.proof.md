+++
kind = "proof"
of   = "lem-h2-tate-twists-bound"
uses = ["thm-hilbert-modular-inputs", "thm-de-rham-abelian-schemes", "thm-p-adic-monodromy", "thm-dual-abelian-scheme", "def-galois-cohomology-inputs", "thm-base-change-unitary", "thm-borel-type-rank-bound", "thm-chebotarev-degree-one", "thm-tate-local-finiteness", "thm-tate-local-duality-global-places", "thm-poitou-tate", "thm-hecke-character-wd-above-l", "thm-hc-finiteness-gl", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-brauer-induction-degree-zero", "thm-chevalley-congruence-units", "thm-clozel-cohomological", "thm-clozel-purity", "thm-cusp-rapid-decay", "thm-cuspidal-spectrum-gl", "thm-depth-zero-from-support", "thm-shimura-main-theorem-cm", "thm-zelevinsky-segments", "thm-gelfand-kazhdan", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-green-regular-characters", "thm-grothendieck-messing", "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-functional-equation-cm", "thm-singular-moduli-class-number", "thm-jacquet-shalika", "thm-henniart-local-converse", "thm-moy-prasad-jacquet", "thm-partial-zeta-functional-equation", "thm-ray-class-field", "thm-siegel-klingen-rationality", "thm-square-integrable-segment", "thm-tempered-products"]
+++
Cycles of cyclic subgroups give classes in the homology of
$\GL_n(\mathcal O_L)$. Reduced at primes of $L$, they are detected by explicit
cocycles on $\GL_n$ of finite fields, which take the value
$x^{e+1}v(g)$ on the class of an element of order $q$ twisted by $x$. *We
read* this as a form of Soulé's comparison between the homology of
$\GL_n(\mathcal O_L)$ and Galois cohomology of Tate twists. The rank bound of
Borel type ([thm-borel-type-rank-bound]) limits how many independent classes there are;
[Chebotarev's theorem](@thm-chebotarev-degree-one) supplies primes of degree one
at which to reduce. The [Poitou–Tate sequence](@thm-poitou-tate),
[local Tate duality](@thm-tate-local-duality-global-places) and [local finiteness](@thm-tate-local-finiteness)
turn the result into the bound on $H^2$.
