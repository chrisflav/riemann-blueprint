+++
kind  = "lemma"
title = "Orbit data at inert primes of odd order"
provenance = "new"
lean  = ["UpperTheory.OrbitFamilyRestriction.exists_rowFamS", "UpperTheory.exists_pkgCs_of_degree_bound_at_inert_primes", "UpperTheory.labelSetGeo_of_even_of_rankOK_of_not_dvd_discr"]
order = 2
+++
In the setting of [prop-local-data-unitary-shimura-points], take a point of
$X$ and a prime $l$ that is inert, of odd order $d_l$. Let $a(\tau, i)$ be
the weights attached to the complex embeddings $\tau$ of $E$, with
$0 \le i < m(\tau)$, decreasing in $i$. Here $m(\tau) = p$ or $q$ according
as $\tau$ lies in the CM type or not.

1. Suppose a degree hypothesis holds and $n_W \ge f\big((i_0+1)(k-1) + 4r\big)$.
   Then there are a set $Z$ of representatives of the Frobenius orbits and a
   bijection $\tau : Z \times \Z/2d_l \to \mathrm{Hom}(E, \C)$, with
   $\tau(o, s)$ in the CM type exactly when $s$ is even. There are also
   flags of ranks $m(\tau(o, s))$ whose valuations, at precision $n_W$, are
   bounded below in blocks by $\nu$.
2. Suppose the weights are non-negative, $a(\tau, 0) \le s(l-1)$ for every
   $\tau$, and $4rsf \le n_W$. Then the same data exist with the simpler
   block condition.
