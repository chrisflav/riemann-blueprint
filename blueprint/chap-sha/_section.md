+++
id    = "chap-sha"
kind  = "chapter"
title = "The Tate-Shafarevich bound"
uses  = ["chap-galois", "chap-literature"]
order = 7
+++
This chapter proves [thm-sha-bound] and shows where the rest of the proof uses it.
For a primitive Dirichlet character $\psi$ the $\psi$-fields $E$ are abelian
fields in a 2-power cyclotomic tower ([def-sha-bound]). The theorem says that
the Tate–Shafarevich groups $Ш^1_l(E, e)$ of the Tate twists
$\Q_l/\Z_l(-e)$, $0 < e < t = \lfloor x^{401}\rfloor$, are finite, and that
the sum of their lengths, weighted by $\log l$, is at most $e^{x^\varepsilon/2}$.
The families of definite unitary groups ([chap-families]) carry an error
term that these lengths control, and the bound keeps that term small.

The first four sections prove the bound. The Poitou–Tate sequence and the
Greenberg–Wiles formula bound $Ш^1_l(E, e)$ by the $\chi$-isotypic Selmer
groups of $\chi \otimes \Z_l(e)$, for the even characters $\chi$ of
$\Gal(E/\Q)$, and by the second cohomology of Tate twists, which
[sec-sha-h2] bounds through the homology of $\GL_n$ over rings of integers. The
Selmer groups are bounded case by case in $(l, e, \chi)$: by Kato's Euler
system for ordinary newforms ([sec-sha-kato], with the explicit reciprocity
law of [sec-sha-reciprocity]), by automorphy of lifts with values in
$\mathrm{GSp}_4$ ([sec-sha-gsp4]), by automorphy of 3-dimensional
representations through base change, and by vanishing for the trivial
character. The automorphy results use the Galois representations of
[chap-galois].

The last three sections show where the bound enters. By
[thm-family-sha-error-bound] the error term $\eta_j$ of each member of a
family is at most $d_j$ times the sum of a polynomial in the size
parameters and the same weighted sum of lengths of $Ш^1_l(E, e)$
([sec-sha-error]). Its proof bounds congruence modules prime by prime. A global index theorem, proved by
Ribet's construction, bounds a congruence module by local lengths, Selmer
groups, Tate–Shafarevich groups and the class number ([sec-sha-congruence]);
lifting theorems for crystalline lattices bound the local lengths
([sec-sha-lifting]). [thm-zero-free-from-families] then combines this error
bound with [thm-sha-bound].
