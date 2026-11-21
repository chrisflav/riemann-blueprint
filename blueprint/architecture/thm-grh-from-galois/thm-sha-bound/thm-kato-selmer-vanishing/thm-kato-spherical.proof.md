+++
kind = "proof"
of   = "thm-kato-spherical"
uses = ["def-galois-cohomology-inputs", "thm-bloch-kato-local", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-tate-euler-characteristic-global-places", "thm-tate-euler-characteristic-l-adic",
        "thm-tate-local-finiteness", "thm-tate-local-finiteness-padic", "thm-tate-local-duality-global-places", "thm-tate-local-duality-l-adic", "thm-kato-euler-system-ordinary"]
+++
By the hypothesis, $W$ and its twist by $\det W$ come from $l$-ordinary
newforms of level prime to $l$, so [thm-kato-euler-system-ordinary] gives each an Euler system whose
bottom class is not in the ordinary local condition at $l$. Kolyvagin's
argument then shows that the Selmer group with the dual local condition
vanishes: for a nonzero Selmer class, [Chebotarev's theorem](@thm-chebotarev-degree-one-frobenius) gives a
prime $w \equiv 1 \bmod l^n$ at which the class and the Euler system
derivative are both nonzero locally, and the reciprocity law, with
[local Tate duality](@thm-tate-local-duality-global-places), [local Euler characteristics](@thm-tate-euler-characteristic-global-places)
and the [local Bloch–Kato conditions](@thm-bloch-kato-local), gives a
contradiction. Applied to $W$ and to $W \otimes \theta$ this is the claim.
