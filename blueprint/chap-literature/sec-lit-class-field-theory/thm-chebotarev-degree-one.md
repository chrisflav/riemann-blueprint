+++
kind  = "theorem"
title = "Chebotarev's theorem, existence of degree-one primes"
provenance = "modified"
source = "special case of Chebotarev [chebotarev-1926]"
lean  = ["GlobalTheory.Published.ChebotarevDegreeOne", "GlobalTheory.Published.chebotarevDegreeOne'",
         "GlobalTheory.Published.cheb_holds", "GlobalTheory.TwSys.Cheb"]
order = 4
+++
Let $L/F$ be a finite Galois extension of number fields, $g \in \Gal(L/F)$ and
$S$ a finite set of primes of $F$. Then there is a prime $v \notin S$ of
absolute residue degree one, unramified in $L$, whose Frobenius at some prime
above it is $g$.

In profinite form: let $\Omega$ be an algebraic closure of $F$, $U$ an open
normal subgroup of $\Gal(\Omega/F)$, $g \in \Gal(\Omega/F)$ and $A$ a finite
set of primes. Then there is a prime $v \notin A$ of $F$, of degree one over
$\Q$ and unramified over $\Q$, with a place above it whose inertia group lies
in $U$ and whose Frobenius $\sigma$ satisfies $\sigma g^{-1} \in U$.

This is a weak form of the density theorem: it asks only
for one such prime outside a finite set, not for a density.
