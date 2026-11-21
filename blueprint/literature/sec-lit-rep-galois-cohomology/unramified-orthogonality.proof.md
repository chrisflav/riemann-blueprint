+++
kind = "proof"
of   = "unramified-orthogonality"
uses = ["local-euler-char", "local-euler-char-k", "local-finiteness", "local-tate-duality"]
+++
Both unramified subgroups are images of the cohomology of
$G_v/I_v \cong \hat\Z$, so their orders are $|H^0|$. Their pairing is zero
because the cup product lands in $H^2(G_v/I_v, \cdot) = 0$. Local duality
[local-tate-duality] and the local Euler characteristic formula
([local-euler-char], [local-euler-char-k]) together with finiteness
[local-finiteness] then give equality of orders, hence exact annihilation.
