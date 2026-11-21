+++
id    = "prop-local-estimate-from-three-steps"
kind  = "proposition"
title = "The local estimate from three steps"
lean  = ["Formalism.MainNotions.PairMembershipBlocks.stmtE_of_last"]
order = 10
+++
Suppose that:

* the *operator step* holds: applying a derivation $\partial/\partial x$, a
  multiplication by $x$, or their product to the polynomials of the local
  construction keeps them within the bounds for their degrees and
  valuations;
* the plane bound of [prop-local-estimate-from-plane] holds;
* the *arithmetic step* holds for all large constants.

Then every member satisfies the local estimate at inert primes.
