+++
kind = "proof"
of   = "thm-galois-reps-unramified-compatible"
uses = ["thm-hecke-character-wd-above-l", "thm-hc-finiteness-gl", "thm-labesse-base-change",
        "thm-bz-finiteness", "thm-borel-casselman", "thm-chebotarev-degree-one",
        "thm-chevalley-congruence-units", "thm-twisted-trace-lowest-type", "thm-cusp-bounded-gl", "thm-multiplicity-one-gl",
        "thm-cuspidal-spectrum-gl", "thm-p-adic-monodromy", "thm-zelevinsky-segments",
        "thm-fontaine-bcris", "thm-hecke-bound-base-change", "thm-gelfand-kazhdan", "thm-tadic-generic-unitary-dual",
        "thm-geometric-lemma", "thm-geometric-lemma-filtration", "thm-artin-reciprocity", "thm-hasse-norm-quadratic",
        "thm-hecke-l-adic-character", "thm-hecke-l-adic-character-above-l", "thm-hecke-l-adic-character-crystalline",
        "thm-hecke-l-adic-character-de-rham", "thm-jacquet-irreducible-admissible", "thm-jacquet-rallis-fundamental-lemma",
        "thm-jacquet-shalika", "thm-jacquet-shalika-strong-mult-one", "thm-bz-functors-finite-length",
        "thm-base-change-unitary", "thm-wave-kernels-gln-c"]
+++
1. *Limits in odd rank.* Combine the seed and the congruences: the Galois
   representations of the approximating eigensystems have a limit, which is
   attached to every eigensystem of odd rank; *we read* this as Chenevier's
   argument with pseudo-representations. A congruence argument for the
   crystalline Frobenius gives the properties at $l$.
2. *Even rank.* For a representation of a definite unitary group in an even
   number $n$ of variables, theta lifts ([thm-theta-lift-nonvanishing]) give two
   lifts to rank $n + t$, $n + t$ odd, whose Galois representations are
   $\rho \otimes \kappa \oplus \bigoplus_i \psi_{1,i}$ and $\rho \otimes \kappa \oplus \bigoplus_i \psi_{2,i}$
   with no character in common. Subtracting isolates $\rho$.
3. *From unitary groups to $\GL_a$.* A conjugate self-dual $\pi$ descends to a
   definite unitary group away from a finite set of non-split places, and
   base change ([thm-base-change-unitary]) relates the two; the proof of base change
   in this setting uses [thm-twisted-trace-lowest-type], [thm-wave-kernels-gln-c],
   [thm-hecke-bound-base-change] and the fundamental lemma
   ([thm-jacquet-rallis-fundamental-lemma]). This gives the conjugate self-dual
   pairs, with $\chi$ a power of the quadratic character of $E/E^+$.
4. *All polarized pairs.* The general case follows from that one with
   Jacquet–Shalika rigidity, the Gelfand–Kazhdan theorem, Chebotarev's density
   theorem and the strong form of cyclic base change of Arthur and Clozel.
