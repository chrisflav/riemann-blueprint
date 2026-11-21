+++
kind = "proof"
of   = "cuspidal-lift-smooth-at-cusps"
uses = ["casselman-wallach", "cusp-bounded", "cusp-rapid-decay",
        "discrete-series-hermitian-unique", "discrete-series-upq-exists",
        "harish-chandra-modules", "hasse-norm-st", "k-finite-vectors-unitary"]
+++
For each of the five kinds of arrow, three things are checked. The kernel
times the cusp form is integrable, because cusp forms are bounded
[cusp-bounded] and decay rapidly [cusp-rapid-decay]. The lift is a smooth
automorphic form. It is cuspidal, and its archimedean type is the expected
one, by uniqueness of discrete series with given infinitesimal character
[discrete-series-hermitian-unique], $K$-finiteness
[k-finite-vectors-unitary] and the Casselman–Wallach theorem
[casselman-wallach].
