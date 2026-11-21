+++
kind = "proof"
of   = "prop-selmer-bound-twisted-places"
uses = ["thm-fontaine-bcris", "thm-lifting-deep-weights", "thm-bloch-kato-local", "thm-artin-reciprocity", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-duality-l-adic"]
+++
Bound the lifting exponents at $q$ and $d$ with [thm-lifting-deep-weights],
and convert them into Selmer lengths with the
[local theory of Bloch and Kato](@thm-bloch-kato-local),
[local Tate duality](@thm-tate-local-duality-l-adic) and the
[Euler characteristic formula](@thm-tate-euler-characteristic-l-adic).
[Global Artin reciprocity](@thm-artin-reciprocity) relates the characters at
the two primes.
