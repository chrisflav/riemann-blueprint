+++
id    = "thm-congruence-module-selmer-bound"
kind  = "theorem"
title = "Congruence modules are bounded by Selmer data"
provenance = "new"
lean  = ["GlobalTheory.SelmerBoundAtPoint.main",
         "GlobalTheory.T.globalLatticeIndexTheorem_of_lengthBoundAtPlaces"]
order = 12
+++
Let $D$ be a
member of a family over the auxiliary CM field $E$, $l$ a prime of its
coefficients other than the two auxiliary primes, and $r_x$ a family of
Galois representations of $G_E$ of dimension $n_V$ over the coefficient
ring $\mathcal O$, indexed by the Hecke eigensystems $x$, which for $x = \pi$
decomposes as $\rho \oplus \bigoplus_{c=1}^{t}\chi^c$. Suppose the family is
continuous, its local coefficients are compatible, it satisfies Fontaine's
conditions and the Bloch–Kato conditions at the places above $l$, the
unramified classes are trivial, and the tame generator conditions hold. Suppose
the local length of $\pi$ at each place in a set $R$ above $l$ is at most
$\mathrm{len}_w$, and the lifting exponent at each place in a set $C$ is at
most $e'_w$. If $\pi$ lies in the chosen set of eigensystems and
$Ш^1_l(E, e)$ is finite for $0 < e < t$, then the length of the congruence
module of $\pi$ is at most
$$\sum_{w \in R \cup C}\lambda_w + s_\pi + \sum_{0<e<t}\mathrm{len}\,Ш^1_l(E, e) + v_l(h_E) + t\sum_{w \in R}(\deg w + 2)c_B + 4n_V(|C| + 1)\delta + t|C|h_0 + t\sum_{v \in Q}\mathrm{len}\big(\mathcal O/(\zeta_v - 1)\big),$$
where $\lambda_w$ is the local term built from $\mathrm{len}_w$ and $e'_w$,
$s_\pi$ a Selmer term, $h_E$ the class number of $E$, and the remaining
terms are explicit in the data of the member.

This is a bound of the type of the numerical criterion of Wiles and
Lenstra: the congruences of $\pi$ with the other eigensystems are bounded by
Selmer and Tate–Shafarevich groups. *We read* it as the source of the
Tate–Shafarevich error term of the families ([def-sha-error-term]).
