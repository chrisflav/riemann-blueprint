+++
kind = "proof"
of   = "ind-cs"
uses = ["automorphic-forms-finite-gl", "car-u-alt", "cusp-forms-bounded-gl", "cuspidal-multiplicity-one",
        "cuspidal-spectrum-gl", "global-artin-reciprocity", "hasse-norm-st", "jacquet-shalika-rigidity"]
+++
*We read* the proof as follows. The induced parameter is an automorphic representation of $\GL_4(\A_K)$ by
base change and descent along the cyclic extension $M/K$, using
[Artin reciprocity](@global-artin-reciprocity) for the quadratic character
and the [Hasse norm theorem](@hasse-norm-st). It is cuspidal because the
condition on infinitesimal characters prevents $\pi$ from being isomorphic
to its conjugate, and [Jacquet–Shalika rigidity](@jacquet-shalika-rigidity)
with [multiplicity one](@cuspidal-multiplicity-one) excludes the other
decompositions.
