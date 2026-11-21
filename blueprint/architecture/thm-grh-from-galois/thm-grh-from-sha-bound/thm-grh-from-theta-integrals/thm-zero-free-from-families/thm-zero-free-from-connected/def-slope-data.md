+++
kind  = "definition"
title = "Slope data"
lean  = ["Formalism.MainNotions.ChainTied", "UpperTheory.Comparison₂.CoreAtH", "Formalism.HC.EAtH"]
order = 2
+++
Let $E$ be an auxiliary CM field at scale $x$, and put $a = x\,e^{x^\varepsilon}$
and $b = e^{x^\varepsilon}$. *Slope data* at $x$ consist of:

* lattices with slopes $\mu_N, \mu_{\max,N}, \mu_M, \mu_{CC}, \mu_{\min,CC}$ and
  heights, attached to the members of a family;
* an identity that writes the sum
  $$\sum_{p \text{ inert in } E}2\log p\sum_i\Big(\frac{a}{p^i} - w\Big)_+$$
  of von Mangoldt type over the primes inert in $E$ as a sum of such
  contributions over the members of the family;
* a slope inequality: the weighted mean of the slopes, less
  $\log|W|$ and an error of order the heights, is at most $\mu_{CC}$, with
  bounds on the largest and smallest slopes;
* divisibility, comparison and counting conditions, including a term
  $\gamma + \log(\pi/v) - L'/L(1, \chi)$ of the shape of the Chowla–Selberg
  formula;
* conditions on $E$: the primes used are equidistributed in $\Gal(E/\Q)$
  with weights $4/(3o+1)$ or $3/(3o+1)$, and $|L'/L(1,\chi)| \le C\log x$
  for the characters that matter.

*We read* the slope inequality as an instance of Bost's slope inequality
for hermitian lattices, which the announcement names. *It is not clear*
how the members of a family produce the slopes.
