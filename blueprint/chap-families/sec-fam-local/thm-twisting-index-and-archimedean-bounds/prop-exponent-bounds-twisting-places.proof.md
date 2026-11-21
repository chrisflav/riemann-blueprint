+++
kind = "proof"
of   = "prop-exponent-bounds-twisting-places"
uses = ["thm-hc-finiteness-gl", "thm-bz-finiteness", "thm-borel-casselman",
        "thm-galois-reps-csd-above-l", "thm-cusp-bounded-gl", "thm-zelevinsky-segments",
        "thm-fontaine-bcris", "thm-geometric-lemma", "thm-hasse-norm-quadratic",
        "thm-jacquet-irreducible-admissible", "lem-local-models-weight-range",
        "thm-labesse-base-change", "thm-bhatt-scholze-coefficients", "thm-chebotarev-degree-one",
        "thm-clozel-cohomological", "thm-galois-reps-polarized-cuspidal",
        "thm-hecke-l-adic-character", "thm-hecke-l-adic-character-above-l",
        "lem-prime-power-lattice-inclusion-exponent"]
+++
Take for $J_j(l)$ the recursive exponent $J^{\mathrm{rec}}_j(l)$ of
[lem-prime-power-lattice-inclusion-exponent]. The argument has three
inputs.

* A *cutting inequality* for $l$-adic exponents: for a partition $\lambda$
  of length $N$, a prime $l$ and $a \le N$, the exponent attached to
  $\lambda$ is at most the sum of the exponents of its first $a$ and last
  $N-a$ parts plus $a(N-a)\log_l w$, where $w$ bounds the spread of the
  parts. It comes from the exact exponents of Weyl lattices; *we read* it
  as a subadditivity of exponents of Weyl-module lattices.
* Numerical conditions relating the parameters and weights at each index
  $j$ to the size data of the point, and the sums of exponents; these are
  proved directly.
* Local models at the twisting places in the weight range
  ([lem-local-models-weight-range]). The Galois input there comes from
  Clozel's theorem on cohomological representations
  [thm-clozel-cohomological], base change for definite unitary groups
  [thm-labesse-base-change], the Galois representations of polarized
  cuspidal representations [thm-galois-reps-polarized-cuspidal] and the
  $l$-adic characters of algebraic Hecke characters
  ([thm-hecke-l-adic-character], [thm-hecke-l-adic-character-above-l]),
  with Chebotarev's theorem for primes of degree one
  [thm-chebotarev-degree-one] and the theorem of Bhatt and Scholze
  [thm-bhatt-scholze-coefficients].

Each $J_j(w)$ is bounded by the exponent of the inclusion
$l^{J}\Lambda \subseteq \Lambda'_w$ of the cut lattices in the localised
reference lattices at $w$, which
[lem-prime-power-lattice-inclusion-exponent] bounds by
$J^{\mathrm{rec}}_j(p_w)$. A bound for sums of exponents over a set of
primes, which uses the cutting inequality, gives
$\sum_{l \in Q}J_j(l)\log l \le E_J$ with $E_J = 30\,t\,m\,b\,L^2 + 2mb$,
where $L = x^\varepsilon$, $b = e^L$ and $t$ is the size of an auxiliary
set of places.
