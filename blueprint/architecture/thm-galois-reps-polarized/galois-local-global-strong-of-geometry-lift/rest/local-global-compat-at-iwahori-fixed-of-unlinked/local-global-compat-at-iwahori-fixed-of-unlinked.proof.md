+++
kind = "proof"
of   = "local-global-compat-at-iwahori-fixed-of-unlinked"
uses = ["automorphic-forms-finite-gl", "bernstein-zelevinsky-finiteness", "car-u-alt", "cheb",
        "chebotarev-degree-one", "chevalley-units", "cusp-forms-bounded-gl", "cuspidal-multiplicity-one",
        "cuspidal-spectrum-gl", "def-local-parameters", "ess-square-integrable-segments",
        "gelfand-kazhdan-dual", "geometric-lemma", "global-artin-reciprocity", "hasse-norm-st",
        "irreducible-admissible-gl", "jacquet-shalika-rigidity", "supp-bc-outright",
        "thm-local-parameters-exist"]
+++
For a principal series the claim is the hypothesis together with the
compatibility at unramified places. For the mixed depth-zero case, choose the
solvable extension $K$ by Chebotarev's theorem and Artin reciprocity, base change
$\pi$ to $K$, and apply [supp-bc-outright] at the place above $w$. Restriction to
$G_K$ does not change the action of inertia, and the local parameters of
[thm-local-parameters-exist] give depth-zero representations the inertial
characteristic polynomials that match ([def-local-parameters]).
