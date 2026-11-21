+++
kind = "proof"
of   = "thm-automorphic-induction-quadratic"
uses = ["thm-hc-finiteness-gl", "thm-galois-reps-csd-above-l", "thm-cusp-bounded-gl", "thm-multiplicity-one-gl",
        "thm-cuspidal-spectrum-gl", "thm-artin-reciprocity", "thm-hasse-norm-quadratic", "thm-jacquet-shalika-strong-mult-one"]
+++
*We read* the proof as follows. The induced parameter is an automorphic representation of $\GL_4(\A_K)$ by
base change and descent along the cyclic extension $M/K$, using
[Artin reciprocity](@thm-artin-reciprocity) for the quadratic character
and the [Hasse norm theorem](@thm-hasse-norm-quadratic). It is cuspidal because the
condition on infinitesimal characters prevents $\pi$ from being isomorphic
to its conjugate, and [Jacquet–Shalika rigidity](@thm-jacquet-shalika-strong-mult-one)
with [multiplicity one](@thm-multiplicity-one-gl) excludes the other
decompositions.
