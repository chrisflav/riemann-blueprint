+++
kind = "proof"
of   = "thm-family-data-exists"
uses = ["thm-family-membership-admissible-data", "thm-twisting-index-and-archimedean-bounds",
        "thm-basic-conditions-from-local-parameters", "thm-family-conditions-from-basic",
        "thm-family-sha-error-bound", "thm-theta-functionals-separate",
        "thm-rational-test-vectors-theta", "thm-indefinite-slope-bound",
        "thm-inner-form-multiplicities-equal", "thm-downward-theta-lift-nonvanishing"]
+++
We build the families, check a short list of basic conditions, and derive
the full list of family hypotheses from them.

1. *Members.* Siegel's mass formula for standard hermitian lattices over
   CM fields, in the form of an explicit ratio involving $L(M, \eta^M)$,
   gives the members of the families and admissible data for them
   ([thm-family-membership-admissible-data]). One hypothesis here is that
   cuspidal multiplicities agree on unitary groups that are isomorphic at
   every finite place. [thm-inner-form-multiplicities-equal] proves it.
2. *Local estimates.* Integral models of unitary Shimura varieties of PEL
   type bound the depth of the local data at every prime. Explicit
   exponents bound the index at the twisting places, and the archimedean
   weights are bounded below ([thm-twisting-index-and-archimedean-bounds]).
3. *Basic conditions.* With a system of local parameters, the families
   satisfy twelve basic conditions
   ([thm-basic-conditions-from-local-parameters]).
4. *Theta lifts.* Howe duality at unramified places and the Siegel–Weil
   formula show that theta functionals separate vectors
   ([thm-theta-functionals-separate]). Test vectors for twisted theta lifts
   take values in a number field, up to one constant and roots of unity
   ([thm-rational-test-vectors-theta]). Downward theta lifts do not vanish
   ([thm-downward-theta-lift-nonvanishing]).
5. *Slopes on the indefinite side.* [thm-indefinite-slope-bound] proves a
   slope inequality for the indefinite unitary groups. It takes as
   hypotheses five arithmetic statements about $L$-values and a lower bound
   for $L$-values, and a related step takes as hypothesis that certain Hecke
   $L$-values do not vanish ([thm-witt-tower-square-ratios]). The main
   theorems carry no hypotheses, so these are proved further up the
   argument; *it is not clear* where.
6. *All conditions.* The basic conditions imply the full list of family
   hypotheses ([thm-family-conditions-from-basic]). The main estimate there
   is an almost-orthogonality bound
   $|K_0(u,u')|^2 \le (1 + b^{-6})\,d_u d_{u'}/D^*$ for distinct types $u \ne u'$.
   It rests on Siegel–Weil mass data, uniqueness of Bessel models across a
   large gap of weights, and archimedean models. The spectral setting needs
   rank at least $1801$, and consecutive highest weights that differ by at
   least $16r^{19}$.
7. *The error term.* The Tate–Shafarevich error bound holds
   ([thm-family-sha-error-bound]), with exponent budget
   $E_J = 30\,t\,m\,b\,L^2 + 2mb$ at the twisting places. The bound at the
   primes $2$ and $3$ comes from the local parameters.

The covolume bound comes from arithmetic intersection theory
([thm-covolume-bound]).
