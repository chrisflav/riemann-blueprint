+++
kind = "proof"
of   = "lem-pair-count-siegel-mass-ratio"
uses = ["thm-hasse-norm-quadratic", "thm-siegel-main-theorem-hermitian"]
+++
Count the pairs of terms with given indices by the masses of the lattices
they determine, and bound these masses by $m_u$ times the amplitudes. Two
consequences of Siegel's mass formula ([thm-siegel-main-theorem-hermitian])
enter. First, for every CM field $K$ unramified over its real subfield and
every $n \ge 1$ there is a constant $c$ with
$\mathrm{mass}(M) = c\,\lambda(M)$ for every maximal lattice $M$ of a
positive definite hermitian space of dimension $n$. Second, for orthogonal
lattices $L$ of rank $M \ge 3$ and $L'$ of rank $M - 1$, the ratio
$\mathrm{mass}(L)/\mathrm{mass}(L')$ is an explicit function of $K$ and $M$;
we use it one rank at a time. The Hasse norm theorem
[thm-hasse-norm-quadratic] is also used; *it is not clear* where.
