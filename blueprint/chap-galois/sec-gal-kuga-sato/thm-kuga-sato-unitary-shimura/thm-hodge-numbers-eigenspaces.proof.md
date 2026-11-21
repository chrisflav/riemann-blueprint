+++
kind = "proof"
of   = "thm-hodge-numbers-eigenspaces"
uses = ["thm-hecke-fixed-points-kuga-sato", "thm-abelian-variety-torsion-count", "thm-hasse-norm-quadratic", "thm-unitary-shimura-integral-models", "thm-semistable-reduction",
        "thm-semi-abelian-theta-models"]
+++
For each Hecke correspondence composed with translations, the holomorphic
Lefschetz formula writes its alternating trace on $H^*(\Omega^h)$ as a sum of
fixed-point terms, and [thm-hecke-fixed-points-kuga-sato] turns that sum into orbital integrals.
*We read* the rest as follows: varying the translations $\alpha_s$ separates the
Hodge exponents, and the orbital integrals, taken over the Hecke algebra,
detect $\theta$ with weight $\lambda$, so the $\theta$-eigenspace of each predicted type
is non-zero. The proof also uses the Hasse norm theorem and the semistable
reduction theorem.
