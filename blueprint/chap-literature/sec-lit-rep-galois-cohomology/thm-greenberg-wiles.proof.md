+++
kind = "proof"
of   = "thm-greenberg-wiles"
uses = ["thm-tate-global-euler-characteristic", "thm-tate-euler-characteristic-global-places", "thm-tate-local-finiteness", "thm-tate-local-duality-global-places", "thm-poitou-tate"]
+++
This is the standard argument. The Poitou–Tate sequence [thm-poitou-tate]
with the local conditions $\mathcal L$ and $\mathcal L^\perp$, which are exact
annihilators under local Tate duality [thm-tate-local-duality-global-places],
expresses the ratio of the two Selmer groups through global and local
cohomology groups, all finite by [thm-tate-local-finiteness]. Tate's global
Euler characteristic formula [thm-tate-global-euler-characteristic] and the
local formula [thm-tate-euler-characteristic-global-places] then evaluate
the alternating products of their orders.
