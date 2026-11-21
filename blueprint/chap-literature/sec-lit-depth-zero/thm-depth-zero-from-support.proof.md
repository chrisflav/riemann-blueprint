+++
kind = "proof"
of   = "thm-depth-zero-from-support"
uses = ["thm-bz-finiteness", "thm-geometric-lemma"]
+++
Let $\sigma_1, \dots, \sigma_r$ be the cuspidal support of $\pi$. By the
Bernstein–Zelevinsky theory [thm-bz-finiteness] and the geometric lemma
[thm-geometric-lemma], some Jacquet module of $\pi$ along a parabolic with
Levi $M = \prod_a \GL_{d_a}$ has $\sigma_1 \otimes \dots \otimes \sigma_r$ as a
subquotient. Each $\sigma_a$ has a vector fixed by its first congruence
subgroup, so this subquotient, and hence the Jacquet module, has a non-zero
vector fixed by the first congruence subgroup $M_1$ of $M$; the modulus
character is trivial on $M_1$. Since $\pi$ is admissible, Jacquet's lemma
lifts this vector to a vector of $\pi$ fixed by a pro-unipotent subgroup
that contains the first congruence subgroup of $\GL_n(F)$.
