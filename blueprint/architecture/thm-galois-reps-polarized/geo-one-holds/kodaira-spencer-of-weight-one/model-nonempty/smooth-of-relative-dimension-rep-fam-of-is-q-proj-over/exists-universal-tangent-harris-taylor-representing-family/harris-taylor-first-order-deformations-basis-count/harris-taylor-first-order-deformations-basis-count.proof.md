+++
kind = "proof"
of   = "harris-taylor-first-order-deformations-basis-count"
uses = ["abelian-de-rham", "abelian-de-rham-page", "abelian-lifting", "dual-abelian-scheme",
        "grothendieck-deformation", "harris-taylor-finrank-de-rham-quotient-character"]
+++
By Grothendieck's deformation theory, first-order deformations correspond to
lifts of the Hodge filtration that respect the $\mathcal O_D$-action and the
polarisation. *We read* the count as the usual one: $\mathcal O_F$ splits
$H^{\mathrm{dR}}_1(A_0)$ into eigenparts for the embeddings, and each of the $a$
embeddings $t_i$ contributes $n - 1$ directions. The sizes of the eigenparts come
from [harris-taylor-finrank-de-rham-quotient-character].
