+++
kind = "proof"
of   = "thm-sha-bound-from-hilbert-inputs"
uses = ["thm-labesse-base-change", "thm-bloch-kato-local", "thm-borel-casselman", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius",
        "thm-chebotarev-degree-one", "thm-twisted-trace-lowest-type", "thm-cusp-bounded-gl", "thm-multiplicity-one-gl",
        "def-local-parameters", "thm-depth-zero-support", "thm-fontaine-bcris", "thm-hecke-bound-base-change", "thm-tadic-generic-unitary-dual",
        "thm-geometric-lemma-filtration", "thm-tate-global-euler-characteristic", "thm-tate-global-finiteness", "thm-greenberg-wiles",
        "thm-hasse-norm-quadratic", "thm-hecke-l-adic-character", "thm-hecke-l-adic-character-de-rham", "thm-jacquet-irreducible-admissible",
        "thm-jacquet-rallis-fundamental-lemma", "thm-jacquet-shalika-strong-mult-one", "thm-kato-selmer-vanishing",
        "lem-h2-tate-twists-bound", "thm-tate-euler-characteristic-global-places", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness", "thm-tate-local-finiteness-padic",
        "thm-tate-local-duality-global-places", "thm-tate-local-duality-l-adic", "thm-poitou-tate", "thm-radford-shuffle",
        "thm-gsp4-lift-automorphy", "thm-local-parameters-exist", "thm-unramified-annihilators",
        "thm-wave-kernels-gln-c"]
+++
Fix an auxiliary pair and a $\psi$-field $E$. By the
[Poitou–Tate sequence](@thm-poitou-tate), [local Tate duality](@thm-tate-local-duality-l-adic),
the [local Euler characteristic formula](@thm-tate-euler-characteristic-l-adic) and the
[Greenberg–Wiles formula](@thm-greenberg-wiles), the length of $Ш^1_l(E, -e)$ is
bounded by the lengths of the $\chi$-isotypic Selmer groups of
$\chi \otimes \Z_l(e)$, $\chi$ running over the even characters of
$\Gal(E/\Q)$, plus the second cohomology of Tate twists, which
[lem-h2-tate-twists-bound] bounds. With the theorem of Ferrero and Washington this
gives the polynomial part. The Selmer groups are then bounded case by case
in $(l, e, \chi)$:

* $l$ prime to the fixed bad set and $l - 1 \nmid 2e$: Kato's Euler system
  ([thm-kato-selmer-vanishing]), together with automorphy of the relevant
  2-dimensional representations over imaginary quadratic fields;
* two further cases: automorphy of $\mathrm{GSp}_4$-valued lifts ([thm-gsp4-lift-automorphy]);
* $l$ in the bad set and $e = 1$: automorphy of 3-dimensional
  representations over imaginary quadratic fields, through
  [base change from definite unitary groups](@thm-labesse-base-change);
* $\chi = 1$ and $l - 1 \mid 2e$: the Selmer group vanishes;
* the remaining part is bounded through [unramified orthogonality](@thm-unramified-annihilators).

Summing over $l$ and $e < t$ gives the bound of [def-sha-bound] with $t = \lfloor x^{401}\rfloor$.
