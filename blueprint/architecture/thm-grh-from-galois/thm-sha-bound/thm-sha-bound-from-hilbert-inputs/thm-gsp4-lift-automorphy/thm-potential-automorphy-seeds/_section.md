+++
id    = "thm-potential-automorphy-seeds"
kind  = "theorem"
title = "Seed points for potential automorphy"
lean  = ["UpperTheory.V.Z.Bc.seedIIs_alt"]
uses  = ["thm-de-rham-abelian-schemes", "thm-hecke-character-wd-above-l", "thm-hc-finiteness-gl",
         "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-brauer-induction-degree-zero",
         "thm-chevalley-congruence-units", "thm-clozel-cohomological", "thm-clozel-purity", "thm-cusp-rapid-decay", "thm-cuspidal-spectrum-gl",
         "thm-p-adic-monodromy", "thm-depth-zero-from-support", "thm-dual-abelian-scheme",
         "thm-shimura-main-theorem-cm", "thm-zelevinsky-segments", "thm-gelfand-kazhdan", "thm-geometric-lemma",
         "thm-artin-reciprocity", "thm-green-regular-characters", "thm-grothendieck-messing",
         "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-functional-equation-cm",
         "thm-singular-moduli-class-number", "thm-jacquet-shalika", "def-galois-cohomology-inputs", "thm-henniart-local-converse", "thm-moy-prasad-jacquet",
         "thm-partial-zeta-functional-equation", "thm-ray-class-field", "thm-siegel-klingen-rationality",
         "thm-square-integrable-segment", "thm-tempered-products", "thm-base-change-unitary"]
order = 11
+++
Assume the standard inputs and the inputs for Hilbert modular forms
([thm-hilbert-modular-inputs]). Let $\bar\rho$ be a residual
representation as in [thm-gsp4-lift-automorphy], and consider a tower of fields of the
kind used for potential automorphy of its lifts, with totally real top field
$F$, deep enough and of the second type. Then, after enlarging the
coefficients, there is a lift of the pseudo-representation of
$\bar\rho|_{G_F}$ that is a *seed*: it is continuous, reduces to
$\bar\rho|_{G_F}$, is attached to an automorphic representation, lies in the
component of the deformation space that the tower prescribes, and its
reduction has nonzero entries at prescribed root positions of
$\mathrm{GSp}_4$.
