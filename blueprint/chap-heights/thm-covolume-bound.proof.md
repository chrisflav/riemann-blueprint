+++
kind = "proof"
of   = "thm-covolume-bound"
uses = ["thm-mean-arithmetic-volume-lower-bound", "thm-arithmetic-hilbert-samuel-inequalities", "lem-height-lower-bound-deep-covers",
        "thm-unitary-integral-models", "thm-mumford-degeneration", "thm-toroidal-compactification-unitary", "thm-toroidal-compactification-siegel", "thm-functorial-resolution",
        "thm-abelian-variety-torsion-count", "thm-de-rham-abelian-schemes", "thm-cusp-rapid-decay", "thm-grothendieck-existence", "thm-hasse-norm-quadratic", "thm-jantzen-lowest-alcove", "thm-landherr-cm", "thm-principal-polarisation-one-section", "thm-principalisation-projective", "thm-dieudonne-theory-oc", "thm-ray-class-field", "thm-semi-abelian-hom-extension", "thm-semistable-reduction", "thm-strong-approximation-su", "thm-mumford-good-metrics", "thm-arithmetic-volume-bound", "thm-arithmetic-volume-nef", "thm-arithmetic-intersection-theory", "thm-chow-form", "thm-green-parametrisation", "thm-grothendieck-messing", "thm-kawamata-viehweg", "thm-ohsawa-takegoshi-points", "thm-hodge-bundle-semipositive", "thm-gaga-sections", "thm-angehrn-siu-point-separation", "def-hodge-bundle-inputs", "thm-green-regular-characters", "thm-fargues-hodge-tate-sequence", "thm-hilbert-samuel-nef", "thm-poincare-lelong-integrated", "thm-principalisation-relative", "thm-hironaka-resolution", "thm-zarhin-trick"]
+++
The proof has three steps.

1. *Volumes.* On the unitary Shimura variety attached to a member of the
   family, the mean over connected components of the slopes
   $\widehat{\mathrm{vol}}/\deg$ of an automorphic line bundle is bounded
   below ([thm-mean-arithmetic-volume-lower-bound]). The proof builds a tower
   of flag bundles over an integral model and applies to its root line
   bundles the arithmetic Hilbert–Samuel inequalities and Moriwaki's theorem
   ([thm-arithmetic-hilbert-samuel-inequalities]).
2. *Heights.* At each member, cover the data by deep covers built from the
   automorphic line bundles. The volume bound gives a uniform lower bound
   for heights on these covers ([lem-height-lower-bound-deep-covers]); the
   sections it needs come from separation of points
   ([thm-angehrn-siu-point-separation]), $L^2$ extension
   ([thm-ohsawa-takegoshi-points]) and Kawamata–Viehweg vanishing
   ([thm-kawamata-viehweg]). Green's regular characters and their
   classification ([thm-green-regular-characters],
   [thm-green-parametrisation]) control the weights, and Chow forms
   ([thm-chow-form]) and arithmetic degrees
   ([thm-arithmetic-intersection-theory]) compute the heights.
3. *Covolumes.* A lower bound for the lifted lattices, with a truncation, a
   bad set and a bound on a parameter $\lambda$, turns the height bound into
   the bound on $\log \mathrm{covol}(M_j)$. *We have not unfolded* this step.

All three steps use the same geometry: integral models of unitary Shimura
varieties inside Siegel moduli ([thm-unitary-integral-models]), Mumford's
degenerating abelian varieties ([thm-mumford-degeneration]), toroidal
compactifications ([thm-toroidal-compactification-unitary],
[thm-toroidal-compactification-siegel]) with seminegativity of the Lie
algebras of semi-abelian schemes ([thm-hodge-bundle-semipositive]), and
resolution of singularities ([thm-functorial-resolution]), through
Hironaka's theorem ([thm-hironaka-resolution]) and principalisation
([thm-principalisation-relative]). Grothendieck's deformation theorem
([thm-grothendieck-messing]) gives the degree of the covers. The published
results on Hodge bundles ([def-hodge-bundle-inputs]) enter through Mumford's
proportionality theorem on toroidal flag bundles, which follows from his
theorem on good metrics ([thm-mumford-good-metrics]).
