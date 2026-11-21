+++
kind = "proof"
of   = "thm-unramified-annihilators"
uses = ["thm-tate-euler-characteristic-global-places", "thm-tate-local-finiteness", "thm-tate-local-duality-global-places"]
+++
Both unramified subgroups are images of the cohomology of
$G_v/I_v \cong \hat\Z$, so their orders are $|H^0|$. Their pairing is zero
because the cup product lands in $H^2(G_v/I_v, \cdot) = 0$. Local duality
[thm-tate-local-duality-global-places] and the local Euler characteristic formula
[thm-tate-euler-characteristic-global-places] together with finiteness
[thm-tate-local-finiteness] then give equality of orders, hence exact annihilation.
