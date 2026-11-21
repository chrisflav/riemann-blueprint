+++
kind = "proof"
of   = "thm-wach-lifting-theorem"
uses = ["thm-fontaine-bcris", "thm-bloch-kato-local", "thm-tate-euler-characteristic-l-adic",
        "thm-tate-local-duality-l-adic"]
+++
Attach to each crystalline lattice of a member its Wach module. By the
theory of Wach and Berger, the Wach module recovers the étale lattice, its
de Rham and crystalline periods agree in the unramified case, and for
$l \ge 5$ it has unit generators; the proof uses about a dozen such
properties, which follow from the
[local theory of Bloch and Kato](@thm-bloch-kato-local),
[local Tate duality](@thm-tate-local-duality-l-adic), the
[Euler characteristic formula](@thm-tate-euler-characteristic-l-adic) and
[Fontaine's period ring](@thm-fontaine-bcris). Reduce to a lift along the
cyclotomic tower, which is compatible with base change, and apply a
crystalline lifting bound to the Wach module of each lattice. This gives
the lifting theorem with constant $800$. The corollary follows by applying
the theorem along the clusters.
