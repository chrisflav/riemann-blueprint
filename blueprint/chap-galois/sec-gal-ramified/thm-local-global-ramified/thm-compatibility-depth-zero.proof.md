+++
kind = "proof"
of   = "thm-compatibility-depth-zero"
uses = ["thm-hc-finiteness-gl", "thm-bz-finiteness", "thm-chebotarev-degree-one", "thm-chevalley-congruence-units", "thm-cusp-bounded-gl", "thm-multiplicity-one-gl",
        "thm-cuspidal-spectrum-gl", "def-local-parameters", "thm-zelevinsky-segments",
        "thm-gelfand-kazhdan", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-hasse-norm-quadratic",
        "thm-jacquet-irreducible-admissible", "thm-jacquet-shalika-strong-mult-one", "thm-depth-zero-base-change-principal-series",
        "thm-local-parameters-exist"]
+++
For a principal series the claim is the hypothesis together with the
compatibility at unramified places. For the mixed depth-zero case, choose the
solvable extension $K$ by Chebotarev's theorem and Artin reciprocity, base change
$\pi$ to $K$, and apply [thm-depth-zero-base-change-principal-series] at the place above $w$. Restriction to
$G_K$ does not change the action of inertia, and the local parameters of
[thm-local-parameters-exist] give depth-zero representations the inertial
characteristic polynomials that match ([def-local-parameters]).
