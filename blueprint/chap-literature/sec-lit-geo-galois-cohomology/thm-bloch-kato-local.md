+++
kind  = "theorem"
title = "Bloch–Kato local theory"
source = "Bloch–Kato [bloch-kato-1990]"
lean  = ["GlobalTheory.Published.BlochKatoLocal", "UpperTheory.Lit.blochKatoLocal"]
order = 6
+++
Let $K/\Q_l$ be a finite extension, with Fontaine's period rings, and let
$V$ be a de Rham representation of $G_K$ over $\Q_l$. Let
$H^1_f(K, V) = \ker\big(H^1(K, V) \to H^1(K, V \otimes B_{\mathrm{cris}})\big)$.
Then:

* $H^1_f(K, V)$ is finite-dimensional and
  $$ \dim H^1_f(K, V) = \dim H^0(K, V) + \dim D_{\mathrm{dR}}(V)/\mathrm{Fil}^0 D_{\mathrm{dR}}(V); $$
* under the cup product with a dual $V' = V^\vee(1)$, $H^1_f(K, V)$ and
  $H^1_f(K, V')$ are exact annihilators of each other;
* the same holds integrally: for $\Z_l$-lattices $T \subset V$ and
  $T' \subset V'$ in duality, the images of $H^1_f$ in the cohomology of
  $V/T$ and $V'/T'$ are exact annihilators.
