+++
id    = "seed-i-is-alt"
kind  = "theorem"
title = "Seed points for potential automorphy"
lean  = ["UpperTheory.V.Z.Bc.seedIIs_alt"]
uses  = ["abelian-de-rham", "algebraic-character-wd", "automorphic-forms-finite-gl",
         "bernstein-unitary-product-irreducible", "bernstein-zelevinsky-finiteness", "brauer-degree-zero",
         "chevalley-units", "clozel-cohomological", "clozel-purity", "cusp-rapid-decay", "cuspidal-spectrum-gl",
         "de-rham-potentially-semistable", "depth-zero-induction", "dual-abelian-scheme",
         "elliptic-main-theorem-cm", "ess-square-integrable-segments", "gelfand-kazhdan-dual", "geometric-lemma",
         "global-artin-reciprocity", "green-regular-characters", "grothendieck-deformation",
         "harish-chandra-finite", "hecke-l-adic-character-above", "hecke-tate-functional-equation",
         "hilbert-class-field-j", "jacquet-shalika", "lit-coh", "local-converse-gl", "moy-prasad-jacquet-iso",
         "partial-zeta-functional-equation", "ray-class-field-st", "siegel-klingen-deligne-ribet",
         "square-integrable-segment", "tempered-product-of-square-integrable", "thm-base-change-unitary"]
order = 11
+++
Assume the standard inputs and the inputs for Hilbert modular forms
([published-hypotheses-from-patching-alt]). Let $\bar\rho$ be a residual
representation as in [sp4-in0-alt], and consider a tower of fields of the
kind used for potential automorphy of its lifts, with totally real top field
$F$, deep enough and of the second type. Then, after enlarging the
coefficients, there is a lift of the pseudo-representation of
$\bar\rho|_{G_F}$ that is a *seed*: it is continuous, reduces to
$\bar\rho|_{G_F}$, is attached to an automorphic representation, lies in the
component of the deformation space that the tower prescribes, and its
reduction has nonzero entries at prescribed root positions of
$\mathrm{GSp}_4$.
