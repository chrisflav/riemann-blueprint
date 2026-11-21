+++
kind = "proof"
of   = "thm-galois-reps-csd-above-l"
uses = ["def-galois-reps-polarized", "thm-bz-finiteness", "thm-borel-casselman", "thm-zelevinsky-segments", "thm-geometric-lemma", "thm-hasse-norm-quadratic", "thm-hc-finiteness-gl", "thm-cusp-bounded-gl", "thm-multiplicity-one-gl", "thm-gelfand-kazhdan", "thm-jacquet-shalika-strong-mult-one"]
+++
A conjugate self-dual $\pi$ forms a polarized pair with $\chi = \eta^a$,
$\eta$ the quadratic character of $E/E^+$, once one knows
$\pi^\vee \cong \pi\circ\theta$, $\theta(g) = {}^tg^{-1}$. This is
Gelfand–Kazhdan [thm-gelfand-kazhdan], which rests on strong multiplicity
one [thm-jacquet-shalika-strong-mult-one], multiplicity one
[thm-multiplicity-one-gl] and the boundedness of cusp forms
[thm-cusp-bounded-gl]. The existence theorem for polarized pairs,
[thm-galois-reps-polarized], then gives $r$ with the first three
properties. The compatibility above $l$ is read off from the local
conditions of $r$ in the abelian case, using the Langlands classification
[thm-zelevinsky-segments], [thm-bz-finiteness], the geometric lemma
[thm-geometric-lemma], the Borel–Casselman theorem [thm-borel-casselman]
and the Hasse norm theorem [thm-hasse-norm-quadratic]. The finiteness
theorem [thm-hc-finiteness-gl] appears among the inputs of one step but is
not needed there.
