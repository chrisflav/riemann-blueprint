+++
kind = "proof"
of   = "prop-lattice-and-depth-estimates"
uses = ["thm-abelian-variety-torsion-count", "thm-hasse-norm-quadratic", "thm-landherr-cm",
        "prop-height-inequalities-at-points", "prop-local-data-unitary-shimura-points"]
+++
The height inequalities of [prop-height-inequalities-at-points] hold along
the family. They give the fullness and stability of the lattices, and with
the size conditions they give the index bound at pairs of places.

For the depth bounds, pass to the points of the integral model of a
unitary Shimura variety. Three local statements about the formal group of
an abelian variety with an action of $\mathcal O_E$ hold at every prime
$p$: a colength bound at split places, a Hodge–Tate inclusion, and an
*estimate at unramified primes*. The last says: let $T$ be a complete local
noetherian domain of characteristic zero in which $p$ is not a unit, $A$ a
polarised abelian scheme over $T$ with an action of the ring of integers
$\mathcal O$ of a CM field, and $F$ a formal group law of dimension $d$
giving coordinates on the formal group of $A$, compatible with the action;
if $p \ne 2$ does not divide the discriminant of $\mathcal O$, then at a
place of $\mathcal O$ above $p$, eigenbases for the action of $\mathcal O$,
taken over the valuation ring of an algebraically closed field, have
valuations bounded as prescribed.

There is a constant $C_0$ such that the four depth bounds hold at every
point satisfying the recursive conditions, provided that the scale
satisfies $x \ge 3$ and $x^{\varepsilon/5} \ge 3$, that $k b' \le b$, that
$C \ge C_0$ and a weight constant is at least $10$, and that the local
numbers of the point are those of its data; at a large scale all of this
holds. The estimate at unramified primes gives depth data at every point of
the moduli space ([prop-local-data-unitary-shimura-points]). Applied at the
points of the moduli space attached to the indices $j$ of the family, these
data give the bound at good primes. The bounds at $q$, $d$ and the level
have separate proofs, and the bound at $2$ uses the first two local
statements.
