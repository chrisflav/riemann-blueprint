+++
kind  = "theorem"
title = "Complex abelian varieties as tori with theta functions"
provenance = "published"
source = "Appell, Humbert, Riemann; see Mumford [mumford-1970]"
lean  = ["ReciprocityTheory.ChartRestriction.G.Geo.Tor.ThetaUnifAV", "GlobalTheory.thetaUnifAV_all",
         "GlobalTheory.thetaUnifAV_of_laws"]
order = 13
+++
Let $A$ be a principally polarised abelian variety of dimension $g$ over $\C$,
with polarisation $L$ rigidified at the origin. Then there are a lattice
$\Lambda \subset \C^g$, a holomorphic uniformisation
$\C^g/\Lambda \cong A(\C)$ whose differential at $0$ identifies $\C^g$ with
the tangent space, a positive definite hermitian form $H$ on $\C^g$ and a
semicharacter $\chi$ of $\Lambda$ (the Appell–Humbert data of $L$), such that:

* every endomorphism of $A$ lifts to a $\C$-linear map of $\C^g$;
* for every $n$, sections of $L^n$ correspond bijectively to theta functions
  of type $(nH, \chi^n)$;
* $E = \Im H$ takes integer values on $\Lambda$ and is a perfect pairing there;
* for $k > 0$ and $a, b \in \Lambda$, the Weil pairing of the $k$-torsion
  points $a/k$ and $b/k$ is $\exp(-2\pi i\, E(a, b)/k)$.
