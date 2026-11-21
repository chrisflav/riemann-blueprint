+++
kind = "proof"
of   = "core-all-of"
uses = ["algebraic-character-wd", "automorphic-forms-finite-gl", "base-change-definite-unitary-group",
        "bernstein-zelevinsky-finiteness", "borel-casselman", "car-u-alt", "cheb", "chebotarev-degree-one",
        "chevalley-units", "core-g", "cusp-forms-bounded-gl", "cuspidal-multiplicity-one",
        "cuspidal-spectrum-gl", "de-rham-potentially-semistable", "ess-square-integrable-segments",
        "fontaine-bcris", "frame-bound", "gelfand-kazhdan-dual", "generic-unitary-dual-gl",
        "geometric-lemma", "geometric-lemma-filtration", "global-artin-reciprocity", "hasse-norm-st",
        "hecke-l-adic-character", "hecke-l-adic-character-above", "hecke-l-adic-character-crystalline",
        "hecke-l-adic-character-de-rham", "irreducible-admissible-gl", "jacquet-rallis-unit-match-all-ranks",
        "jacquet-shalika", "jacquet-shalika-rigidity", "standard-functors-finite-length",
        "thm-base-change-unitary", "wave-existence-speed-multiplicity"]
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
   in this setting uses [core-g], [wave-existence-speed-multiplicity],
   [frame-bound] and the fundamental lemma
   ([jacquet-rallis-unit-match-all-ranks]). This gives the conjugate self-dual
   pairs, with $\chi$ a power of the quadratic character of $E/E^+$.
4. *All polarized pairs.* The general case follows from that one with
   Jacquet–Shalika rigidity, the Gelfand–Kazhdan theorem, Chebotarev's density
   theorem and the strong form of cyclic base change of Arthur and Clozel.
