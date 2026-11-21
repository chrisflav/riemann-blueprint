+++
kind  = "theorem"
title = "Tempered representations are products of square-integrable ones"
lean  = ["GlobalTheory.Published.TemperedProductOfSquareIntegrable", "UpperTheory.Lit.Cas.temperedProduct"]
uses  = ["thm-bz-finiteness", "thm-zelevinsky-segments", "thm-geometric-lemma", "thm-jacquet-irreducible-admissible", "thm-bz-functors-finite-length"]
order = 11
+++
Let $F$ be a non-archimedean local field of characteristic zero and
$N \ge 1$. An irreducible smooth representation $\pi$ of $\GL_N(F)$ is
tempered if and only if $\pi \cong \delta_1 \times \dots \times \delta_h$ for
irreducible square-integrable representations $\delta_i$ of $\GL_{n_i}(F)$
with $\sum n_i = N$. This is the classical description of the tempered dual
of $\GL_N$ (Jacquet; Bernstein–Zelevinsky). It rests on
[thm-bz-finiteness], [thm-bz-functors-finite-length],
[thm-jacquet-irreducible-admissible], the geometric lemma [thm-geometric-lemma] and
the segment classification [thm-zelevinsky-segments].
