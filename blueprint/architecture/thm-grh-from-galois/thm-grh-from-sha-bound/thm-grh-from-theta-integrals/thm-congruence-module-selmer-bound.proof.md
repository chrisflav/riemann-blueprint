+++
kind = "proof"
of   = "thm-congruence-module-selmer-bound"
uses = ["thm-congruence-bound-local-inputs", "thm-artin-reciprocity", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-duality-l-adic"]
+++
The triviality of unramified classes gives the unramified condition of
[thm-congruence-bound-local-inputs], which then applies with the same data.
Its proof uses [global Artin reciprocity](@thm-artin-reciprocity),
[local Tate duality](@thm-tate-local-duality-l-adic) and the
[local Euler characteristic formula](@thm-tate-euler-characteristic-l-adic).
