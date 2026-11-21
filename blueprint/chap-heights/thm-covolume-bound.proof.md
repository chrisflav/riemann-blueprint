+++
kind = "proof"
of   = "thm-covolume-bound"
uses = ["thm-mean-arithmetic-volume-lower-bound", "lem-height-lower-bound-deep-covers",
        "thm-abelian-variety-torsion-count", "thm-de-rham-abelian-schemes", "thm-cusp-rapid-decay", "thm-grothendieck-existence", "thm-grothendieck-messing-nilpotent-p", "thm-hasse-norm-quadratic", "thm-jantzen-lowest-alcove", "thm-landherr-cm", "thm-unitary-integral-models", "thm-principal-polarisation-one-section", "thm-principalisation-projective", "thm-dieudonne-theory-oc", "thm-ray-class-field", "thm-semi-abelian-hom-extension", "thm-semistable-reduction", "thm-strong-approximation-su", "thm-mumford-good-metrics", "thm-toroidal-compactification-unitary-lit", "thm-arithmetic-volume-bound", "thm-arithmetic-volume-nef", "thm-arithmetic-intersection-theory", "thm-chow-form", "thm-green-parametrisation", "thm-grothendieck-messing", "thm-kawamata-viehweg", "thm-ohsawa-takegoshi-points", "thm-hodge-bundle-semipositive", "thm-gaga-sections", "thm-angehrn-siu-point-separation", "def-hodge-bundle-inputs", "thm-toroidal-compactification-siegel", "thm-toroidal-compactification-unitary", "thm-green-regular-characters", "thm-fargues-hodge-tate-sequence", "thm-hilbert-samuel-nef", "thm-poincare-lelong-integrated", "thm-principalisation-relative", "thm-hironaka-resolution", "thm-zarhin-trick", "thm-arithmetic-hilbert-samuel-inequalities"]
+++
The proof has two parts: a lower bound for the mean arithmetic volumes of
automorphic line bundles on unitary Shimura varieties
([thm-mean-arithmetic-volume-lower-bound]), and a height argument that turns
this lower bound into the covolume bound.

*The volume bound.* It rests on resolution and principalisation
([thm-hironaka-resolution], [thm-principalisation-relative]), the inverse
Poincaré–Lelong formula ([thm-poincare-lelong-integrated]), the arithmetic
Hilbert–Samuel inequalities and Moriwaki's theorem
([thm-arithmetic-hilbert-samuel-inequalities]), Fargues' exact sequence
([thm-fargues-hodge-tate-sequence]), Zarhin's theorem ([thm-zarhin-trick]) and
Riemann–Roch for nef bundles ([thm-hilbert-samuel-nef]).

*The height argument.* At each member of a family, cover the data by deep
covers built from the automorphic line bundles. The toroidal
compactifications ([thm-toroidal-compactification-siegel],
[thm-toroidal-compactification-unitary]) and seminegativity of the Lie
algebras of semi-abelian schemes ([thm-hodge-bundle-semipositive]) make the
covers good, the theorem of Scholze and Weinstein gives the flat degree, and
Grothendieck's deformation theorem ([thm-grothendieck-messing]) the degree of
the covers. The height lower bound ([lem-height-lower-bound-deep-covers]),
with a bound for the arithmetic self-intersections and injectivity of small
sections, gives a uniform lower bound for heights on the covers; here Green's
regular characters and classification ([thm-green-regular-characters],
[thm-green-parametrisation]), separation of points
([thm-angehrn-siu-point-separation]), arithmetic degrees
([thm-arithmetic-intersection-theory]), the Fubini–Study formula for Chow
heights, Kawamata–Viehweg vanishing ([thm-kawamata-viehweg]), $L^2$
extension ([thm-ohsawa-takegoshi-points]), Serre's holomorphic sections
([thm-gaga-sections]) and Chow forms ([thm-chow-form]) enter. A lower bound
for the lifted lattices, with truncation, the bad set and the bound on
$\lambda$, then gives the covolume bound. The published theorems on Hodge
bundles ([def-hodge-bundle-inputs]) enter through Mumford's proportionality
theorem on toroidal flag bundles, which follows from his theorem on good
metrics ([thm-mumford-good-metrics]). Semistable reduction, the norm
theorems of Hasse and Landherr, multiplication by $n$ on abelian schemes and
Serre's holomorphic sections enter through the toroidal charts.
