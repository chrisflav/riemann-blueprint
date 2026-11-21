+++
kind = "proof"
of   = "vwin-of-hypotheses-h-e-alt"
uses = ["base-change-definite-unitary-group", "bloch-kato-local", "borel-casselman", "car-u-alt", "cheb",
        "chebotarev-degree-one", "core-g", "cusp-forms-bounded-gl", "cuspidal-multiplicity-one",
        "def-local-parameters", "depth-zero-support", "fontaine-bcris", "frame-bound", "generic-unitary-dual-gl",
        "geometric-lemma-filtration", "global-euler-char-full", "global-finiteness", "greenberg-wiles",
        "hasse-norm-st", "hecke-l-adic-character", "hecke-l-adic-character-de-rham", "irreducible-admissible-gl",
        "jacquet-rallis-unit-match-all-ranks", "jacquet-shalika-rigidity", "kato-two-w-of-prints-h",
        "lemma-k-lit-n-alt", "local-euler-char", "local-euler-char-k", "local-finiteness", "local-finiteness-k",
        "local-tate-duality", "local-tate-duality-k", "poitou-tate-normalised", "radford-shuffle-polynomial",
        "sp4-in0-alt", "thm-local-parameters-exist", "unramified-orthogonality",
        "wave-existence-speed-multiplicity"]
+++
Fix an auxiliary pair and a $\psi$-field $E$. By the
[Poitou–Tate sequence](@poitou-tate-normalised), [local Tate duality](@local-tate-duality-k),
the [local Euler characteristic formula](@local-euler-char-k) and the
[Greenberg–Wiles formula](@greenberg-wiles), the length of $Ш^1_l(E, -e)$ is
bounded by the lengths of the $\chi$-isotypic Selmer groups of
$\chi \otimes \Z_l(e)$, $\chi$ running over the even characters of
$\Gal(E/\Q)$, plus the second cohomology of Tate twists, which
[lemma-k-lit-n-alt] bounds. With the theorem of Ferrero and Washington this
gives the polynomial part. The Selmer groups are then bounded case by case
in $(l, e, \chi)$:

* $l$ prime to the fixed bad set and $l - 1 \nmid 2e$: Kato's Euler system
  ([kato-two-w-of-prints-h]), together with automorphy of the relevant
  2-dimensional representations over imaginary quadratic fields;
* two further cases: automorphy of $\mathrm{GSp}_4$-valued lifts ([sp4-in0-alt]);
* $l$ in the bad set and $e = 1$: automorphy of 3-dimensional
  representations over imaginary quadratic fields, through
  [base change from definite unitary groups](@base-change-definite-unitary-group);
* $\chi = 1$ and $l - 1 \mid 2e$: the Selmer group vanishes;
* the remaining part is bounded through [unramified orthogonality](@unramified-orthogonality).

Summing over $l$ and $e < t$ gives the bound of [def-sha-bound] with $t = \lfloor x^{401}\rfloor$.
