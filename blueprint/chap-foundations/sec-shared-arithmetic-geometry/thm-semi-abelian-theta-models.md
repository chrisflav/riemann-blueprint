+++
kind  = "theorem"
title = "Semi-abelian models with theta functions"
lean  = ["GlobalTheory.T.semiAbelianScheme_uniformisation_exists_geometric",
         "GlobalTheory.T.zarhinGeometric_of_semistableReduction", "GlobalTheory.ZH.GeoHalf.zhGeo",
         "GlobalTheory.zhGeo_of_semistableReduction"]
uses  = ["thm-semistable-reduction"]
order = 12
+++
Assume Grothendieck's semistable reduction theorem. Let a polarised abelian
variety be given over the generic point of an arithmetic model $Z$, with a
sufficiently large system of theta functions and a lattice of their
coefficients. Then over an open part of $Z$ there is a quasi-projective
semi-abelian scheme $G$ extending it, with a symmetric cubical line bundle
$L$ extending the polarisation, such that:

* $G$ is abelian exactly where the theta system says, and $L$ is relatively
  ample there;
* over every complete noetherian normal local domain of characteristic $0$
  mapping to $Z$ and meeting the abelian locus, $G$ has a Mumford
  uniformisation;
* the theta functions extend to sections of powers of $L$ that give an
  immersion of $G$ into projective space.

*It is not clear* which published theorem this is meant to be; it has the shape
of the theory of degenerations of Mumford and Faltings–Chai.
