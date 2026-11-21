+++
id    = "prop-local-estimate-from-chain"
kind  = "proposition"
title = "The local estimate from the chain bound"
lean  = ["Formalism.MainNotions.PairMembershipBlocks.stmtE_of_chain"]
order = 10
+++
Consider polynomials $A_i$ over a discrete valuation ring of residue
characteristic $p$, supported on the variables attached to the letters of a
valid system of frames of rank $r$, together with signed chain data tied to
the frames. The *chain bound* is a bound for the valuations of the
coefficients produced from such $A_i$ by the chain construction. If the
chain bound holds, then every member satisfies the local estimate at inert
primes ([thm-local-estimate-inert-primes]).

*It is not clear* from the statements what the chain construction computes;
we name the bound after it.
