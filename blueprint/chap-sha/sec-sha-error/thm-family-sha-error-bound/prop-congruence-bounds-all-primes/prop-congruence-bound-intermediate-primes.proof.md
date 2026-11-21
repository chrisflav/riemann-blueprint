+++
kind = "proof"
of   = "prop-congruence-bound-intermediate-primes"
uses = ["thm-bloch-kato-local", "thm-chebotarev-degree-one", "thm-fontaine-bcris", "thm-artin-reciprocity", "thm-congruence-module-selmer-bound", "thm-tate-euler-characteristic-global-places", "thm-tate-local-finiteness", "thm-lifting-clustered-weights", "thm-tate-local-duality-global-places", "prop-lifting-ramified-coefficients"]
+++
At inert primes, the local lifting bound [thm-lifting-clustered-weights]
bounds the cokernels of the maps on finite cohomology. When the coefficients
are ramified, [prop-lifting-ramified-coefficients] does the same.
[Local Tate duality](@thm-tate-local-duality-global-places) and the
[Euler characteristic formula](@thm-tate-euler-characteristic-global-places) turn
these cokernels into the Selmer and local lengths, and
[Chebotarev's theorem](@thm-chebotarev-degree-one) and the global
index theorem for lattices ([thm-congruence-module-selmer-bound]) sum them.
