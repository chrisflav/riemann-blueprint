+++
kind  = "theorem"
title = "Inputs for Hilbert modular forms"
lean  = ["UpperTheory.V.HV.DescentVanishingReductions.published_hypotheses_from_patching_alt"]
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
order = 10
+++
We call *standard inputs* the published results on which the proof of
[thm-sha-bound] rests: the representation theory of $\GL_n$ over $p$-adic
fields (the work of [Bernstein and Zelevinsky](@thm-bz-finiteness),
the [geometric lemma](@thm-geometric-lemma), [Moy–Prasad](@thm-moy-prasad-jacquet),
[Green's characters](@thm-green-regular-characters), the
[local converse theorem](@thm-henniart-local-converse)); automorphic forms on $\GL_n$
([Jacquet–Shalika](@thm-jacquet-shalika), [Clozel's purity theorem](@thm-clozel-purity),
[base change from definite unitary groups](@thm-base-change-unitary)), with the
Galois representations of polarized pairs; Galois cohomology ([def-galois-cohomology-inputs]); and
CM abelian varieties ([the main theorem of complex multiplication](@thm-shimura-main-theorem-cm),
[Siegel–Klingen and Deligne–Ribet](@thm-siegel-klingen-rationality)).

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
