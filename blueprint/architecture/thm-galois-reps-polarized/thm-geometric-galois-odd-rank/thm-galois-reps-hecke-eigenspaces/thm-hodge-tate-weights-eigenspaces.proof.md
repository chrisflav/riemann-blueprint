+++
kind = "proof"
of   = "thm-hodge-tate-weights-eigenspaces"
uses = ["thm-eigenspaces-crystalline", "thm-etale-finiteness", "thm-hodge-tate-functorial",
        "thm-projective-bundle-formula", "thm-proper-base-change"]
+++
Pass to the smooth projective model as in [thm-eigenspaces-crystalline]. The Hodge–Tate
decomposition is compatible with pull-back and push-forward along the
correspondences ([thm-hodge-tate-functorial]), so it respects the $\theta$-eigenspaces on
both sides, and a non-zero Hodge eigenvector of type $(a, b)$ gives the
Hodge–Tate weight $a$ in $V_\theta$, hence in its subquotient $\rho$.
