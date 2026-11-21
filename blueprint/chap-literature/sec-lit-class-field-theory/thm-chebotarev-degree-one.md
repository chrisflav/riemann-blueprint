+++
kind  = "theorem"
title = "Chebotarev's theorem, existence of degree-one primes"
provenance = "modified"
source = "special case of Chebotarev [chebotarev-1926]"
lean  = ["GlobalTheory.Published.ChebotarevDegreeOne", "GlobalTheory.Published.chebotarevDegreeOne'"]
order = 5
+++
Let $L/F$ be a finite Galois extension of number fields, $g \in \Gal(L/F)$ and
$S$ a finite set of primes of $F$. Then there is a prime $v \notin S$ of
absolute residue degree one, unramified in $L$, whose Frobenius at some prime
above it is $g$.

This is a weak form of the density theorem: it asks only
for one such prime outside a finite set, not for a density.
