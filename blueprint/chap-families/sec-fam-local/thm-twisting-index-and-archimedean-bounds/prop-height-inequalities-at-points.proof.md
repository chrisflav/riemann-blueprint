+++
kind = "proof"
of   = "prop-height-inequalities-at-points"
uses = ["thm-abelian-variety-torsion-count", "lem-local-point-data-heights",
        "thm-hasse-norm-quadratic", "thm-landherr-cm", "thm-unitary-integral-models",
        "thm-semistable-reduction", "thm-complex-theta-uniformisation"]
+++
The height inequality has four inputs: a base condition, a net of points,
global family data, and local point data with height bounds; a support
condition is needed as well. We show that there are a constant $C_L$ and
functions $C_q, Z_0$ such that these inputs hold with constants $C_L$ and
$C_q(C_A, C_K)$ at every point, every prime $p$ and every index $j$ in
range satisfying the parameter and size conditions, once $Z_0(C_A, C_K)$ is
at most the base size.

A lower bound for the logarithmic sup norm of integral forms gives $C_L$, a
recursive bound on lattices gives $C_q$, and polynomial domination gives
$Z_0$. Choose generators with controlled invariants. Local shares at all
places, and a combined bound on the scalars that uses Hodge–Tate inclusions
in formal coordinates, give the family data. The net comes from the point
itself. [lem-local-point-data-heights] gives the point data. The
[theta uniformisation of complex abelian varieties](@thm-complex-theta-uniformisation)
is among the inputs.

A numerical argument turns the threshold $Z_0$ into the threshold $x_0$ on
the scale. The conclusion for the extended data follows from the conclusion
for the base data.
