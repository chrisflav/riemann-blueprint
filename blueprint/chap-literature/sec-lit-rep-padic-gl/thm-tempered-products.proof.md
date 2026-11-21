+++
kind = "proof"
of   = "thm-tempered-products"
uses = ["thm-bz-finiteness", "thm-zelevinsky-segments", "thm-geometric-lemma", "thm-jacquet-irreducible-admissible", "thm-bz-functors-finite-length"]
+++
By the Langlands classification (part 3 of [thm-zelevinsky-segments]),
$\pi$ is the irreducible cosocle of a standard module
$\delta_1\nu^{e_1} \times \dots \times \delta_h\nu^{e_h}$, $e_1 \ge \dots \ge e_h$,
with $\delta_i$ square-integrable by part 1. Computing the Jacquet modules
of this product with the geometric lemma [thm-geometric-lemma], in the
finite-length setting of [thm-bz-finiteness],
[thm-bz-functors-finite-length] and [thm-jacquet-irreducible-admissible],
Casselman's criterion shows that $\pi$ is tempered exactly when all $e_i$
vanish, and in that case the standard module is irreducible and equal to
$\pi$.
