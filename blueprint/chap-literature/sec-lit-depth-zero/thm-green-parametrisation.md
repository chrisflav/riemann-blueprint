+++
kind  = "theorem"
title = "Green's parametrisation of cuspidal characters"
provenance = "published"
source = "Green [green-1955]"
lean  = ["GlobalTheory.Published.GreenCuspidal", "GlobalTheory.Published.GreenSeriesSt", "PositivityTheory.Prw.greenSeriesSt_of", "PositivityTheory.Stage1.PM.greenCuspidal",
         "GlobalTheory.GLq.Green"]
order = 7
+++
Two forms of Green's theorem on $\GL_N(\mathbb F_g)$, $g$ prime:

* the cuspidal irreducible characters of $\GL_d(\mathbb F_g)$ are in
  bijection with a set of labels of degree $d$ (Frobenius orbits of regular
  characters of $\mathbb F_{g^d}^\times$, presented through irreducible
  polynomials), and each has degree $\prod_{i=1}^{d-1}(g^i-1)$; the
  character values are those of [thm-green-regular-characters];
* there is an injective assignment of irreducible representations of
  $\GL_N(\mathbb F_g)$ to a set of polynomials over $\mathbb F_g$. *It is not
  clear* from the statement which polynomials index which representations;
  *we read* it as Green's parametrisation of all irreducible characters.
