+++
kind = "proof"
of   = "prop-congruence-bound-auxiliary-pair"
uses = ["thm-bloch-kato-local", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one",
        "thm-fontaine-bcris", "thm-artin-reciprocity", "thm-congruence-module-selmer-bound",
        "thm-tate-euler-characteristic-l-adic", "thm-tate-local-finiteness-padic",
        "thm-tate-local-duality-l-adic", "thm-lifting-deep-weights"]
+++
Check that the Galois representations $r_\pi$ of the member and their parts
$\rho_\pi$ satisfy a list of local conditions: an index condition away from
the types, Iwahori admissibility, small Selmer groups at the twisted places,
Hodge–Tate weights in windows at $q$ and $d$, compatibility of Fontaine's
functor with sums, tame generators at $q$ and $d$, and a polynomial bound on
the parameters. The check uses
[Chebotarev's theorem](@thm-chebotarev-degree-one-frobenius), the
[theorem on primes of degree one](@thm-chebotarev-degree-one), and the
global index theorem for lattices ([thm-congruence-module-selmer-bound]).
Under these conditions the bound holds for any $C \ge 2080$ and any $Q$ with
$Q(f, r, t) \ge 260 f^2t^2(r+t)$. Bound the lifting exponents at $q$ and $d$
with [thm-lifting-deep-weights], and convert them into Selmer lengths with
the [local theory of Bloch and Kato](@thm-bloch-kato-local),
[local Tate duality](@thm-tate-local-duality-l-adic) and the
[Euler characteristic formula](@thm-tate-euler-characteristic-l-adic).
[Global Artin reciprocity](@thm-artin-reciprocity) relates the characters at
the two primes.
