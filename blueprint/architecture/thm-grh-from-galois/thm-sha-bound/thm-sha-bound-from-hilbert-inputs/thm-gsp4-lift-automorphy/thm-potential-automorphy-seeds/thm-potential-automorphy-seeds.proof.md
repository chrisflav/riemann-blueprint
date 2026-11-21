+++
kind = "proof"
of   = "thm-potential-automorphy-seeds"
uses = ["thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-cusp-bounded-gl", "thm-multiplicity-one-gl",
        "thm-geometric-lemma-filtration", "thm-hasse-norm-quadratic", "thm-automorphic-induction-quadratic", "thm-jacquet-irreducible-admissible",
        "thm-jacquet-shalika-strong-mult-one", "thm-seeds-from-mixed-congruences", "thm-local-parameters-exist"]
+++
Apply [thm-seeds-from-mixed-congruences]. Its extra inputs are the theorems on Eisenstein series
of weight one and on lifts of the Hasse invariant over totally real fields,
which are published, and automorphy
of the 4-dimensional representations built from mixed seeds. The latter
follows from quadratic base change from real to imaginary quadratic fields,
cyclic base change in rank two (both among the inputs for Hilbert modular
forms) and automorphic induction ([thm-automorphic-induction-quadratic]).
