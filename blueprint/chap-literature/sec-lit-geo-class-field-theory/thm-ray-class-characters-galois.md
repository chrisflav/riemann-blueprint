+++
kind  = "theorem"
title = "Galois characters from ray class characters"
source = "Artin [artin-1927]; see Neukirch [neukirch-1999]"
lean  = ["GlobalTheory.Published.GlobalArtinReciprocity.rayCharacterArtin", "GlobalTheory.Published.RayCharacterArtin"]
order = 3
+++
Let $F$ be a number field, $\mathfrak m \ne 0$ an ideal of $\mathcal O_F$, $A$
an abelian group and $f$ a homomorphism from the group of fractional ideals
prime to $\mathfrak m$ to $A$ that is trivial on every principal ideal $(x)$
with $x \equiv 1 \bmod \mathfrak m$. Then there is a unique homomorphism
$\varphi : \Gal(\bar F/F) \to A$ with open kernel such that
$\varphi(\mathrm{Frob}_v) = f(v)$ for every prime $v \nmid \mathfrak m$.
Moreover $\varphi$ is unramified outside $\mathfrak m$, and if
$\mathfrak m = v^n \mathfrak n$ with $v \nmid \mathfrak n$, then $\varphi$ of
the inertia group at $v$ is the set of values $f((x))$ with $x$ a $v$-unit
congruent to $1$ modulo $\mathfrak n$.

It is stated for ray class characters, in the "wide" form with no sign
conditions at the real places.
