+++
kind = "proof"
of   = "lem-first-order-deformation-count"
uses = ["thm-de-rham-abelian-schemes", "lem-hodge-filtration-abelian-scheme", "thm-abelian-scheme-lifting-divided-powers", "thm-dual-abelian-scheme",
        "thm-grothendieck-messing", "lem-de-rham-eigenpart-rank"]
+++
By Grothendieck's deformation theory, first-order deformations correspond to
lifts of the Hodge filtration that respect the $\mathcal O_D$-action and the
polarisation. *We read* the count as the usual one: $\mathcal O_F$ splits
$H^{\mathrm{dR}}_1(A_0)$ into eigenparts for the embeddings, and each of the $a$
embeddings $t_i$ contributes $n - 1$ directions. The sizes of the eigenparts come
from [lem-de-rham-eigenpart-rank].
