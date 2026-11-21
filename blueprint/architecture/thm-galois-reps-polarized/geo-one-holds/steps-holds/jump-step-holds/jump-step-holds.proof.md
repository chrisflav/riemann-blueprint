+++
kind = "proof"
of   = "jump-step-holds"
uses = ["crys-step-holds", "etale-finiteness-of-duality", "ht-spec-good",
        "projective-bundle-formula-vector-bundle-any-space", "proper-base-change"]
+++
Pass to the smooth projective model as in [crys-step-holds]. The Hodge–Tate
decomposition is compatible with pull-back and push-forward along the
correspondences ([ht-spec-good]), so it respects the $\theta$-eigenspaces on
both sides, and a non-zero Hodge eigenvector of type $(a, b)$ gives the
Hodge–Tate weight $a$ in $V_\theta$, hence in its subquotient $\rho$.
