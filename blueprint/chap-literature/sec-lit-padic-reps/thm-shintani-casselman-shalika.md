+++
kind  = "theorem"
title = "The formula of Shintani and Casselman–Shalika"
provenance = "published"
source = "Shintani [shintani-1976]; Casselman–Shalika [casselman-shalika-1980]"
lean  = ["GroundTheory.Automorphic.Spherical.casselman_shalika",
         "GroundTheory.Automorphic.Spherical.eq_smul_sphericalWhittaker",
         "GroundTheory.Automorphic.Spherical.sphericalWhittaker"]
order = 13
+++
Let $F$ be a non-archimedean local field with ring of integers $\mathcal O$
and uniformiser $\varpi$, and let $\psi$ be an additive character of $F$ that
is trivial on $\mathcal O$ but not on $\varpi^{-1}\mathcal O$. Let $N$ be the
upper triangular unipotent subgroup of $\GL_n(F)$ with its generic character
$\psi_N$, $\delta$ the modulus character of the upper triangular Borel
subgroup, and $z \in (\C^\times)^n$.

Let $W$ be a function on $\GL_n(F)$ with $W(ug) = \psi_N(u)W(g)$ for $u \in N$,
right invariant under $\GL_n(\mathcal O)$, and an eigenfunction of the
spherical Hecke algebra whose eigenvalues are the Satake transforms evaluated
at $z$. Then for $l \in \Z^n$,
$$
W(\mathrm{diag}(\varpi^{l_1}, \dots, \varpi^{l_n})) =
\begin{cases}
W(1)\, \delta^{1/2}(\mathrm{diag}(\varpi^{l_1}, \dots, \varpi^{l_n}))\, s_l(z) & \text{if } l_1 \ge \dots \ge l_n,\\
0 & \text{otherwise,}
\end{cases}
$$
where $s_l$ is the Schur polynomial of the dominant weight $l$. By the Iwasawa
decomposition, $W$ is therefore $W(1)$ times one explicit spherical Whittaker
function; in particular such a $W$ is unique up to a scalar.
