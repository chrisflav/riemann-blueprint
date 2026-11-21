+++
kind = "proof"
of   = "seed-i-is-alt"
uses = ["car-u-alt", "cheb", "chebotarev-degree-one", "cusp-forms-bounded-gl", "cuspidal-multiplicity-one",
        "geometric-lemma-filtration", "hasse-norm-st", "ind-cs", "irreducible-admissible-gl",
        "jacquet-shalika-rigidity", "seed-ii-z-alt", "thm-local-parameters-exist"]
+++
Apply [seed-ii-z-alt]. Its extra inputs are the theorems on Eisenstein series
of weight one and on lifts of the Hasse invariant over totally real fields,
which are published, and automorphy
of the 4-dimensional representations built from mixed seeds. The latter
follows from quadratic base change from real to imaginary quadratic fields,
cyclic base change in rank two (both among the inputs for Hilbert modular
forms) and automorphic induction ([ind-cs]).
