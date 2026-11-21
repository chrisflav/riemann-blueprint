+++
kind = "proof"
of   = "lem-local-models-constructed-points"
uses = ["thm-hasse-norm-quadratic", "lem-inert-theta-admissibility-cm",
        "lem-admissibility-each-place"]
+++

A standard construction gives matching local data at every place for every
tuple $\mu$ in use, with the twisted forms normalised at the reference tuple
$\mu_0$, and its stabilisers at step zero are trivial. At each place where a
model is needed, take the lattice chain given by the matching datum and the
$l$-adic CM curve at that place; elsewhere take the chain of the lattices
themselves. The comparison condition holds by construction, and
[lem-admissibility-each-place] shows, using the admissibility of theta data
at inert primes ([lem-inert-theta-admissibility-cm]), that the chain is
admissible. This gives local models for the standard construction itself.
They carry over to the point, whose division lattices and heights differ
only by a change that does not affect the models.
