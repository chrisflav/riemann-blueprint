+++
kind = "proof"
of   = "thm-kato-euler-system-ordinary"
uses = ["thm-kato-zeta-integral", "thm-kato-zeta-euler-system-exists",
        "thm-kato-explicit-reciprocity"]
+++
From the integral norm-compatible zeta classes ([thm-kato-zeta-integral])
and the explicit reciprocity law, [thm-kato-zeta-euler-system-exists]
gives a zeta Euler system with
its Iwasawa data. It remains to see that the bottom class is not in the
ordinary local condition at $l$. By the explicit reciprocity law
([thm-kato-explicit-reciprocity]) its image at $l$ is a nonzero
multiple of a value of a Hecke-equivariant functional on Eisenstein series;
a projection to the eigenspace of $g$ that does not vanish there exists, so
the class is not ordinary.
