+++
id    = "thm-family-sha-error-bound"
kind  = "theorem"
title = "The Tate–Shafarevich error bound for the families"
provenance = "new"
lean  = ["GlobalTheory.NLink.Final.mainTheorem", "UpperTheory.GalC.final_alt_alt"]
uses = ["def-local-parameters"]
order = 130
+++
Fix a system of local parameters ([def-local-parameters]) and a
constant $c$, and consider the classes of families of [def-family-data]
built from them.

We use the following notation for a member at scale $x$, with auxiliary CM
field $E$. A *local datum* $i$ is a prime $l$, a place $w$ of $E$ and a finite
set of Hecke eigensystems $\pi$ with values in the ring of integers $O$ of a
finite extension of $\Q_l$; each good $\pi$ has a Galois representation
$\rho_\pi : G_E \to \GL_r(O)$. Write

* $\delta_\pi$ for the *congruence valuation*: the least $l$-adic valuation of
  $f(\pi)$, $f$ in the congruence ideal of the Hecke algebra at $i$;
* $s_\pi$ for the length of a Bloch–Kato Selmer group attached to $\rho_\pi$;
* $V_l = \sum_{0<e<t}\mathrm{len}\,Ш^1_l(E, e)$, and $h_E$ for the class
  number of $E$.

Suppose the *bound at $2$ and $3$*: there is $C$ such that for all large $x$,
every member, every local datum at a twisted place with $l = 2$, or with
$l = 3$ when $3$ is not one of the small primes of $E$, and every good $\pi$,
$$\delta_\pi \le s_\pi + V_l + v_l(h_E) + l^{-2} + C f m b\log x + C x^C\Lambda^2 ,$$
where $f, m, b$ are size parameters of the family as in [def-sha-error-term]
and $\Lambda$ is a further size parameter. Then these classes satisfy the
Tate–Shafarevich error bound ([def-sha-error-term]).
