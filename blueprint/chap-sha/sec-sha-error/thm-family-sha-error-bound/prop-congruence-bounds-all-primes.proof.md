+++
kind = "proof"
of   = "prop-congruence-bounds-all-primes"
uses = ["thm-bhatt-scholze-coefficients", "thm-bhatt-scholze-crystalline-lattices", "thm-bloch-kato-local", "thm-chebotarev-degree-one-frobenius", "prop-congruence-bound-auxiliary-pair", "prop-congruence-bound-large-primes", "thm-fontaine-bcris", "thm-artin-reciprocity", "thm-congruence-module-selmer-bound", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness-padic", "thm-tate-local-duality-l-adic", "prop-congruence-bound-intermediate-primes", "thm-wach-lifting-theorem"]
+++
Combine four local results. The local lifting theorem
([thm-wach-lifting-theorem]) supplies the constants. The
intermediate range is [prop-congruence-bound-intermediate-primes], the large primes
are [prop-congruence-bound-large-primes], and the primes $q, d$ are
[prop-congruence-bound-auxiliary-pair]. At $2$ and $3$ the bound is the
hypothesis; at the other small primes it follows in the same way. The
lattices come from the theorem of Bhatt and Scholze
([thm-bhatt-scholze-crystalline-lattices]), and the global index
theorem for lattices ([thm-congruence-module-selmer-bound]) assembles the
local lengths.
