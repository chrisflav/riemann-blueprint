+++
kind  = "definition"
title = "Scale and size data of a member"
provenance = "new"
lean  = ["Formalism.BasicNotions.Scale", "Formalism.BasicNotions.SizeData₂"]
uses  = ["def-family-member", "def-harish-chandra-parameters"]
order = 6
+++
A *scale* is a triple $(x, \varepsilon, J)$ with $x > 1$,
$0 < \varepsilon < 1/52$ and $J \ge 1$. It determines
$$b = e^{x^\varepsilon},\qquad a = x\,b,\qquad X' = e^{x^{\varepsilon/3}},\qquad b' = a/X'.$$

*Size data* for a member $D$ ([def-family-member]) at a scale consist of:

* for each top element $\tau$ of the CM type, integers
  $a_\tau \in [a, a + a/(k x^{13})]$ and $b_\tau \ge b'$, which fix the extreme
  entries of the parameter at $\tau$: $u_1 = a_\tau + \tfrac{k-1}{2}$ and
  $u_k = -b_\tau - \tfrac{k-1}{2}$ ([def-harish-chandra-parameters]); all
  entries $b_j$ are at most $b^2$;
* a finite set of places of the coefficient field and, at each of them,
  local quantities (gains along the chain, local error terms and degrees).
  They vanish at places above the auxiliary primes $g_0, g_1$, at primes
  that are neither signal nor inert ([def-auxiliary-field-data]), and,
  for some of them, above $X'' = a x n/b'$;
* a set of dropped primes, not containing any level prime $T_u$;
* the value $L'/L(1, \chi_K)$ for the quadratic character $\chi_K$ of
  $K = \Q(\sqrt{-d})$;
* size ties to the auxiliary field: the order $o$ of $\psi$ and $Q/4n$
  are at most $x^{\varepsilon/100}$, every odd prime below
  $x^{\varepsilon/5J}$ splits in $K$, and the thick elements have density
  $|T_2|/n \in (0, 1]$.

So the archimedean weights of a member have size $a = x\,e^{x^\varepsilon}$,
the number that appears in the slope data ([def-slope-data]).
