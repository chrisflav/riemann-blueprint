+++
kind = "proof"
of   = "thm-family-membership-admissible-data"
uses = ["thm-abelian-variety-torsion-count", "thm-bz-finiteness", "thm-casselman-wallach",
        "thm-gross-cm-curves", "thm-cusp-decay-sobolev", "thm-cusp-rapid-decay",
        "thm-cusp-trace-class", "thm-hc-discrete-series-classification",
        "thm-discrete-series-parametrisation", "thm-discrete-series-exist-cover",
        "thm-discrete-series-exist", "thm-discrete-series-exist-upq", "thm-dixmier-malliavin",
        "thm-doubling-method", "thm-harish-chandra-discrete-series",
        "thm-siegel-weil-outside-weil-range", "thm-flath-unramified", "thm-formal-degree-upq",
        "thm-geometric-lemma", "prop-admissible-data-exist", "thm-artin-reciprocity",
        "thm-green-parametrisation", "thm-hc-analyticity-density", "thm-hc-finiteness-unitary",
        "thm-hc-modules-unitary", "thm-hasse-norm-quadratic", "thm-hecke-l-entire",
        "thm-hecke-l-nonvanishing-line-one", "prop-member-hypotheses-from-literature",
        "thm-landherr-cm", "thm-downward-theta-lift-nonvanishing", "thm-unitary-integral-models",
        "thm-siegel-weil-convergent-doubling", "thm-godement-schur-orthogonality",
        "thm-semistable-reduction", "thm-siegel-eisenstein-continuation",
        "thm-siegel-main-theorem-hermitian", "thm-inner-form-multiplicities-equal",
        "thm-unramified-doubling-gl", "def-trivial-statement", "thm-weber-ray-class-field",
        "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range",
        "thm-rational-test-vectors-theta", "prop-intermediate-constructions-exist",
        "thm-borel-casselman", "thm-depth-zero-support", "thm-geometric-lemma-filtration",
        "thm-jacquet-irreducible-admissible", "thm-hc-finiteness-gl", "thm-labesse-base-change",
        "thm-bernstein-unitary-product", "thm-galois-reps-csd-above-l",
        "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one",
        "thm-galois-reps-polarized-cuspidal", "thm-depth-zero-jacquet-injective",
        "thm-zelevinsky-segments", "thm-tadic-generic-unitary-dual", "thm-tate-global-finiteness",
        "thm-greenberg-wiles", "thm-hecke-l-adic-character-above-l",
        "thm-hecke-character-local-parameter-above-l", "thm-jacquet-shalika",
        "thm-tate-euler-characteristic-global-places", "thm-tate-euler-characteristic-l-adic",
        "thm-tate-local-finiteness", "thm-tate-local-finiteness-padic",
        "thm-tate-local-duality-global-places", "thm-tate-local-duality-l-adic",
        "thm-ray-class-characters-galois", "thm-ray-class-field", "thm-clozel-regular-algebraic",
        "thm-disjoint-support-product-irreducible", "thm-unramified-annihilators",
        "thm-p-adic-monodromy", "thm-tate-global-euler-characteristic",
        "prop-twisting-property-constructed-points", "lem-membership-two-passes",
        "lem-depth-three-to-four"]
+++
The mass ratio (1) is a published input, a form of Siegel's mass formula
([thm-siegel-main-theorem-hermitian]) for the standard lattices. For (2)
and (3) we first prove them for the construction data $p$ with origin $c$,
before imposing $A$.

*Local parameters.* The published inputs used at the members
([prop-member-hypotheses-from-literature]) give local parameters with an
archimedean comparison and a statement on points. Their proof uses Artin
reciprocity [thm-artin-reciprocity], Weber's ray class fields
[thm-weber-ray-class-field], CM elliptic curves with good reduction outside
a prime [thm-gross-cm-curves], Harish-Chandra modules, discrete series and
their formal degrees [thm-formal-degree-upq], and the Siegel–Weil formula.
Rational weights and multiplicity one for the members come from
Harish-Chandra's analyticity theorem [thm-hc-analyticity-density], the
factorisations of Flath [thm-flath-unramified] and of Dixmier–Malliavin
[thm-dixmier-malliavin], the geometric lemma [thm-geometric-lemma], Green's
classification [thm-green-parametrisation], Siegel Eisenstein series
[thm-siegel-eisenstein-continuation], the doubling method
[thm-doubling-method] and Schur orthogonality
[thm-godement-schur-orthogonality], together with the rationality of test
vectors, which we read as [thm-rational-test-vectors-theta].

*Multiplicities.* At every point of the families, let $G_0, G_i$ be inner
forms of the definite unitary groups involved that are isomorphic at the
finite adèles by $\Phi$. Then every irreducible admissible representation
$\sigma$ occurs in the cuspidal spectrum of $G_0$ with the same multiplicity
as $\sigma \circ \Phi^{-1}$ in that of $G_i$
([thm-inner-form-multiplicities-equal]).

*Two choices of norms.* Every starting configuration has a saturated
refinement with no local conditions, and the intermediate constructions
exist by [prop-intermediate-constructions-exist]. A weight-case condition
comes from the residue characters, and a fine adelic datum extends to
larger fields by the covering theorem for discrete series. These give
finiteness and a second, enlarged choice of norms: two choices
$N_g \subseteq N$ such that every choice allowed by $N$ refines the choice
with a Bloch–Kato law, and every choice allowed by $N_g$ is allowed by $N$
and is good. Let $p$ and $p_g$ be their construction data. The local
parameters give depth-three partial constructions for $p$ from every
start; the level-three upgrade holds for $p$ and for $p_g$; partial
constructions for $p$ move with changes of the division data; and at
constructed points for $p$ one can pass to an enlarged base at which
depth-three partial constructions for $p_g$ exist.

*Membership.* Constructed points for $p$ have the twisting property by
[prop-twisting-property-constructed-points], which rests on the Galois
cohomology of Tate and Greenberg–Wiles ([thm-tate-local-duality-l-adic],
[thm-tate-global-euler-characteristic], [thm-greenberg-wiles]). Depth-three
partial constructions extend to depth four, for $p$ and for $p_g$, by
[lem-depth-three-to-four]. Ambient and division data exist for both. Theta
data with all compatibilities exist by the theory of discrete series
([thm-hc-discrete-series-classification],
[thm-discrete-series-parametrisation], [thm-hc-modules-unitary],
[thm-casselman-wallach]) and the Weil representation
[thm-weil-representation-auxiliary-pairs]. Points built for $p_g$ are good
for $p$. Now [lem-membership-two-passes] gives the membership conditions
for the families built from $p$.

*Admissible data.* By [prop-admissible-data-exist], which rests on a
non-vanishing statement for the blocks of the Weil representation, every
good constructed point carries an admissible datum compatible with $p$.

Imposing $A$ keeps membership, because $A$ holds for all large auxiliary
data. The published results used along the way also include Jacquet–Shalika
[thm-jacquet-shalika], Bernstein–Zelevinsky finiteness [thm-bz-finiteness],
base change for definite unitary groups [thm-labesse-base-change], purity
of regular algebraic representations [thm-clozel-regular-algebraic], local
Tate duality [thm-tate-local-duality-l-adic], the local and global Euler
characteristic formulas ([thm-tate-euler-characteristic-l-adic],
[thm-tate-global-euler-characteristic]), the Greenberg–Wiles formula
[thm-greenberg-wiles] and Berger's theorem [thm-p-adic-monodromy].
