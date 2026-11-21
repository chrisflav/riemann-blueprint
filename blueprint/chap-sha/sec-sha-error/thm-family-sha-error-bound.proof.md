+++
kind = "proof"
of   = "thm-family-sha-error-bound"
uses = ["thm-borel-casselman", "thm-cusp-bounded-gl", "thm-discrete-series-exist-upq",
        "thm-doubling-method", "thm-fontaine-bcris", "thm-geometric-lemma-filtration",
        "thm-hasse-norm-quadratic", "thm-hecke-l-nonvanishing-line-one", "thm-hodge-tate-count",
        "thm-jacquet-irreducible-admissible", "thm-jacquet-shalika-strong-mult-one",
        "thm-bz-derivative-leibniz", "thm-downward-theta-lift-nonvanishing",
        "thm-inner-form-multiplicities-equal", "thm-unramified-doubling-gl",
        "thm-weil-representation-unitary-exists", "thm-siegel-weil-weil-range",
        "thm-hc-finiteness-gl", "thm-labesse-base-change", "thm-bernstein-unitary-product",
        "thm-bz-finiteness", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal",
        "thm-depth-zero-jacquet-injective", "thm-depth-zero-support", "thm-zelevinsky-segments",
        "thm-tadic-generic-unitary-dual", "thm-geometric-lemma", "thm-artin-reciprocity",
        "thm-green-parametrisation", "thm-hc-finiteness-unitary",
        "thm-hecke-l-adic-character-above-l", "thm-hecke-character-local-parameter-above-l",
        "thm-jacquet-shalika", "thm-tate-euler-characteristic-global-places",
        "thm-tate-local-finiteness", "thm-tate-local-duality-global-places",
        "thm-ray-class-characters-galois", "thm-ray-class-field", "thm-clozel-regular-algebraic",
        "thm-disjoint-support-product-irreducible", "thm-p-adic-monodromy",
        "def-theta-analytic-inputs", "def-padic-hodge-package",
        "prop-hecke-integrality-transformation", "thm-chevalley-congruence-units",
        "thm-green-regular-characters", "thm-bloch-kato-local", "thm-bhatt-scholze-crystalline-lattices", "prop-congruence-bounds-all-primes",
        "prop-congruence-bound-auxiliary-primes", "thm-congruence-module-selmer-bound"]
+++
We first check three conditions on the members, then sum local bounds.

1. *Cutting.* Every member can be cut down to its good eigensystems: at
   each local datum there is a Hecke-equivariant endomorphism of its space
   of forms that acts by a fixed nonzero integer on the good eigensystems
   and by $0$ on the others, and the conditions below survive the cut. This
   follows from Chebotarev's density theorem
   ([thm-chebotarev-degree-one]), local finiteness
   ([thm-tate-local-finiteness]), local Tate duality
   ([thm-tate-local-duality-global-places]) and the Euler characteristic
   formula ([thm-tate-euler-characteristic-global-places]).
2. *Galois conditions.* From some scale on, every member satisfies about
   twenty conditions on its Galois representations: residual
   irreducibility, admissible tame eigenvalues, weight and block
   parameters, depth-zero conditions at the unramified places, uniqueness
   of localisation, and others. They come from the $l$-adic Hodge theory of
   [def-padic-hodge-package], the analytic inputs of
   [def-theta-analytic-inputs], the depth-zero support theorem
   ([thm-depth-zero-support]), the integrality of the Hecke series of the
   members, which we read as [prop-hecke-integrality-transformation], and
   the local parameters: the representations $\rho_\pi$ are built by the
   doubling method ([thm-doubling-method]) and the non-vanishing of theta
   lifts ([thm-downward-theta-lift-nonvanishing]), separated by twisted
   multiplicity one ([thm-inner-form-multiplicities-equal]) and
   Jacquet–Shalika rigidity ([thm-jacquet-shalika]), and controlled above
   $l$ by Fontaine's crystalline period ring ([thm-fontaine-bcris]).
3. *Character conditions.* The results on representations of $\GL_n$ over
   local fields, with [global Artin reciprocity](@thm-artin-reciprocity)
   and the depth-zero support theorem, give the character conditions at the
   two auxiliary primes $g_0, g_1$ of every member: at the places above
   $g_k$ the relevant characters have eigenvalues $u$ and $u^{-1}$ at a
   place and its conjugate. Together with the Galois conditions, these pass
   to the classes of families.

Now the error $\eta_j$ of the $j$-th member is a weighted sum, over the
twisted places $w$, of the errors $\eta_i$ of the local data at $w$. Cut
every member to its good eigensystems. At the auxiliary primes $g_0, g_1$,
[prop-congruence-bound-auxiliary-primes] bounds $\eta_i$. At the primes $2$
and $3$ we use the hypothesis. At every other prime,
[prop-congruence-bounds-all-primes] bounds the congruence valuations
$\delta_\pi$ by $s_\pi + V_l + v_l(h_E)$ plus small errors, and bounds
$s_\pi$. Summing over local data, with the multiplicities bounded by the
ranks, gives the bound of [def-sha-error-term]. The summation uses
[local Tate duality](@thm-tate-local-duality-global-places), the
[Euler characteristic formula](@thm-tate-euler-characteristic-global-places),
[Chebotarev's theorem](@thm-chebotarev-degree-one), Fontaine's
period ring and a global index theorem for lattices
([thm-congruence-module-selmer-bound]).

Along the way the proof also uses the Borel–Casselman theorem
[thm-borel-casselman], Chevalley's unit theorem
[thm-chevalley-congruence-units], the boundedness of cusp forms
[thm-cusp-bounded-gl], Green's regular characters
[thm-green-regular-characters] and the $p$-adic monodromy theorem
[thm-p-adic-monodromy].
