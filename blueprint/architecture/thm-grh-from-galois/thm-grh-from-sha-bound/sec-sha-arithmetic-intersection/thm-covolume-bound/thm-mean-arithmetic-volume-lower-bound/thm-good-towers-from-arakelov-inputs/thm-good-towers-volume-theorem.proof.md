+++
kind = "proof"
of   = "thm-good-towers-volume-theorem"
uses = ["thm-abelian-variety-torsion-count", "thm-hasse-norm-quadratic", "thm-landherr-cm", "lem-de-rham-hodge-tate-flag-comparison", "thm-unitary-integral-models", "thm-semistable-reduction", "thm-volume-theorem", "thm-arithmetic-intersection-theory", "thm-semi-abelian-hom-extension", "lem-volume-theorem-inputs", "thm-fargues-hodge-tate-sequence"]
+++
Build the tower from the integral models ([thm-unitary-integral-models]) and
the Hodge bundles, using Hasse's and Landherr's norm theorems
([thm-hasse-norm-quadratic], [thm-landherr-cm]) and semistable reduction
([thm-semistable-reduction]) to control the reductions; the inputs of
[lem-volume-theorem-inputs] give the flat realisation. The volume theorem
is [thm-volume-theorem]. Its comparison of de Rham and Hodge–Tate flags comes
from [lem-de-rham-hodge-tate-flag-comparison] and the families of Dieudonné
lattices, the triviality of the flag bundle on the Hodge part from Fargues'
sequence ([thm-fargues-hodge-tate-sequence]), and the geometric bound, the
flat-degree statement and the statement on twisted automorphisms are proved
directly.
