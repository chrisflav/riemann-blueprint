+++
kind  = "theorem"
title = "Green's parametrisation of cuspidal characters"
lean  = ["GlobalTheory.Published.GreenCuspidal", "GlobalTheory.Published.GreenSeriesSt", "PositivityTheory.Prw.greenSeriesSt_of", "PositivityTheory.Stage1.PM.greenCuspidal"]
order = 2
+++
Two forms of Green's theorem (1955) on $\GL_N(\mathbb F_g)$, $g$ prime:

* the cuspidal irreducible characters of $\GL_d(\mathbb F_g)$ are in
  bijection with a set of labels of degree $d$ (Frobenius orbits of regular
  characters, presented through irreducible polynomials), and each has
  degree $\prod_{i=1}^{d-1}(g^i-1)$; this is the statement of Green's
  classification in the architecture chapter, [thm-green-cuspidal];
* there is an injective assignment of irreducible representations of
  $\GL_N(\mathbb F_g)$ to a set of polynomials over $\mathbb F_g$. *It is not
  clear* from the statement which polynomials index which representations;
  *we read* it as Green's parametrisation of all irreducible characters.
