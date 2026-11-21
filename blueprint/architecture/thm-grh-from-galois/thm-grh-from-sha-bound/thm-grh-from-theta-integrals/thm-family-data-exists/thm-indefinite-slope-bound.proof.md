+++
kind = "proof"
of   = "thm-indefinite-slope-bound"
uses = ["thm-bz-finiteness", "thm-casselman-wallach", "thm-cusp-rapid-decay", "thm-discrete-series-parametrisation", "thm-discrete-series-exist", "thm-discrete-series-exist-upq", "thm-doubling-method", "thm-geometric-lemma-filtration", "thm-artin-reciprocity", "thm-hc-modules-unitary", "thm-hasse-norm-quadratic", "thm-howe-duality-archimedean-trivial", "thm-siegel-weil-convergent-doubling", "thm-oscillator-lie-action", "thm-reduction-theory-unitary", "thm-square-term-estimates", "thm-rational-test-vectors-theta", "thm-unramified-doubling-gl", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range", "thm-hecke-functional-equation-cm", "thm-theta-tower-step-identities", "thm-non-endoscopic-hypotheses-hold", "thm-theta-functionals-separate", "thm-twisting-index-and-archimedean-bounds", "thm-chowla-selberg"]
+++
Besides the step identities of theta towers
([thm-theta-tower-step-identities]) and the
[functional equation of Hecke $L$-functions](@thm-hecke-functional-equation-cm),
the proof uses five arithmetic statements on $L$-values, proved in
[thm-non-endoscopic-hypotheses-hold]: denominators of toric periods, a
transport of lattice norms and its twisted form, denominators of zeta
values, and the reflection
$\Lambda(s)\Lambda_0(1-s) = \varepsilon\,\Lambda(1-s)\Lambda_0(s)$ with
$\varepsilon$ a unit away from a fixed set of primes, for
$1 - e_0 \le s \le 0$.

The estimates on the leading square term ([thm-square-term-estimates])
give the bounds on $L$-values and the Witt tower identity. The rational
test vectors of [thm-rational-test-vectors-theta] give finite rational sums
with nonzero constants. Separation
([thm-theta-functionals-separate]) makes the test
functionals injective. A size bound at all places (at the infinite places
through the mean of the periods given by the Chowla–Selberg formula,
[thm-chowla-selberg]), a bound
$|L'/L(1,\chi)| \le x^{\varepsilon}$, toric ratio estimates, the
rationality of the square ratios and the archimedean lower bound of
[thm-twisting-index-and-archimedean-bounds] then give a function on the grid
of evaluation points with the required properties. A scaling bound turns it
into the slope inequality at the point $0$ of the grid.
