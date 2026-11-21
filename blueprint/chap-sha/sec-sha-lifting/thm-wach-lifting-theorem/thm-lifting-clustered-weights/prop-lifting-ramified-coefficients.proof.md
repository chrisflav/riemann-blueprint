+++
kind = "proof"
of   = "prop-lifting-ramified-coefficients"
uses = ["thm-fontaine-bcris", "thm-bloch-kato-local", "thm-tate-euler-characteristic-global-places",
        "thm-tate-local-duality-global-places"]
+++
Let $F : T_1 \to T_2$ be a surjection of crystalline lattices of a member.
Follow chains of lattices through the ramified coefficient field, one step
per window, and add the exponents. Each step uses the lifting properties of
Wach modules, the extension of Herr's description of Galois cohomology to
these lattices, bounds for crystalline lifting and
[Fontaine's period ring](@thm-fontaine-bcris); the
[local theory of Bloch and Kato](@thm-bloch-kato-local),
[local Tate duality](@thm-tate-local-duality-global-places) and the
[Euler characteristic formula](@thm-tate-euler-characteristic-global-places) give
these. The chains also need a condition on the labelling of the
embeddings, which the lattices of a member satisfy. The bound holds for
every choice of the auxiliary constants. *It is not clear* how the constant
$25$ arises.
