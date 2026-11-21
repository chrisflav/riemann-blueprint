+++
kind = "proof"
of   = "lem-ramified-lifting-from-inputs"
uses = ["thm-fontaine-bcris", "thm-bloch-kato-local", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-duality-l-adic"]
+++
Follow chains of lattices through the ramified coefficient field, one step
per window, and add the exponents. Each step uses the lifting properties of
Wach modules, the extension of Herr's description of Galois cohomology to
these lattices, bounds for crystalline lifting and
[Fontaine's period ring](@thm-fontaine-bcris); the
[local theory of Bloch and Kato](@thm-bloch-kato-local),
[local Tate duality](@thm-tate-local-duality-l-adic) and the
[Euler characteristic formula](@thm-tate-euler-characteristic-l-adic) give
these. The chains also need a condition on the labelling of the
embeddings, which the lattices of a member satisfy. *It is not clear* how
the constant $25$ arises.
