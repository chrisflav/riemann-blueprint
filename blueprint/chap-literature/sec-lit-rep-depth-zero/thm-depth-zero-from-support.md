+++
kind  = "theorem"
title = "Depth zero is detected on the cuspidal support"
lean  = ["GlobalTheory.DepthZeroPass.depthZeroInduction", "GlobalTheory.Published.DepthZeroInduction"]
uses  = ["thm-bz-finiteness", "thm-geometric-lemma"]
order = 5
+++
Let $F$ be a non-archimedean local field of characteristic zero. If every
member of the cuspidal support of an irreducible representation $\pi$ of
$\GL_n(F)$ has depth zero, then $\pi$ has depth zero: it has a non-zero
vector fixed by the first principal congruence subgroup. This is the
converse of [thm-depth-zero-support] (Moy–Prasad), stated in terms of the
Bernstein–Zelevinsky cuspidal support ([thm-bz-finiteness],
[thm-geometric-lemma]).
