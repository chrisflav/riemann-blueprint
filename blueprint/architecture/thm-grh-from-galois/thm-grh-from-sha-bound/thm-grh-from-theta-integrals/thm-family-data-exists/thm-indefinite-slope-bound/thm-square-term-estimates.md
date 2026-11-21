+++
kind  = "theorem"
title = "Estimates for the leading square term"
lean  = ["GlobalTheory.SqTop.square_top_term_joined_estimates",
         "GlobalTheory.T.square_leading_term_bound"]
uses  = ["thm-howe-duality-archimedean-trivial", "thm-grh-from-theta-integrals"]
order = 1
+++
Assume Howe duality for real unitary dual pairs ([thm-howe-duality-archimedean-trivial]), the
published results of [thm-grh-from-theta-integrals], the step identities
of theta towers ([def-theta-tower-step]), the absolute value of the
functional equation of Hecke $L$-functions, and the arithmetic inputs on
toric denominators, lattice norm transport, zeta denominators and
reflection listed in [thm-indefinite-slope-bound]. Then for all
large scales, at every node $(i, j)$ of the grid and every
$1 \le s \le h$ ($h$ half the rank):

* the values $\Lambda(s)$ of the Hecke $L$-functions are nonzero, and their
  algebraic parts exist and are algebraic;
* their denominators $n_l$ are supported on finitely many primes, are
  nonnegative, and $\sum_{l \in S} n_l \log l$ is bounded by an explicit
  function of $C$, $x$ and $b$ for every finite set $S$;
* the bottom theta triples and bottom pairs exist, the bottom theta lifts
  do not vanish, and the bottom constants are small;
* the Witt tower identity of [thm-witt-tower-square-ratios] holds;
* at every place $w$ of the field of the family, the valuation of each
  ratio of square constants is nonzero and at most the sum of the
  valuations of the $L$-values and their denominators, with explicit
  multiplicities $1, 4, 5, 2h, 6$ and a term from the conductor.

The last item is the one used: it bounds the square ratios, place by place,
by special values of $L$-functions.
