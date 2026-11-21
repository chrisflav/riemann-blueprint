+++
kind  = "theorem"
title = "Finiteness and duality for parabolic induction (Bernstein–Zelevinsky)"
lean  = ["GlobalTheory.Published.BernsteinZelevinskyFiniteness", "GlobalTheory.Published.TotallyDisjointProductIrreducible", "GlobalTheory.Published.ZelevinskyPolynomialRing", "GlobalTheory.geometricLemma_of_filtration", "PositivityTheory.Geo.geometricLemmaFiltration", "PositivityTheory.Prw.bernsteinZelevinskyFiniteness_holds", "PositivityTheory.Prw.zelevinskyPolynomialRing_of", "PositivityTheory.SlGl.totallyDisjointProductIrreducible_of_parts"]
order = 9
+++
Let $F$ be a non-archimedean local field. For $\GL_n(F)$:

* every irreducible smooth representation is admissible;
* Jacquet functors and parabolic induction, for any ordered block
  decomposition, preserve finite length;
* the contragredient of an induced representation is the representation
  induced from the contragredient, through the pairing
  $\langle f', f\rangle = \int_{K} f'(x)(f(x))\,dx$ over the maximal compact
  subgroup $K = \GL_n(\mathcal O)$.

This is Bernstein–Zelevinsky (1976, 1977). We also record here the
Zelevinsky polynomial ring of [thm-zelevinsky-segments], the
geometric lemma ([thm-geometric-lemma-filtration], [thm-geometric-lemma]) and the
irreducibility of $\pi_1 \times \pi_2$ when no cuspidal constituent of $\pi_1$
equals one of $\pi_2$ up to the twists $\nu^{j}$, $|j| \le 1$.
