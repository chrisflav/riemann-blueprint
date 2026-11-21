+++
kind = "proof"
of   = "thm-grh-from-galois"
uses = ["thm-sha-bound", "thm-local-parameters-exist", "thm-grh-from-sha-bound",
        "thm-grh-from-theta-integrals", "thm-family-data-exists",
        "thm-zero-free-from-families", "thm-zero-free-from-connected"]
+++
Assume that polarized pairs have Galois representations. The proof walks
down the chain of [sec-outline-chain].

1. From these Galois representations, [thm-sha-bound] ([chap-sha]) gives the
   Tate–Shafarevich bound with exponent $401$ for every primitive character,
   and [thm-local-parameters-exist] gives a system of local parameters. These
   are the hypotheses of [thm-grh-from-sha-bound].
2. By the theorem of Gelfand and Kazhdan, the Galois representations of
   polarized pairs give Galois representations for the cuspidal
   representations that the families use ([sec-gal-cuspidal]). This reduces
   the claim to [thm-grh-from-theta-integrals].
3. With these, [thm-family-data-exists] ([chap-families]) gives a class of
   families of definite unitary groups satisfying the family hypotheses. Its
   inputs come from [chap-theta], [chap-heights] and [chap-sha]. This reduces
   the claim to [thm-zero-free-from-families].
4. The families have slope data, the Tate–Shafarevich bound gives auxiliary
   fields, and [thm-zero-free-from-connected] ([chap-zero-free]) turns the two
   into zero-freeness for primitive characters, through the core inequality
   and Landau's theorem. Imprimitive characters follow at once.
