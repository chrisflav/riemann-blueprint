+++
kind = "proof"
of   = "thm-mumford-degeneration"
uses = ["thm-abelian-variety-torsion-count", "lem-uniformisation-labelled-cover", "thm-unitary-integral-models", "thm-semi-abelian-hom-extension", "thm-semistable-reduction", "thm-semi-abelian-theta-models"]
+++
First pass to a finite extension of $R$ over which the data become labelled
by torsion points of all levels prime to a fixed odd prime; there
[lem-uniformisation-labelled-cover] gives the uniformisation
of the pull-back. Then descend, using that homomorphisms of semi-abelian
schemes extend uniquely over normal bases and the semistable reduction
theorem with Zarhin's geometric version of it.
