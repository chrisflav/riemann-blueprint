+++
id    = "prop-local-data-unitary-shimura-points"
kind  = "proposition"
title = "Local data at the points of unitary Shimura varieties"
lean  = ["GlobalTheory.T.allGoodPrimeDepthDataExist_proof", "GlobalTheory.goodPrime_packages"]
order = 1
+++
Assume the estimate at unramified primes of
[lem-depth-bound-good-primes] for every prime. Let $E$ be a CM
field containing $\sqrt{-d}$, with $d \equiv 7 \bmod 16$ prime and $E$
unramified over its maximal real subfield. Let $L$ be a unimodular hermitian
$\mathcal O_E$-lattice of signature $(p, q)$. Let $X$ be the moduli scheme
of polarised abelian schemes with $\mathcal O_E$-action of this signature
and of a given level, which is a unitary Shimura variety. Let $c$ be a
coefficient field containing the images of $E$ and the roots of unity of
the level.

Then at every point of $X$ with values in a complete discrete valuation ring
there are local data of seven kinds: depth data at inert, split and large
primes, two kinds of data that relate Frobenius to complex conjugation, and
the two kinds of data at inert primes of [lem-orbit-data-inert-primes].
