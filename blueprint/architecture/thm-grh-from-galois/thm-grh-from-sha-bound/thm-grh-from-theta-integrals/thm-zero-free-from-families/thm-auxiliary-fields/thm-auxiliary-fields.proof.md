+++
kind = "proof"
of   = "thm-auxiliary-fields"
uses = ["lem-good-auxiliary-primes", "thm-pnt-progressions-exceptional-zero"]
+++
Choose the ranks of the families so that the Galois group has order
between $x^{2+8\varepsilon}$ and $2x^{2+8\varepsilon}$, and take for $E$ the
$\psi$-field of that size. The Tate–Shafarevich condition is the hypothesis.
The primes $q$ and $d$ are not arbitrary: by [lem-good-auxiliary-primes]
most of them are good, so that the new characters, those involving
$(\cdot/q)$ or $(\cdot/d)$, satisfy $|L'/L(1,\chi)| \le C\log Y$ and the
square-root bound $|g_\chi(y)| \le y^{1/2+\tau}$ on the window. This is how
the bound on $L'/L(1,\chi)$ is obtained for real characters: by averaging
over $q$ and $d$, not for each character. The supply of primes comes from
the prime number theorem in progressions
([thm-pnt-progressions-exceptional-zero]), whose proof uses the
Deuring–Heilbronn phenomenon and Turán's power sums. *It is not clear*
from the statements how the equidistribution of the primes in
$\Gal(E/\Q)$ is proved.
