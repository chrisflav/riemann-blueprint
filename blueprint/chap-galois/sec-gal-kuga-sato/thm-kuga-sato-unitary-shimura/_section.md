+++
id    = "thm-kuga-sato-unitary-shimura"
kind  = "theorem"
title = "Kuga–Sato varieties over unitary Shimura varieties"
provenance = "new"
lean  = ["UpperTheory.Gal.Int.Geo.kodaira_spencer_of_weight_one"]
order = 1
+++
Let $G$ be a unitary group of odd rank $n$ over a CM field $F$, of signature
$(1, n-1)$ at one infinite place and $(0, n)$ at the others, attached to a PEL
datum of the kind used by Harris and Taylor with compact Shimura varieties.
For $k \ge 0$ let the *Kuga–Sato variety* of level $N$ be the $k$-fold fibre power of
the universal abelian scheme over the Shimura variety of level $N$. Then:

* the Shimura varieties have models over $F$, and for every $k$ the Kuga–Sato
  varieties with their Hecke correspondences form a Hecke tower
  ([thm-galois-reps-hecke-eigenspaces]): smooth, projective, with finite étale correspondences;
* they have good reduction at the places where the level is prime to the
  residue characteristic, with the deck group of a cover acting by Hecke
  correspondences, as [thm-eigenspaces-crystalline] requires;
* at such places the Eichler–Shimura congruence relation holds: the Hecke
  operators $T_0, \dots, T_n$ at the place give a polynomial killing Frobenius;
* for every dominant weight $\lambda$ there is $k$ such that, for every Hecke
  eigensystem $\theta$ occurring in automorphic forms of weight $\lambda$ on $G$,
  the $\theta$-eigenspace of $H^*(\Omega^h)$ of the Kuga–Sato variety is non-zero
  for each of the Hodge exponents $h$ that $\lambda$ predicts.
