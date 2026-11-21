+++
kind = "proof"
of   = "lem-inert-theta-admissibility-cm"
uses = ["thm-cm-j-integral-good-reduction"]
+++

CM elliptic curves have good models: for every square-free
$d \equiv 3 \bmod 4$, every lattice $\Lambda$ with complex multiplication by
$\Q(\sqrt{-d})$, every prime $l \ge 5$ with $l \nmid d$ and every
isomorphism $\iota : \C \cong \C_l$, there are $g_2, g_3$ in the ring of
integers of the maximal unramified extension of $\Q_l$ and $\lambda \ne 0$
with
$$g_2 = \lambda^4\iota(g_2(\Lambda)), \quad g_3 = \lambda^6\iota(g_3(\Lambda)), \quad |g_2^3 - 27g_3^2|_l = 1,$$
because [singular moduli are integral and CM curves have good reduction](@thm-cm-j-integral-good-reduction)
at these primes. With these models the first kernel law holds for small
lattice chains, and the admissibility follows from it. *It is not clear*
from the statements how the good models enter that law.
