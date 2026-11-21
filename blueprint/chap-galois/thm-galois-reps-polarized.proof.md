+++
kind = "proof"
of   = "thm-galois-reps-polarized"
uses = ["thm-galois-reps-from-geometry-and-theta", "thm-geometric-galois-odd-rank", "thm-theta-lift-nonvanishing",
        "thm-galois-reps-hecke-eigenspaces", "thm-kuga-sato-unitary-shimura", "thm-unitary-shimura-integral-models",
        "thm-base-change-unitary", "thm-local-global-ramified"]
+++
The theorem is [thm-galois-reps-from-geometry-and-theta] applied with its two
inputs, [thm-geometric-galois-odd-rank] and [thm-theta-lift-nonvanishing].

1. *Odd rank* ([thm-geometric-galois-odd-rank]). Let $a$ be odd. Move an
   automorphic representation of the definite unitary group in $a$ variables,
   with a cuspidal type at one place above $l$ and lacunary weights at
   another, to a Hecke eigensystem on a compact unitary Shimura variety of
   signature $(1, a-1)$. Its integral models
   ([thm-unitary-shimura-integral-models]) carry Kuga–Sato varieties that form
   a Hecke tower with good reduction, the Eichler–Shimura relation and the
   Hodge numbers predicted by the weight ([thm-kuga-sato-unitary-shimura]).
   The eigenspaces of such a tower carry Galois representations
   ([thm-galois-reps-hecke-eigenspaces]). The result has unknown dimension,
   and the Satake polynomial kills its Frobenius elements.
2. *Theta lifts* ([thm-theta-lift-nonvanishing]). Theta lifts from definite
   unitary groups do not vanish, with explicit weights.
3. *Assembly* ([thm-galois-reps-from-geometry-and-theta]). Cut a piece of
   dimension $a$ out of the representation of step 1; reach all weights by
   congruences and a limit of pseudo-representations; in even rank compare
   two theta lifts to odd rank; pass to $\GL_a$ by base change
   ([thm-base-change-unitary]). This gives compatibility at the unramified
   places, and [thm-local-global-ramified] adds the ramified places.
