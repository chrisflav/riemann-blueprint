+++
kind  = "lemma"
title = "Served twists bound the sums over primes"
lean  = ["Formalism.L2.G.ServT.closed_servF_of_servT_of_dGamSize", "Formalism.MainNotions.Pk.sum_over_primes_service"]
order = 10
+++
Each lattice $u$ of a member of a family carries a positive integer $D(u)$;
*we read* it as a discriminant. Say the member satisfies the *size bound*
if $\log D(u) \le C f N\log(fN)$ for all $u$, with $f$ and $N$ the size
parameters of the family.

Let $\mathcal C$ be a class of families with a choice of twists that is
served (as in [thm-twisted-admissibility]), and suppose that the
members of its families eventually satisfy the size bound. Then they
eventually satisfy the bound for sums over primes that the comparison
between twisted and untwisted members requires. *It is not clear* from the
statement which sum over primes this is.
