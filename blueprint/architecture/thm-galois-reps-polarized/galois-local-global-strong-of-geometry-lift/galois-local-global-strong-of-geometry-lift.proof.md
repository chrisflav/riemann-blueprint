+++
kind = "proof"
of   = "galois-local-global-strong-of-geometry-lift"
uses = ["algebraic-character-wd", "chebotarev-degree-one", "chevalley-units", "core-all-of",
        "de-rham-potentially-semistable", "fontaine-bcris", "global-artin-reciprocity",
        "hecke-l-adic-character", "hecke-l-adic-character-de-rham", "rest"]
+++
1. *Seed.* From the representation $\rho$ of [geo-one-holds], of unknown
   dimension, cut out an $a$-dimensional piece: the lacunary Hodge–Tate weights
   and the determinant character, an $l$-adic character of an algebraic Hecke
   character, single out the right eigenvalues. This gives an $a$-dimensional
   representation whose Frobenius characteristic polynomials equal the Satake
   polynomials on a dense open set of Frobenius elements.
2. *Congruences.* Hecke eigensystems of definite unitary groups of odd rank are
   $l$-adic limits of eigensystems with a cuspidal type at $w_0$ and lacunary
   weights at $v'$, of the same weight elsewhere.
3. *All polarized pairs.* [core-all-of] turns these two statements and
   [thm-theta-lift-nonvanishing] into Galois representations compatible at the
   unramified places.
4. *Ramified places.* [rest] adds the compatibility at the other places.
