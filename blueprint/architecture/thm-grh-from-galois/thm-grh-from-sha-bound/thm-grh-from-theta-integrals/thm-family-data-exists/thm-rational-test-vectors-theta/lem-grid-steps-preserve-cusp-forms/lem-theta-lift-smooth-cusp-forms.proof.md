+++
kind = "proof"
of   = "lem-theta-lift-smooth-cusp-forms"
uses = ["thm-casselman-wallach", "thm-cusp-bounded-unitary", "thm-cusp-rapid-decay",
        "thm-discrete-series-frame-independent", "thm-discrete-series-exist-upq",
        "thm-hc-modules-unitary", "thm-hasse-norm-quadratic", "thm-hc-k-finite-vectors"]
+++
For each of the five kinds of arrow, three things are checked. The kernel
times the cusp form is integrable, because cusp forms are bounded
[thm-cusp-bounded-unitary] and decay rapidly [thm-cusp-rapid-decay]. The lift is a smooth
automorphic form. It is cuspidal, and its archimedean type is the expected
one, by uniqueness of discrete series with given infinitesimal character
[thm-discrete-series-frame-independent], $K$-finiteness
[thm-hc-k-finite-vectors] and the Casselman–Wallach theorem
[thm-casselman-wallach].
