+++
kind = "proof"
of   = "thm-family-membership-admissible-data"
uses = ["thm-abelian-variety-torsion-count", "thm-bz-finiteness", "thm-casselman-wallach", "thm-gross-cm-curves", "thm-cusp-decay-sobolev", "thm-cusp-rapid-decay", "thm-cusp-trace-class", "thm-hc-discrete-series-classification", "thm-discrete-series-parametrisation", "thm-discrete-series-exist-cover", "thm-discrete-series-exist", "thm-discrete-series-exist-upq", "thm-dixmier-malliavin", "thm-doubling-method", "thm-harish-chandra-discrete-series", "thm-siegel-weil-outside-weil-range", "thm-flath-unramified", "thm-formal-degree-upq", "thm-geometric-lemma", "prop-admissible-data-exist", "thm-artin-reciprocity", "thm-green-parametrisation", "thm-hc-analyticity-density", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary", "thm-hasse-norm-quadratic", "thm-hecke-l-entire", "thm-hecke-l-nonvanishing-line-one", "prop-member-hypotheses-from-literature", "thm-landherr-cm", "thm-downward-theta-lift-nonvanishing", "thm-membership-with-origin", "thm-unitary-integral-models", "thm-siegel-weil-convergent-doubling", "thm-godement-schur-orthogonality", "thm-semistable-reduction", "thm-siegel-eisenstein-continuation", "thm-siegel-main-theorem-hermitian", "thm-inner-form-multiplicities-equal", "thm-unramified-doubling-gl", "def-trivial-statement", "thm-weber-ray-class-field", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range", "thm-rational-test-vectors-theta"]
+++
The mass ratio (1) is a published input, a form of Siegel's mass formula
([thm-siegel-main-theorem-hermitian]) for the standard lattices. For
membership we apply [thm-membership-with-origin]. The published inputs
used at the members ([prop-member-hypotheses-from-literature]) give local
parameters with the archimedean comparison and the statement on points
that it asks for. Its proof uses Artin reciprocity [thm-artin-reciprocity],
Weber's ray class fields [thm-weber-ray-class-field], CM elliptic curves
with good reduction outside a prime [thm-gross-cm-curves], Harish-Chandra
modules, discrete series and their formal degrees [thm-formal-degree-upq],
and the Siegel–Weil formula. Rational weights and multiplicity one for the
members come from Harish-Chandra's analyticity theorem
[thm-hc-analyticity-density], the factorisations of Flath
[thm-flath-unramified] and of Dixmier–Malliavin [thm-dixmier-malliavin],
the geometric lemma [thm-geometric-lemma], Green's classification
[thm-green-parametrisation], Siegel Eisenstein series
[thm-siegel-eisenstein-continuation], the doubling method
[thm-doubling-method] and Schur orthogonality
[thm-godement-schur-orthogonality], together with the rationality of test
vectors, which we read as [thm-rational-test-vectors-theta]. The
multiplicity condition of [thm-membership-with-origin] is
[thm-inner-form-multiplicities-equal]. This gives membership for the data
with origin $c$. Imposing $A$ keeps membership, because $A$ holds for all
large auxiliary data. A non-vanishing statement for the blocks of the Weil
representation gives the admissible data.
