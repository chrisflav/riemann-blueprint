+++
kind  = "theorem"
title = "The arithmetic Hilbert–Samuel theorem"
lean  = ["GlobalTheory.Published.ArithHilbertSamuel", "GlobalTheory.arithHilbertSamuel_of_principalisation", "UpperTheory.LiteratureTheorems.arith_hilbert_samuel_of_literature"]
uses  = ["def-local-parameters", "principalisation"]
order = 10
+++
Let $X$ be an arithmetic variety of relative dimension $D$ and $\bar L, \bar N$
hermitian line bundles on $X$, with $\bar L$ nef and $\bar L^{D+1} = a$. Then the
set of small sections of $L^m \otimes N$ is finite for large $m$, and
$$\log \#\{\text{small sections of } L^m \otimes N\} = \frac{a}{(D+1)!}\, m^{D+1} + o(m^{D+1}).$$

This is the arithmetic Hilbert–Samuel theorem of Gillet–Soulé, Abbes–Bouche
and Zhang (1992–1995). It holds under the hypotheses of
[thm-grh-from-sha-bound], for a system of local parameters
([def-local-parameters]), and uses principalisation ([principalisation]).
