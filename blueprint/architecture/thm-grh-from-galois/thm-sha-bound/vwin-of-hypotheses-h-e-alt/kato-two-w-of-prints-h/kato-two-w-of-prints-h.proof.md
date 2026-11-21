+++
kind = "proof"
of   = "kato-two-w-of-prints-h"
uses = ["borel-casselman", "car-u-alt", "cheb", "chebotarev-degree-one", "cusp-forms-bounded-gl",
        "def-local-parameters", "fontaine-bcris", "geometric-lemma-filtration", "hasse-norm-st",
        "irreducible-admissible-gl", "jacquet-shalika-rigidity", "thm-local-parameters-exist", "two-s"]
+++
Reduce to [two-s]. Its hypothesis on $W$ asks that every cuspidal
representation of $\GL_2(\A_\Q)$ attached to a twist of $W$ by a character of
finite order be unramified at $l$ when the twist is. This follows from
local–global compatibility at $l$ for the Galois representations of
polarized pairs, for the [local parameters](@thm-local-parameters-exist):
quadratic base change to $K$, the comparison with
[Fontaine's ring](@fontaine-bcris), and [Jacquet–Shalika rigidity](@jacquet-shalika-rigidity)
identify the local component at $l$. The second hypothesis of [two-s], that
an $l$-ordinary newform of level prime to $l$ is attached to the twist,
comes from the roots of the Hecke polynomial at $l$, which the same
compatibility identifies with the eigenvalues of Frobenius on the flag.
