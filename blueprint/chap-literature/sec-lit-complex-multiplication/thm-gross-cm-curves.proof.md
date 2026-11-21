+++
kind = "proof"
of   = "thm-gross-cm-curves"
uses = ["thm-singular-moduli-class-number"]
+++
The proof is explicit. Since $\mathcal O_K$ has a non-real multiplier,
$j(\mathcal O_K)$ is an algebraic integer, and $F$ is a number field whose
relation to the Hilbert class field is [thm-singular-moduli-class-number]. Rescale the
lattice $\mathcal O_K \subset \C$ so that its invariants $g_2, g_3$ lie in
$F$, take the curve $y^2 = x^3 - \tfrac{g_2}{4}x - \tfrac{g_3}{4}$ twisted by
$1$ if $p \equiv 3 \bmod 8$ and by $-p$ otherwise, and check its
discriminant and its reduction prime by prime.
