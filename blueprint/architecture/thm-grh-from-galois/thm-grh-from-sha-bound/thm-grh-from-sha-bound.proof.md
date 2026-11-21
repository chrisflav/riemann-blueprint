+++
kind = "proof"
of   = "thm-grh-from-sha-bound"
uses = ["thm-grh-from-theta-integrals", "chap-literature", "thm-theta-tower-step-identities",
        "thm-covolume-bound"]
+++
Collect the published results of [chap-literature]. A few need the
hypotheses.

* The local Langlands correspondence for $\GL_n$, in the weak form of
  [def-local-parameters], follows from the local parameters, the local
  converse theorem and the theory of Bernstein and Zelevinsky.
* The compatibility of Galois representations of unitary groups follows
  from [def-galois-reps-polarized].

Two further hypotheses of [thm-grh-from-theta-integrals] are proved in this
chapter:

* the step identities of theta towers ([thm-theta-tower-step-identities]),
  from the Siegel–Weil formula for definite unitary groups;
* the bound on covolumes ([thm-covolume-bound]), from a lower bound for the
  mean arithmetic volumes of automorphic line bundles on toroidal
  compactifications.

With these, the theorem is a case of [thm-grh-from-theta-integrals].
