+++
kind = "proof"
of   = "thm-sha-error-from-congruence-bounds"
uses = ["thm-bloch-kato-local", "thm-chebotarev-degree-one-frobenius", "prop-congruence-bounds-all-primes", "prop-congruence-bound-auxiliary-primes", "thm-fontaine-bcris", "thm-artin-reciprocity", "thm-congruence-module-selmer-bound", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness-padic", "thm-tate-local-duality-l-adic"]
+++
The error $\eta_j$ of the $j$-th member is a weighted sum, over the twisted
places $w$, of the errors $\eta_i$ of the local data at $w$. Cut every member
to its good eigensystems. At the auxiliary primes $g_0, g_1$,
[prop-congruence-bound-auxiliary-primes] bounds $\eta_i$. At every other prime,
[prop-congruence-bounds-all-primes] bounds the congruence
valuations $\delta_\pi$ by $s_\pi + V_l + v_l(h_E)$ plus small errors, and
bounds $s_\pi$. Summing over local data, with the multiplicities bounded by
the ranks, gives the bound of [def-sha-error-term]. The summation uses local
Tate duality, the Euler characteristic formula, Chebotarev's theorem,
Fontaine's period ring and a global index theorem for lattices
([thm-congruence-module-selmer-bound]).
