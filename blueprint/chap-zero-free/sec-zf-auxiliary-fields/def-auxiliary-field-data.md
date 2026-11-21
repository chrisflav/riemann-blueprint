+++
kind  = "definition"
title = "Auxiliary CM fields and their Galois data"
provenance = "new"
lean  = ["Formalism.HC.Frame", "Formalism.HC.HostRaw", "Formalism.HC.HostDer", "Formalism.HC.HostAx",
         "Formalism.BasicNotions.Host", "Formalism.BasicNotions.PrimeClass",
         "Formalism.BasicNotions.primeClass", "Formalism.FrobeniusOrbits.HostHyp",
         "Formalism.FrobeniusOrbits.HGrp"]
order = 1
+++
Let $e \ge 2$, let $H_e = (\Z/2^{e+2})^\times/\{\pm 1\}$, a cyclic group of
order $2^e$, and let $A$ be a finite abelian group of order $n$ with a
surjection $h : A \to H_e$ and an element $a_0$ on whose multiples $h$ is
injective. Put $o = n/\mathrm{ord}(a_0)$ and
$$\Gamma = \{\pm1\} \times \{\pm1\} \times A, \qquad c = (-1, -1, 0).$$

An *auxiliary CM field* for these data consists of:

* primes $q \equiv 3 \bmod 8$ and $d \equiv 7 \bmod 16$ with $(-d/q) = 1$, and
  an integer $Q$ divisible by $2^{e+2}$, prime to $qd$, whose odd prime
  factors split in $K = \Q(\sqrt{-d})$;
* a Galois field $E \subset \Q(\zeta_{Qqd})$ containing $\sqrt{-q}$ and
  $\sqrt{-d}$, with an isomorphism $\Gal(E/\Q) \cong \Gamma$ under which the
  Artin map $(\Z/Qqd)^\times \to \Gamma$ sends $-1$ to $c$, has first two
  coordinates the quadratic characters of $\Q(\sqrt{-q})$ and
  $\Q(\sqrt{-d})$, and sends $u$ to an element whose third coordinate maps
  under $h$ to the class of $u$ modulo $2^{e+2}$;
* a CM type $\Phi$: the embeddings sending $\sqrt{-d}$ to $i\sqrt d$, with a
  chosen $\varphi_0 \in \Phi$;
* level data: a finite set of level primes containing two auxiliary primes
  $g_0, g_1$ and two primes $p \ne p'$ with $p \equiv p' \equiv 1 \bmod 15$; a
  primitive ideal $\mathfrak c$ of $K$ prime to the level and supported on
  primes split in $K$;
* sets of *top* and *thick* elements of $A$, which select elements of $\Phi$;
* size conditions: $Q \le n^2$, $o^{64} \le 2^e$, $q, d > 4rt + 1$ in terms of
  the ranks of [def-family-ranks], and every odd prime up to a given bound
  splits in $K$.

From these data one proves that $E$ is a CM field of degree $4n$ with
complex conjugation $c$ and maximal real subfield $F$ of degree $2n$, that
Frobenius at $p \nmid Qqd$ is the Artin image of $p$, that the relative
different of $E/K$ is $\mathfrak b\bar{\mathfrak b}$ with
$\mathfrak b + \bar{\mathfrak b} = 1$ and $\mathfrak b^{-1}$ unimodular for
the trace form, and bounds on the root discriminant $|d_E|^{1/[E:\Q]}$.

A prime $p \nmid Qqd$ is *split* if it splits in $K$. Otherwise its
Frobenius has first coordinates $(1,-1)$ or $(-1,-1)$; we call $p$ a
*signal* prime in the first case and *inert* in the second, where Frobenius
acts on $\Q(\sqrt{-q}, \sqrt{-d})$ as complex conjugation. Only signal and
inert primes contribute to the local size data of [def-family-scale]; *we
read* the primes "inert in $E$" of the slope data ([def-slope-data]) as the
inert primes in this sense.

*We read* $E$ as the $\psi$-field of [def-sha-bound]: $A$ is the Galois group
of its $2$-power and $\psi$ parts, and $o$ the order of $\psi$.
