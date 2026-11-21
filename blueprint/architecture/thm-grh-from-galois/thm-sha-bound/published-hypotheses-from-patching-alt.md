+++
kind  = "theorem"
title = "Inputs for Hilbert modular forms"
lean  = ["UpperTheory.V.HV.DescentVanishingReductions.published_hypotheses_from_patching_alt"]
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
order = 10
+++
We call *standard inputs* the published results on which the proof of
[thm-sha-bound] rests: the representation theory of $\GL_n$ over $p$-adic
fields (the work of [Bernstein and Zelevinsky](@bernstein-zelevinsky-finiteness),
the [geometric lemma](@geometric-lemma), [Moy–Prasad](@moy-prasad-jacquet-iso),
[Green's characters](@green-regular-characters), the
[local converse theorem](@local-converse-gl)); automorphic forms on $\GL_n$
([Jacquet–Shalika](@jacquet-shalika), [Clozel's purity theorem](@clozel-purity),
[base change from definite unitary groups](@thm-base-change-unitary)), with the
Galois representations of polarized pairs; Galois cohomology ([lit-coh]); and
CM abelian varieties ([the main theorem of complex multiplication](@elliptic-main-theorem-cm),
[Siegel–Klingen and Deligne–Ribet](@siegel-klingen-deligne-ribet)).

Assume the standard inputs and *weak descent*: if $E$ is a CM field with
$E/E^+$ unramified at the finite places, every regular algebraic conjugate
self-dual cuspidal representation $\pi$ of $\GL_n(\A_E)$, $2 \le n \le 4$,
unramified away from a finite set of places of $E^+$ that split in $E$, has an
automorphic representation of a unitary group, unramified at the non-split
places, whose components at almost all split places have the Satake parameters
of $\pi$. Then the *inputs for Hilbert modular forms* hold:

* regular algebraic cuspidal representations over CM fields are cohomological,
  their $\mathrm{Aut}(\C)$-conjugates are again cuspidal (Clozel), and their
  number at a given level is at most a dimension of cohomology (Borel);
* every regular algebraic polarized cuspidal representation of $\GL_2$ over a
  totally real field has a Galois representation;
* strong multiplicity one, admissibility, Gelfand–Kazhdan duality and
  semisimplicity of cusp forms for $\GL_n$ over totally real fields;
* quadratic base change from totally real to totally imaginary fields, and
  cyclic base change of prime degree;
* every newform of weight $k \ge 2$ gives a cuspidal representation of
  $\GL_2(\A_\Q)$ with the same Hecke polynomials;
* weak descent itself, and descent from quadratic extensions in rank two;
* every totally real field of even degree carries a totally definite
  quaternion algebra.
