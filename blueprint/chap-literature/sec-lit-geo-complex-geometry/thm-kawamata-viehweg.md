+++
kind  = "theorem"
title = "Kawamata–Viehweg vanishing"
source = "Kawamata [kawamata-1982]; Viehweg [viehweg-1982]"
lean  = ["GlobalTheory.KVFromPair.kawamataViehweg_of_nadelVanishingPair", "GlobalTheory.Published.KawamataViehweg",
         "GlobalTheory.Published.NadelVanishingAndNonKltDivisor", "GlobalTheory.Published.NefNumerics",
         "GlobalTheory.nefNumerics_outright", "NadelVanishingSeparation.NSI.nadelVanishingAndNonKltDivisor"]
order = 6
+++
Let $X$ be a smooth projective variety over an algebraically closed field
of characteristic $0$, with canonical bundle $K_X$, and $N$ a nef and big
line bundle. Then
$$ H^q(X, K_X \otimes N) = 0 \qquad (q > 0). $$

We derive it from two further published results, proved here as well:

* *Nadel vanishing* on a normal projective complex variety: if $N$ is
  numerically equivalent to $\tfrac1m(mK_X + \Delta) + \tfrac1r M_0$ with
  $\Delta$ an effective $\Q$-divisor, $mK_X + \Delta$ Cartier and $M_0$ nef and
  big, then $H^i(X, \mathcal J \otimes N) = 0$ for $i > 0$, where
  $\mathcal J$ is the ideal of the non-klt locus of $(X, \Delta)$; together
  with the construction of a divisor whose non-klt locus is isolated at a
  given point when the self-intersections of $M_0$ on subvarieties through
  it are large;
* the *numerics of nef line bundles*: products of nef bundles have
  non-negative degree, a nef bundle is big exactly when its top
  self-intersection is positive, and
  $h^0(X, L^m) = (L^D)\, m^D/D! + O(m^{D-1})$ for nef $L$ on a variety of
  dimension $D$.
