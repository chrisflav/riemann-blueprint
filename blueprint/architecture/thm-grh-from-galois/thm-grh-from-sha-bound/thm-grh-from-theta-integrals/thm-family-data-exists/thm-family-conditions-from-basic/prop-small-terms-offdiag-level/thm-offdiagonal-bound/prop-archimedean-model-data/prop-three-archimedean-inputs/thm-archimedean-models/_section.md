+++
id    = "thm-archimedean-models"
kind  = "theorem"
title = "Archimedean models for admissible settings"
lean  = ["Formalism.FourierDecayAlt.JCT.ModelPlaceBuilt2",
         "Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.model_place_built_holds",
         "Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_chartEqs",
         "Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_jf"]
order = 1
+++
There is a constant $C_c$ such that the following holds. Let $E$ be a CM
field with, at each infinite place $v$, finite-dimensional hermitian spaces
$W_p(v), W_q(v)$, a tower of levels and test functions $f_v$ with values in
$\mathrm{Hom}(W_q(v), W_p(v))$, admissible with constant $C_c$ (a list of size and
smoothness conditions). Then at every place $v$ there are level data, model
eigenfunctions $j$ with eigenvalues $\lambda$, and constants $C_m, \sigma > 0$,
such that for every $\varepsilon > 0$ and every admissible word $a$, the
principal hermitian pairing of the test function cut off at $\varepsilon$
equals $C_m$ times the model energy form ([lem-cutoff-energy-limit]) cut off at
$\sigma\varepsilon$, and the sizes of the model match those of the setting.
