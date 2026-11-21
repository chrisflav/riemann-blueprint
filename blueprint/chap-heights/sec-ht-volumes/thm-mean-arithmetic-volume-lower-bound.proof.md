+++
kind = "proof"
of   = "thm-mean-arithmetic-volume-lower-bound"
uses = ["lem-de-rham-hodge-tate-flag-comparison", "thm-dieudonne-theory-oc", "thm-abelian-variety-torsion-count", "lem-flag-cover-pullback", "thm-good-towers-from-arakelov-inputs", "lem-absolute-siegel-lemma", "thm-unitary-integral-models", "thm-semistable-reduction", "thm-arithmetic-intersection-theory", "thm-fargues-hodge-tate-sequence", "thm-hilbert-samuel-nef", "thm-poincare-lelong-integrated", "thm-principalisation-relative", "thm-hironaka-resolution", "thm-semi-abelian-hom-extension", "thm-zarhin-trick", "thm-arithmetic-hilbert-samuel-inequalities"]
+++
Resolution and principalisation ([thm-hironaka-resolution],
[thm-principalisation-relative]) and the inverse Poincaré–Lelong formula
([thm-poincare-lelong-integrated]) give the arithmetic intersection theory of
[thm-arithmetic-intersection-theory] on the varieties involved. By
[thm-good-towers-from-arakelov-inputs], good towers of flag bundles exist and
the volume theorem holds; its proof uses the arithmetic Hilbert–Samuel
inequalities and Moriwaki's theorem
([thm-arithmetic-hilbert-samuel-inequalities]), Fargues' Hodge–Tate sequence
([thm-fargues-hodge-tate-sequence]), Zarhin's theorem ([thm-zarhin-trick]),
Riemann–Roch for nef bundles ([thm-hilbert-samuel-nef]) and extension of
homomorphisms of semi-abelian schemes ([thm-semi-abelian-hom-extension]), with
[lem-absolute-siegel-lemma], the integral models
of [thm-unitary-integral-models] and covers of flag type
([lem-flag-cover-pullback]). At the finite places the volume theorem needs
the comparison of de Rham and Hodge–Tate flags
([lem-de-rham-hodge-tate-flag-comparison]), whose input comes from
Dieudonné theory over $\mathcal O_C$ ([thm-dieudonne-theory-oc]) through
Fargues' sequence. The mean slope bound of the volume theorem, pulled back
from the tower to $X$, is the claim.
