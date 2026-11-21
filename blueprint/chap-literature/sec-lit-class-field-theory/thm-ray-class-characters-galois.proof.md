+++
kind = "proof"
of   = "thm-ray-class-characters-galois"
uses = ["thm-artin-reciprocity"]
+++
We pull $f$ back to a character of the ideles that is trivial on $F^\times$,
on the connected component at infinity and on the units congruent to $1$
modulo $\mathfrak m$. By Artin reciprocity [thm-artin-reciprocity] it
factors through the idelic Artin map, which gives $\varphi$ with open
kernel. Uniformisers go to Frobenius elements, which gives
$\varphi(\mathrm{Frob}_v) = f(v)$; uniqueness holds because, by the same
law, these Frobenius elements generate a dense subgroup of the abelianised
Galois group. Local units go onto inertia, which gives
the description of $\varphi$ on inertia and the unramifiedness outside
$\mathfrak m$.
