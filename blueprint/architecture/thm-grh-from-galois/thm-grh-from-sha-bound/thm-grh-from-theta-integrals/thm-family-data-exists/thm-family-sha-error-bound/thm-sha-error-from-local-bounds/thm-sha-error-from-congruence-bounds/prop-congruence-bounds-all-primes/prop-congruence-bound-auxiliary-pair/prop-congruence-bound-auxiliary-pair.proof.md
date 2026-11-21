+++
kind = "proof"
of   = "prop-congruence-bound-auxiliary-pair"
uses = ["thm-bloch-kato-local", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-fontaine-bcris", "thm-artin-reciprocity", "thm-congruence-module-selmer-bound", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness-padic", "thm-tate-local-duality-l-adic", "prop-selmer-bound-twisted-places"]
+++
Check the local conditions at $q$ and $d$ (the weight windows at these
primes, tame generators, Iwahori admissibility, and a polynomial bound on
the parameters) and apply
[prop-selmer-bound-twisted-places]. The proof uses
Chebotarev's theorem, the theorem on primes of degree one, and the global
index theorem for lattices.
