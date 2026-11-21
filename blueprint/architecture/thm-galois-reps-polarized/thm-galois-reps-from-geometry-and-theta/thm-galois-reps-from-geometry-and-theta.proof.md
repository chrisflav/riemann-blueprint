+++
kind = "proof"
of   = "thm-galois-reps-from-geometry-and-theta"
uses = ["thm-hecke-character-wd-above-l", "thm-chebotarev-degree-one", "thm-chevalley-congruence-units", "thm-galois-reps-unramified-compatible",
        "thm-p-adic-monodromy", "thm-fontaine-bcris", "thm-artin-reciprocity",
        "thm-hecke-l-adic-character", "thm-hecke-l-adic-character-de-rham", "thm-local-global-ramified"]
+++
1. *Seed.* From the representation $\rho$ of [thm-geometric-galois-odd-rank], of unknown
   dimension, cut out an $a$-dimensional piece: the lacunary Hodge–Tate weights
   and the determinant character, an $l$-adic character of an algebraic Hecke
   character, single out the right eigenvalues. This gives an $a$-dimensional
   representation whose Frobenius characteristic polynomials equal the Satake
   polynomials on a dense open set of Frobenius elements.
2. *Congruences.* Hecke eigensystems of definite unitary groups of odd rank are
   $l$-adic limits of eigensystems with a cuspidal type at $w_0$ and lacunary
   weights at $v'$, of the same weight elsewhere.
3. *All polarized pairs.* [thm-galois-reps-unramified-compatible] turns these two statements and
   [thm-theta-lift-nonvanishing] into Galois representations compatible at the
   unramified places.
4. *Ramified places.* [thm-local-global-ramified] adds the compatibility at the other places.
