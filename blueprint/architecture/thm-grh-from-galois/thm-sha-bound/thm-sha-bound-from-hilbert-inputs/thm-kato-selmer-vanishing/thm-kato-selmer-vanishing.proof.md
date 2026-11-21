+++
kind = "proof"
of   = "thm-kato-selmer-vanishing"
uses = ["thm-borel-casselman", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-cusp-bounded-gl",
        "def-local-parameters", "thm-fontaine-bcris", "thm-geometric-lemma-filtration", "thm-hasse-norm-quadratic",
        "thm-jacquet-irreducible-admissible", "thm-jacquet-shalika-strong-mult-one", "thm-local-parameters-exist", "thm-kato-spherical"]
+++
Reduce to [thm-kato-spherical]. Its hypothesis on $W$ asks that every cuspidal
representation of $\GL_2(\A_\Q)$ attached to a twist of $W$ by a character of
finite order be unramified at $l$ when the twist is. This follows from
local–global compatibility at $l$ for the Galois representations of
polarized pairs, for the [local parameters](@thm-local-parameters-exist):
quadratic base change to $K$, the comparison with
[Fontaine's ring](@thm-fontaine-bcris), and [Jacquet–Shalika rigidity](@thm-jacquet-shalika-strong-mult-one)
identify the local component at $l$. The second hypothesis of [thm-kato-spherical], that
an $l$-ordinary newform of level prime to $l$ is attached to the twist,
comes from the roots of the Hecke polynomial at $l$, which the same
compatibility identifies with the eigenvalues of Frobenius on the flag.
