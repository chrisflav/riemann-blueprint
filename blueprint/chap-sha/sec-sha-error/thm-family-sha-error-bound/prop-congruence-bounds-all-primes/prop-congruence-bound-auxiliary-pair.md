+++
kind  = "proposition"
title = "Congruence bound at the primes of the auxiliary pair"
provenance = "new"
lean  = ["GlobalTheory.T.embedding_jumps_aux2_of_setup", "GlobalTheory.TheoremBQD.main_alt_alt",
         "GlobalTheory.T.twistedPlace_selmerLengthBound_of_localDuality",
         "GlobalTheory.TwistedPlaceBound.closing"]
order = 1
+++
There are a constant $C$ and a polynomial $Q$ in three variables such that
every member satisfying the setup of the family has the following property.
Let $i$ be a local datum at a twisted place over $l \in \{q, d\}$, the primes
of the auxiliary pair of [def-sha-bound], with $l > x^{2C_t + 5}$, and let
$\pi$ be good with finite Selmer group and with $Ш^1_l(E, e)$ finite for
$0 < e < t$. Then
$$\delta_\pi \le B(l) + V_l + v_l(h_E) + s_\pi + l^{-2},$$
where $B(l)$ is an explicit bound in terms of $C$, $Q$ evaluated at the size
parameters, and $l$.
