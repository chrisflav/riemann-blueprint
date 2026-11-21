+++
kind = "proof"
of   = "thm-sha-bound"
uses = ["thm-hilbert-modular-inputs", "thm-galois-reps-polarized", "thm-kato-euler-system-ordinary", "thm-kato-explicit-reciprocity", "thm-base-change-unitary", "thm-de-rham-abelian-schemes", "thm-p-adic-monodromy", "thm-dual-abelian-scheme", "def-galois-cohomology-inputs", "thm-labesse-base-change", "thm-bloch-kato-local", "thm-borel-casselman", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one", "thm-twisted-trace-lowest-type", "thm-cusp-bounded-gl", "thm-multiplicity-one-gl", "def-local-parameters", "thm-depth-zero-support", "thm-fontaine-bcris", "thm-hecke-bound-base-change", "thm-tadic-generic-unitary-dual", "thm-geometric-lemma-filtration", "thm-tate-global-euler-characteristic", "thm-tate-global-finiteness", "thm-greenberg-wiles", "thm-hasse-norm-quadratic", "thm-hecke-l-adic-character", "thm-hecke-l-adic-character-de-rham", "thm-jacquet-irreducible-admissible", "thm-jacquet-rallis-fundamental-lemma", "thm-jacquet-shalika-strong-mult-one", "thm-kato-selmer-vanishing", "lem-h2-tate-twists-bound", "thm-tate-euler-characteristic-global-places", "thm-tate-local-finiteness", "thm-tate-local-duality-global-places", "thm-poitou-tate", "thm-radford-shuffle", "thm-gsp4-lift-automorphy", "thm-local-parameters-exist", "thm-unramified-annihilators", "thm-wave-kernels-gln-c", "thm-hecke-character-wd-above-l", "thm-hc-finiteness-gl", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-brauer-induction-degree-zero", "thm-chevalley-congruence-units", "thm-clozel-cohomological", "thm-clozel-purity", "thm-cusp-rapid-decay", "thm-cuspidal-spectrum-gl", "thm-depth-zero-from-support", "thm-shimura-main-theorem-cm", "thm-zelevinsky-segments", "thm-gelfand-kazhdan", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-green-regular-characters", "thm-grothendieck-messing", "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-functional-equation-cm", "thm-singular-moduli-class-number", "thm-jacquet-shalika", "thm-henniart-local-converse", "thm-moy-prasad-jacquet", "thm-partial-zeta-functional-equation", "thm-ray-class-field", "thm-siegel-klingen-rationality", "thm-square-integrable-segment", "thm-tempered-products"]
+++
*Inputs from automorphic forms.* The Galois representations of polarized
pairs ([thm-galois-reps-polarized]), with weak descent from $\GL_n$ to
unitary groups, give the results on Hilbert modular forms that the proof
needs ([thm-hilbert-modular-inputs]).

*Reduction to Selmer groups.* Fix an auxiliary pair and a $\psi$-field $E$.
By the [Poitou–Tate sequence](@thm-poitou-tate),
[local Tate duality](@thm-tate-local-duality-global-places), the
[local Euler characteristic formula](@thm-tate-euler-characteristic-global-places)
and the [Greenberg–Wiles formula](@thm-greenberg-wiles), the length of
$Ш^1_l(E, e)$ is bounded by the lengths of the $\chi$-isotypic Selmer groups
of $\chi \otimes \Z_l(e)$, $\chi$ running over the even characters of
$\Gal(E/\Q)$, plus the second cohomology of Tate twists, which
[lem-h2-tate-twists-bound] bounds. With the theorem of Ferrero and
Washington this gives the polynomial part.

*The Selmer groups, case by case.* Let $B$ be the finite set of bad primes
attached to $\psi$, and $\chi'_l$ the character obtained from the
prime-to-$l$ part of $\chi$. For odd $l$ the cases are:

1. $l \notin B$ and $l - 1 \nmid 2e$: Kato's Euler system
   ([thm-kato-selmer-vanishing]), built in [thm-kato-euler-system-ordinary]
   and controlled by the explicit reciprocity law
   [thm-kato-explicit-reciprocity], together with automorphy of the
   relevant 2-dimensional representations over imaginary quadratic fields;
2. $e \ge 2$, $\chi'_l$ of even order, and $l \in B$ or $l - 1 \mid 2e$;
3. $l \notin B$, $l - 1 \mid 2e$ and $\chi \ne 1$ of odd order: in cases 2
   and 3 Ribet's method produces the Selmer classes from irreducible lifts
   with values in $\mathrm{GSp}_4$, which are automorphic
   ([thm-gsp4-lift-automorphy]);
4. $l \in B$, $e \ge 2$ and $\chi'_l$ of odd order: unramified classes are
   [exact annihilators](@thm-unramified-annihilators) under local duality;
5. $l \in B$ and $e = 1$: automorphy of 3-dimensional representations over
   imaginary quadratic fields, through
   [base change from definite unitary groups](@thm-labesse-base-change);
6. $l \notin B$, $l - 1 \mid 2e$ and $\chi = 1$: the Selmer group vanishes.

In each case the lengths are bounded by a polynomial in $l$, $e$, $t$ and
the level. Summing over $l$ and $e < t$ gives the bound with
$t = \lfloor x^{401}\rfloor$.

*We read* the vanishing for the trivial character as the "significant
weakening of Vandiver's conjecture" in the announcement.

*Where the bound is used.* The theorem is not used inside this chapter. The
second half of the chapter proves [thm-family-sha-error-bound]: the error
term of each member of a family is bounded by the same weighted sum of
lengths of $Ш^1_l(E, e)$, through congruence modules
([thm-congruence-module-selmer-bound]) and local lifting theorems
([thm-wach-lifting-theorem]). [thm-zero-free-from-families] combines the
two.
