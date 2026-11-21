+++
id    = "prop-lifting-ramified-coefficients"
kind  = "proposition"
title = "Local lifting bound with ramified coefficients"
lean  = ["GlobalTheory.T.prv_twenty_five_of_blochKato_tateDuality_eulerChar", "GlobalTheory.ramifiedCoefficientChains_prv_twenty_five"]
uses  = ["thm-bloch-kato-local", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-duality-l-adic"]
order = 2
+++
Assume the local theory of Bloch and Kato, local Tate duality and the local
Euler characteristic formula. Then for every member the analogue of
[thm-lifting-clustered-weights] holds, with
constant $25$, for lattices whose coefficient field contains the $l$-th
roots of unity and for $l \ge 11$: the lifting exponent of
$H^1_f(T_1) \to H^1_f(T_2)$ is bounded by an explicit function of $l$, the
window sizes and the number of small weights.
