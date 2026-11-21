+++
kind = "proof"
of   = "thm-step-identities-from-siegel-weil"
uses = ["prop-theta-integrals-along-towers", "thm-siegel-weil-definite", "thm-eisenstein-continuation-growth", "thm-reduction-theory-unitary",
        "thm-weil-representation-unitary-exists", "thm-hecke-l-entire", "thm-bz-finiteness", "thm-geometric-lemma-filtration",
        "thm-hasse-norm-quadratic"]
+++
The statements of [prop-theta-integrals-along-towers] give matching of local
data for triples, and the constant-term computations of theta integrals. The
Siegel–Weil formula ([thm-siegel-weil-definite]) and the Rallis inner product
formula then give the step constants
$C \cdot L^S(\nu, \tfrac{a - (b+2)}{2} + 1)$, with convergence from the bound
on Siegel Eisenstein series ([thm-eisenstein-continuation-growth]) and
reduction theory on Siegel sets ([thm-reduction-theory-unitary]); the Weil
representation exists by [thm-weil-representation-unitary-exists]. Hecke
$L$-functions do not vanish at $s = 1$ ([thm-hecke-l-entire]), which makes the
constants non-zero.

The argument also needs local statements on the Weil representations of the
dual pairs in theta towers: at finite places, coinvariants are determined by
dictionaries of $K$-types, and $\mathrm{SO}$-coinvariants by $K$-finiteness;
local theta lifts have multiplicity one at ramified places, and the relevant
spaces are finite-dimensional at ramified, split and inert places; spherical
vectors match in triples; and the archimedean Lie algebra statements and the
$K$-type statement at real places hold. These come from Bernstein–Zelevinsky
theory ([thm-bz-finiteness]) and the geometric lemma
([thm-geometric-lemma-filtration]) at finite places, from Howe duality at
inert places, where Hasse's norm theorem ([thm-hasse-norm-quadratic]) also
enters, and from lifting of local theta correspondences at the archimedean
places.
