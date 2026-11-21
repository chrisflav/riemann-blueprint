+++
kind = "proof"
of   = "thm-local-estimate-inert-primes"
+++
The proof reduces the estimate in four steps to statements about the
polynomials of the local construction, each proved directly.

1. *Membership.* A Gram-matrix estimate holds for every member with the
   explicit constants $26, 2, 24, 60$: it follows from a choice of test
   vectors, the membership of their images and a numerical bound. With it,
   the local estimate follows from the *membership condition*: for all
   constants $C_\Lambda, C_k, C_{\mathrm{rk}}, C_{\deg}$ for which the member
   is admitted and all large $C$, the polynomials produced by the local
   construction lie in the lattices that the estimate requires.
2. *Three steps.* The membership condition follows from the *operator step*
   (applying a derivation $\partial/\partial x$, a multiplication by $x$, or
   their product keeps the polynomials within the bounds for their degrees
   and valuations), the plane bound below, and the *arithmetic step*. The
   operator step and the bounds for words give the bound for words in the
   operators; the plane bound and the arithmetic step give, through a
   monomial form of an auxiliary lemma, the first half of the membership
   condition, and the bound for words gives the second. The operator step
   follows from substitution of letters, and the arithmetic step holds for
   every constant $C \ge 1$.
3. *Plane bound.* Consider polynomials $A_i$ over a discrete valuation ring
   of residue characteristic $p$, supported on the variables attached to the
   letters of a valid system of frames of rank $r$, with signed chain data
   tied to the frames. The *chain bound* bounds the valuations of the
   coefficients produced from such $A_i$ by the chain construction; it holds
   by a separate counting argument. The *level link* for the same data
   follows from the link at each level, the degree of the letters and the
   count of variables. Together they are the plane bound. *It is not clear*
   from the statements what the chain construction computes; we name the
   bound after it.
4. The restricted form follows from the local estimate by a criterion that
   restricts the constants.
