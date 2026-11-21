+++
kind  = "theorem"
title = "Zelevinsky's classification by segments"
lean  = ["GlobalTheory.Published.EssSquareIntegrableSegments", "GlobalTheory.Published.GenericUnlinkedGL", "GlobalTheory.Published.GrothendieckRingPolynomial", "GlobalTheory.Published.LanglandsExhaustionGL", "GlobalTheory.Published.LanglandsMultisegments", "GlobalTheory.Published.SegmentRepresentation", "GlobalTheory.Published.StandardCosocleGL", "GlobalTheory.RgGu.genericUnlinkedGL_of_segRep2", "PositivityTheory.Exh.essSquareIntegrableSegments_of_seg", "PositivityTheory.Exh.langlandsExhaustionGL_of_seg", "PositivityTheory.Exh.langlandsMultisegments_of_seg", "PositivityTheory.Exh.standardCosocleGL_of_seg", "PositivityTheory.Groth.grothendieckRingPolynomial_of_seg", "PositivityTheory.RgGu.segmentRepresentation", "UpperTheory.GalS.PairUAlt", "UpperTheory.GalS.field_of_starFull_alt"]
uses = ["def-local-parameters"]
order = 8
+++
Let $F$ be a non-archimedean local field of characteristic zero. A *segment*
is a set $\Delta = \{\rho, \rho\nu, \dots, \rho\nu^{l-1}\}$ with $\rho$ an
irreducible cuspidal representation of $\GL_d(F)$ and $\nu = |\det|$; it has
an attached irreducible representation of $\GL_{ld}(F)$, its *segment
representation*. The following hold.

1. An irreducible representation $\delta$ of $\GL_n(F)$, $n \ge 1$, has a
   twist by a character with square-integrable matrix coefficients if and
   only if it is the segment representation of some segment
   (Bernstein–Zelevinsky).
2. For each segment, the product $\rho \times \rho\nu \times \dots \times \rho\nu^{l-1}$
   has a unique irreducible subrepresentation, and its Jacquet module is
   $\rho \otimes \rho\nu \otimes \dots \otimes \rho\nu^{l-1}$ (Zelevinsky, 1980).
3. Every irreducible representation is attached to a multisegment
   (Langlands classification), the multisegment is unique, a product of
   standard modules has the expected irreducible cosocle, and the
   representation attached to $\mathfrak m + \mathfrak n$ is a subquotient of
   the product of those attached to $\mathfrak m$ and $\mathfrak n$.
4. A generic irreducible representation is a product of segment
   representations of pairwise unlinked segments (Zelevinsky, Theorem 9.7).
5. Choosing a segment representation for each segment, the Grothendieck
   ring of all $\GL_n(F)$, $n \ge 0$, with the product given by induction,
   is the polynomial ring over $\Z$ in the segments.

We also record here a global statement: for a CM field $E$, a regular
algebraic cuspidal representation $\pi$ of $\GL_a(\A_E)$ and a Hecke
character $\chi$ of $E^+$ with $\pi^\vee \cong \pi^c \otimes (\chi\circ N)$,
there is a Galois representation attached to $(\pi, \chi)$ with the
properties required in [def-galois-reps-polarized]. This is the existence
of Galois representations for polarized pairs (Harris–Taylor, Shin,
Chenevier–Harris, Caraiani). *We read* its place here as a grouping of
statements; it is not part of the classification.
