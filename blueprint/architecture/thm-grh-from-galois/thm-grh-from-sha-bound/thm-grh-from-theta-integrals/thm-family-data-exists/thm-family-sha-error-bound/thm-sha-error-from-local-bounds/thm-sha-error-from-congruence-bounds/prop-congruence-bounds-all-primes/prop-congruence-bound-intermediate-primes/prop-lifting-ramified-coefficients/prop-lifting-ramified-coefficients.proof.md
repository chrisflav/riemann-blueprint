+++
kind = "proof"
of   = "prop-lifting-ramified-coefficients"
uses = ["thm-fontaine-bcris", "lem-ramified-lifting-from-inputs", "thm-bloch-kato-local", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-duality-l-adic"]
+++
Apply [lem-ramified-lifting-from-inputs] to the lattices of each member. The
properties of Wach modules and of finite classes that the lemma uses follow
from the [local theory of Bloch and Kato](@thm-bloch-kato-local),
[local Tate duality](@thm-tate-local-duality-l-adic), the
[Euler characteristic formula](@thm-tate-euler-characteristic-l-adic) and
[Fontaine's period ring](@thm-fontaine-bcris).
