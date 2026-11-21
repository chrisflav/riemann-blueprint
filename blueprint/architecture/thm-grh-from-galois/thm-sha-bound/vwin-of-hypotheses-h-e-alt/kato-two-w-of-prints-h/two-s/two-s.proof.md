+++
kind = "proof"
of   = "two-s"
uses = ["bloch-kato-local", "cheb", "chebotarev-degree-one", "local-euler-char", "local-euler-char-k",
        "local-finiteness", "local-finiteness-k", "local-tate-duality", "local-tate-duality-k", "zeta-ur"]
+++
By the hypothesis, $W$ and its twist by $\det W$ come from $l$-ordinary
newforms of level prime to $l$, so [zeta-ur] gives each an Euler system whose
bottom class is not in the ordinary local condition at $l$. Kolyvagin's
argument then shows that the Selmer group with the dual local condition
vanishes: for a nonzero Selmer class, [Chebotarev's theorem](@cheb) gives a
prime $w \equiv 1 \bmod l^n$ at which the class and the Euler system
derivative are both nonzero locally, and the reciprocity law, with
[local Tate duality](@local-tate-duality), [local Euler characteristics](@local-euler-char)
and the [local Bloch–Kato conditions](@bloch-kato-local), gives a
contradiction. Applied to $W$ and to $W \otimes \theta$ this is the claim.
