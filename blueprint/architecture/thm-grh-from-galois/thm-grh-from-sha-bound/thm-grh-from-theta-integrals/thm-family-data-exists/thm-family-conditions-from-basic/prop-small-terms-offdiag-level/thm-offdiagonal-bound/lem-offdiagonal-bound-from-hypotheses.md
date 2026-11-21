+++
kind  = "lemma"
title = "The off-diagonal bound from its hypotheses"
lean  = ["Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_closedP",
         "Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_rec2P",
         "Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_rec3P",
         "Formalism.L2.SG.SpectralTiesReal.theoremS_rec",
         "Formalism.L2.SG.TheoremS.pbApplied",
         "Formalism.L2.SG.TheoremSConclusion.theoremS_of_conj"]
uses  = ["prop-archimedean-model-data"]
order = 3
+++
Suppose the following nineteen statements hold: local models at every
place, density inputs, the coefficient identities, the bound on non-generic
terms, the archimedean model data ([prop-archimedean-model-data]), agreement of kernel
exponents, three convergence statements, finiteness, decay of gaps, the
choices of base points, the counting formula, a summation identity, a form
of the mass data, positivity of the mass data, and two compatibilities.
Then there are constants such that for every datum $D$ whose sizes are large
enough, and all types $u \ne u'$ whose large and non-scalar terms are at most
$\varepsilon_D\, d_u d_{u'}/D^*$,
$$|K_0(u,u')|^2 \le (1+b^{-6})\frac{d_u d_{u'}}{D^*}$$
and the same bound holds for a second squared norm $h(u,u')$ of the
pairing, which *we read* as its Hilbert–Schmidt norm.
