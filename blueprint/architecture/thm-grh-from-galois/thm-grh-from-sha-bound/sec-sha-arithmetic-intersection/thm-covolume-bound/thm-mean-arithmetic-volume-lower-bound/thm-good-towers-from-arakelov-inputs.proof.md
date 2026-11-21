+++
kind = "proof"
of   = "thm-good-towers-from-arakelov-inputs"
uses = ["thm-abelian-variety-torsion-count", "lem-volume-theorem-inputs", "lem-flag-cover-pullback", "thm-good-towers-volume-theorem", "thm-arithmetic-intersection-theory", "thm-semi-abelian-hom-extension", "thm-zarhin-trick", "thm-arithmetic-hilbert-samuel-inequalities", "thm-fargues-hodge-tate-sequence", "thm-gaga-sections", "lem-absolute-siegel-lemma"]
+++
We check the hypotheses of [thm-good-towers-volume-theorem]. The inputs of
the volume theorem hold by [lem-volume-theorem-inputs], which uses the
arithmetic intersection theory and resolution in projective space
([thm-arithmetic-intersection-theory]), the arithmetic Hilbert–Samuel
inequalities and Moriwaki's theorem
([thm-arithmetic-hilbert-samuel-inequalities]), extension of homomorphisms of
semi-abelian schemes ([thm-semi-abelian-hom-extension]), Fargues' Hodge–Tate
sequence ([thm-fargues-hodge-tate-sequence]), GAGA for sections
([thm-gaga-sections]) and lines of large degree
([lem-absolute-siegel-lemma]). Fargues' sequence, quotients of abelian
schemes by finite flat group schemes, Zarhin's theorem ([thm-zarhin-trick])
and a statement on ordinary curves give the families of Dieudonné lattices.
The invariance under Galois twists follows from the inputs on flag models,
a comparison statement proved by prime avoidance and resolution, and the
uniformity of theta functions of abelian varieties. Resolution also gives
integrability of Green functions at points. Multiplication by $n$ on
abelian schemes and flag covers ([lem-flag-cover-pullback]) enter along the
way.
