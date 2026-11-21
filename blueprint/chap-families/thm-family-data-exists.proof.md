+++
kind = "proof"
of   = "thm-family-data-exists"
uses = ["thm-family-membership-admissible-data", "thm-twisting-index-and-archimedean-bounds",
        "thm-basic-conditions-from-local-parameters", "thm-family-conditions-from-basic",
        "thm-family-sha-error-bound", "thm-theta-functionals-separate",
        "thm-rational-test-vectors-theta", "thm-indefinite-slope-bound",
        "thm-inner-form-multiplicities-equal", "thm-downward-theta-lift-nonvanishing",
        "thm-theta-tower-step-identities", "thm-covolume-bound", "thm-local-parameters-exist",
        "thm-siegel-weil-definite", "thm-doubling-method", "thm-rallis-inner-product",
        "thm-labesse-base-change", "thm-clozel-purity", "thm-non-endoscopic-hypotheses-hold",
        "thm-witt-tower-square-ratios", "thm-square-term-estimates"]
+++
Fix the system of local parameters of [thm-local-parameters-exist]. We
build the families from it, check twelve basic conditions, and derive the
family hypotheses from them, in seven steps.

1. *Members.* Siegel's mass formula for standard hermitian lattices over
   CM fields, as an explicit ratio involving $L(M, \eta^M)$, gives the
   members of the families and admissible data for them
   ([thm-family-membership-admissible-data]). One input is that cuspidal
   multiplicities agree on unitary groups that are isomorphic at every
   finite place ([thm-inner-form-multiplicities-equal]).
2. *Local estimates.* Integral models of unitary Shimura varieties bound
   the depth of the local data at every prime, explicit exponents bound the
   index at the twisting places, and the archimedean weights are bounded
   below ([thm-twisting-index-and-archimedean-bounds]).
3. *Basic conditions.* The families satisfy twelve basic conditions at
   every admissible datum ([thm-basic-conditions-from-local-parameters]).
4. *Theta lifts* ([chap-theta]). Howe duality at unramified places and the
   Siegel–Weil formula show that theta functionals separate vectors
   ([thm-theta-functionals-separate]). Test vectors for twisted theta lifts
   take values in a number field, up to one constant and roots of unity
   ([thm-rational-test-vectors-theta]). Downward theta lifts do not vanish
   ([thm-downward-theta-lift-nonvanishing]).
5. *Slopes on the indefinite side* ([chap-theta]). A slope inequality holds
   for the indefinite unitary groups ([thm-indefinite-slope-bound]). Its
   proof uses arithmetic statements about $L$-values in the non-endoscopic
   case ([thm-non-endoscopic-hypotheses-hold]), the non-vanishing of Hecke
   $L$-values that the estimates for square terms give
   ([thm-witt-tower-square-ratios], [thm-square-term-estimates]), and the
   lower bound on archimedean weights of step 2.
6. *All conditions.* The basic conditions, the covolume bound of
   [chap-heights] ([thm-covolume-bound]) and a functional condition, which
   comes from the separation of step 4 and the bounds of step 2, imply the full list of family conditions
   ([thm-family-conditions-from-basic]). The main estimate there is the
   almost-orthogonality bound
   $|K_0(u,u')|^2 \le (1 + b^{-6})\,d_u d_{u'}/D^*$ for distinct types
   $u \ne u'$.
7. *The error term* ([chap-sha]). The error term of each member is bounded
   by lengths of Tate–Shafarevich groups ([thm-family-sha-error-bound]);
   the bound at the primes $2$ and $3$ comes from the local parameters.

Throughout, the proof uses the step identities of theta towers
([thm-theta-tower-step-identities]) and published results on unitary
groups and theta lifts, among them the Siegel–Weil formula
[thm-siegel-weil-definite], the doubling method [thm-doubling-method], the
Rallis inner product formula [thm-rallis-inner-product], Labesse's base
change [thm-labesse-base-change] and Clozel's purity theorem
[thm-clozel-purity]. The Galois representations of the hypothesis enter in
steps 1 and 2.
