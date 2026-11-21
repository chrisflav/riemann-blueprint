+++
id    = "functionals-separate-of-howe-unram-of-siegel-weil"
kind  = "theorem"
title = "Theta functionals separate vectors"
lean  = ["UpperTheory.Lit.functionalsSeparate_of_howeUnram_of_siegelWeil"]
uses  = ["published-siegel-weil-unitary-convergent", "thm-grh-from-theta-integrals"]
order = 110
+++
Assume the published results on unitary groups and theta lifts of
[thm-grh-from-theta-integrals], unramified Howe duality, and the Siegel–Weil
formula in its convergent range
([published-siegel-weil-unitary-convergent]). *Unramified Howe duality* is
taken in this form: if $\omega$ is the Weil representation of an unramified
dual pair $\U(V) \times \U(W)$ over a $p$-adic field and $s$ is its spherical
vector, then every vector fixed by the maximal compact subgroup of one group
lies in the span of the translates of $s$ under the other.

Then for every $\varepsilon$ and every constant $C_F \ge 6510$ the following
holds once the scale $x$ is large. Take a member of a family at scale $x$,
an auxiliary set of real data for it, a grid of hermitian spaces and Weil
representations over these data, and a lattice volume of the right type.
For every nonzero vector $w$ in the space of the first group of the grid
there are a real test vector $\rho$ and a linear functional $\xi$ on the
space of theta coefficients such that, for every nonzero $t$ in the
trivial-character eigenspace, some theta coefficient $\Psi$ and some
Schwartz datum $\Phi$ give a convergent theta integral of the form
$(w, t)$ with nonzero value.

In words: theta integrals detect every nonzero vector. *It is not clear*
which automorphic forms the vectors $w$ and $t$ stand for; we read them as
the cusp forms on the bottom group of the theta tower.
