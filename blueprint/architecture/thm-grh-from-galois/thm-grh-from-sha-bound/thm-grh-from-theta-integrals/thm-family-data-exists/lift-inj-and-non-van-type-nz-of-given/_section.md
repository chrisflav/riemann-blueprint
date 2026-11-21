+++
id    = "lift-inj-and-non-van-type-nz-of-given"
kind  = "theorem"
title = "Downward theta lifts are nonzero and injective on eigenspaces"
lean  = ["GlobalTheory.Core.Rk.Exh.Top.downNe_k_of_hypotheses'",
         "GlobalTheory.Core.Rk.LiftOnto.liftInj_nonVan_typeNZ_of_hypotheses_alt",
         "GlobalTheory.T.downNe_of_eulerRight_doubling", "GlobalTheory.T.liftInj_and_nonVan_typeNZ_of_given"]
uses  = ["cusp-rapid-decay", "doubling-method-local-zeta-integrals", "hecke-l-partial-continuation",
         "unramified-doubling-gl"]
order = 120
+++
Assume rapid decay of cusp forms [cusp-rapid-decay], the local theory of
the doubling zeta integrals [doubling-method-local-zeta-integrals] and its
unramified computation [unramified-doubling-gl], meromorphic continuation
of partial Hecke $L$-functions [hecke-l-partial-continuation], and Howe
duality at unramified places. Let a family member carry, for each index
$i$, a pair of hermitian spaces $V_i$ and $W_i$ with the theta
correspondence between $\U(V_i)$ and $\U(W_i)$, satisfying the standing
hypotheses (good types, large gaps of the archimedean parameters
$\lambda_n - \lambda_{n+1} \ge 100r^4$, absolutely irreducible characters).
Then for each $i$:

* *non-vanishing:* every nonzero Hecke eigenform $y$ on $\U(V_i)$ whose Satake
  parameters at good places contain the segment
  $q_w^{(t-1)/2}\nu, \dots, q_w^{-(t-1)/2}\nu$, the other parameters having
  absolute value at most $q_w^{(r-1)/2}$, has a nonzero theta lift to
  $\U(W_i)$;
* *detection:* a good eigenform whose theta pairing vanishes is zero;
* *injectivity:* if two eigenforms $x, y$ have the same Hecke eigenvalues at
  good places, $x$ has nonzero theta pairing and $y$ is good, then $y$ has
  nonzero theta pairing unless $y = 0$.

The first step is the non-vanishing of the downward lift whenever the
partial $L$-function of the doubling method has the expected pole: this is
Rallis' tower argument in the form of Kudla and Rallis.
