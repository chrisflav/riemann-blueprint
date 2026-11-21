+++
kind = "proof"
of   = "thm-kato-selmer-vanishing"
uses = ["thm-kato-euler-system-ordinary", "thm-bloch-kato-local", "thm-tate-euler-characteristic-global-places", "thm-tate-local-finiteness", "thm-tate-local-duality-global-places", "thm-hilbert-modular-inputs", "thm-de-rham-abelian-schemes", "thm-p-adic-monodromy", "thm-dual-abelian-scheme", "def-galois-cohomology-inputs", "thm-base-change-unitary", "thm-borel-casselman", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one", "thm-cusp-bounded-gl", "def-local-parameters", "thm-fontaine-bcris", "thm-geometric-lemma-filtration", "thm-hasse-norm-quadratic", "thm-jacquet-irreducible-admissible", "thm-jacquet-shalika-strong-mult-one", "thm-local-parameters-exist", "thm-hecke-character-wd-above-l", "thm-hc-finiteness-gl", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-brauer-induction-degree-zero", "thm-chevalley-congruence-units", "thm-clozel-cohomological", "thm-clozel-purity", "thm-cusp-rapid-decay", "thm-cuspidal-spectrum-gl", "thm-depth-zero-from-support", "thm-shimura-main-theorem-cm", "thm-zelevinsky-segments", "thm-gelfand-kazhdan", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-green-regular-characters", "thm-grothendieck-messing", "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-functional-equation-cm", "thm-singular-moduli-class-number", "thm-jacquet-shalika", "thm-henniart-local-converse", "thm-moy-prasad-jacquet", "thm-partial-zeta-functional-equation", "thm-ray-class-field", "thm-siegel-klingen-rationality", "thm-square-integrable-segment", "thm-tempered-products"]
+++
*Sphericity and ordinary newforms.* First, $W$ is *spherical at $l$*: every
cuspidal representation of $\GL_2(\A_\Q)$ attached to a twist of $W$ by a
character of finite order is unramified at $l$ when the twist is. This
follows from local–global compatibility at $l$ for the Galois
representations of polarized pairs, for the
[local parameters](@thm-local-parameters-exist): quadratic base change to
$K$, the comparison with [Fontaine's ring](@thm-fontaine-bcris), and
[Jacquet–Shalika rigidity](@thm-jacquet-shalika-strong-mult-one) identify the
local component at $l$. Next, a twist of $W \otimes \epsilon^{-e}\det W^{-1}$
by a character of order $l$ is attached to an $l$-ordinary newform of weight
$2e+1$ and level prime to $l$; this comes from the roots of the Hecke
polynomial at $l$, which the same compatibility identifies with the
eigenvalues of Frobenius on the flag.

*Kolyvagin's argument.* So $W$ and its twist by $\det W$ come from
$l$-ordinary newforms of level prime to $l$, and
[thm-kato-euler-system-ordinary] gives each an Euler system whose bottom
class is not in the ordinary local condition at $l$. Kolyvagin's argument
then shows that the Selmer group with the dual local condition vanishes: for
a nonzero Selmer class, [Chebotarev's theorem](@thm-chebotarev-degree-one)
gives a prime $w \equiv 1 \bmod l^n$ at which the class and the Euler system
derivative are both nonzero locally, and the reciprocity law, with
[local Tate duality](@thm-tate-local-duality-global-places),
[local Euler characteristics](@thm-tate-euler-characteristic-global-places)
and the [local Bloch–Kato conditions](@thm-bloch-kato-local), gives a
contradiction. Applied to $W$ and to $W \otimes \theta$ this is the claim.
