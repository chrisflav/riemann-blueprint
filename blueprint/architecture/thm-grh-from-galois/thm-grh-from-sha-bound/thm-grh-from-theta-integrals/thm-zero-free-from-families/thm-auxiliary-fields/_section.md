+++
id    = "thm-auxiliary-fields"
kind  = "theorem"
title = "Auxiliary CM fields"
provenance = "new"
lean  = ["UpperTheory.Top.supplyChi", "UpperTheory.Top.GChi", "UpperTheory.Top.KerChi"]
uses  = ["def-sha-bound", "def-slope-data"]
order = 3
+++
Let $\psi$ be primitive of order $o$, and assume the Tate–Shafarevich bound
for $\psi$ with exponent $401$. Then there are scales $x$, filling windows
$[Y, Y^{3/2}]$ for arbitrarily large $Y$, with the following property. For
each such $x$ there is a Galois CM field $E$, abelian over $\Q$, such that:

* $E$ is a $\psi$-field of [def-sha-bound] for primes $q \equiv 3 \bmod 8$
  and $d \equiv 7 \bmod 16$; in particular $E \ni \sqrt{-q}, \sqrt{-d}$, and
  $[E : \Q]$ is about $x^{2+8\varepsilon}$;
* the primes used are equidistributed in $\Gal(E/\Q)$ up to
  $x^{-1+\varepsilon}$, and $|L'/L(1, \chi)| \le C\log x$ for the characters
  $\chi$ of $\Gal(E/\Q)$ that matter;
* the Tate–Shafarevich groups of $E$ satisfy the bound of
  [def-sha-bound] with $t = \lfloor x^{401}\rfloor$.

The field also comes with a CM type and two auxiliary primes of level, as
in the definition of [auxiliary CM fields](@def-auxiliary-field-data).
