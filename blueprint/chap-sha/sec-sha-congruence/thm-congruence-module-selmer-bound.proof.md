+++
kind = "proof"
of   = "thm-congruence-module-selmer-bound"
uses = ["thm-artin-reciprocity", "thm-tate-euler-characteristic-global-places", "thm-tate-local-duality-global-places"]
+++
The triviality of unramified classes gives the unramified condition at the
places of $R \cup C$. The congruence module of $\pi$ is the cokernel of the
Hecke algebra in the product of its components; its length equals the index
of the lattice of eigenforms. Ribet's construction turns congruences between
$\pi$ and the other eigensystems into extensions between $\rho$ and the
characters $\chi^c$, and so into Selmer classes of the twists $\Z_l(e)$ and of
$\rho$. Their lengths are bounded by the local lengths at the places of
$R \cup C$, the Tate–Shafarevich groups and the class group, using the
decomposition of $r_\pi$, the local conditions and the bound $c_B$ on the tame
part. The argument uses [global Artin reciprocity](@thm-artin-reciprocity),
[local Tate duality](@thm-tate-local-duality-global-places) and the
[local Euler characteristic formula](@thm-tate-euler-characteristic-global-places).
*We read* the middle steps from the shape of the bound; the proof is not
split into named steps.
