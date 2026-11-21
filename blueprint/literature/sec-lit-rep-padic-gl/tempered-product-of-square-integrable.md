+++
kind  = "theorem"
title = "Tempered representations are products of square-integrable ones"
lean  = ["GlobalTheory.Published.TemperedProductOfSquareIntegrable", "UpperTheory.Lit.Cas.temperedProduct"]
uses  = ["bernstein-zelevinsky-finiteness", "ess-square-integrable-segments", "geometric-lemma", "irreducible-admissible-gl", "standard-functors-finite-length"]
order = 11
+++
Let $F$ be a non-archimedean local field of characteristic zero and
$N \ge 1$. An irreducible smooth representation $\pi$ of $\GL_N(F)$ is
tempered if and only if $\pi \cong \delta_1 \times \dots \times \delta_h$ for
irreducible square-integrable representations $\delta_i$ of $\GL_{n_i}(F)$
with $\sum n_i = N$. This is the classical description of the tempered dual
of $\GL_N$ (Jacquet; Bernstein–Zelevinsky). It rests on
[bernstein-zelevinsky-finiteness], [standard-functors-finite-length],
[irreducible-admissible-gl], the geometric lemma [geometric-lemma] and
the segment classification [ess-square-integrable-segments].
