+++
kind = "proof"
of   = "thm-offdiagonal-bound"
uses = ["prop-archimedean-model-data", "prop-offdiagonal-hypotheses-hold",
        "thm-siegel-main-theorem-hermitian", "thm-hc-finiteness-unitary"]
+++
The core is an abstract bound on a pairing over a CM field. Split
$K_0(u,u')$ into large, non-scalar, non-generic and remaining terms. If the
first three are small, the local model, the energy identity and the
densities bound the rest by $(1+b^{-6})\,d_u d_{u'}/D^*$; the same bound
then holds for a second squared norm $h(u,u')$ of the pairing, which *we
read* as its Hilbert–Schmidt norm.

This abstract bound needs nineteen inputs: local models at every place,
density inputs, the coefficient identities, the bound on non-generic terms,
the archimedean model data ([prop-archimedean-model-data]), agreement of
kernel exponents, three convergence statements, finiteness, decay of gaps,
the choices of base points, the counting formula, a summation identity, a
form of the mass data, positivity of the mass data, and two
compatibilities. They hold by [prop-offdiagonal-hypotheses-hold], which
uses the archimedean model data, the bound on non-generic terms, the
finite-dimensionality of spaces of automorphic forms
([thm-hc-finiteness-unitary]), uniqueness of Bessel models with a large gap
and the mass data that the Siegel–Weil formula
([thm-siegel-main-theorem-hermitian]) gives. So there are constants such
that the bound holds for every datum $D$ whose sizes are large enough and
all types $u \ne u'$ whose large and non-scalar terms are at most
$\varepsilon_D\, d_u d_{u'}/D^*$. It remains to check that the chosen data
of the class meet these size and threshold hypotheses; the rank conditions
and the small-terms bound give this.
