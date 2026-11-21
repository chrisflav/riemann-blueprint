+++
id    = "thm-twisting-index-and-archimedean-bounds"
kind  = "theorem"
title = "Index bounds at the twisting places and a lower bound on archimedean weights"
lean  = ["GlobalTheory.BigOn.ontoX_of_hypotheses_alt_alt", "GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'"]
uses  = ["thm-labesse-base-change", "thm-bhatt-scholze-coefficients", "thm-casselman-wallach", "thm-chebotarev-degree-one", "thm-clozel-cohomological", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal", "def-local-parameters", "thm-discrete-series-parametrisation", "thm-green-parametrisation", "thm-hecke-l-adic-character", "thm-hecke-l-adic-character-above-l", "thm-grh-from-theta-integrals"]
order = 20
+++
Assume the published results on unitary groups listed in
[thm-grh-from-theta-integrals] and a system of local parameters
([def-local-parameters]). Then two estimates hold at the points of the
families of [def-family-data]: for every small $\varepsilon$, for every
large enough member of the class, and at every point of it at a large
enough scale $x$.

At such a point we have a CM field $K$ of degree $[K:\Q]$, hermitian data on
a space of dimension $D$ with $\mathcal O_K$-lattices $M_j$ and maps
$\theta_j$, and a finite set $T$ of *twisting places*: the finite places $w$
at which the local type differs from the base type. The set $T$ is stable
under complex conjugation $w \mapsto \bar w$. Write $p_w$ for the residue
characteristic, $e_w$ for the ramification index of $w$ over $p_w$, and
$I_j(w)$ for the relative index at $w$ of $M_j$ and the image under
$\theta_j$ of the standard lattice. The data carry constants $F_j(w)$,
$J_j(w)$, $E_1$ and $\ell_j$, and the last two depend linearly on a
parameter $C$.

1. *Index bounds.* If the family satisfies its divisibility condition, there
   is $C_0$ such that for $C \ge C_0$ and every $w \in T$, with error terms
   $\delta_j(w) \ge 0$,
   $$\sum_j\big(I_j(w) + I_j(\bar w)\big) \le D\Big(\sum_j\big(2e_wF_j(w) + e_w\delta_j(w)\big) + \frac{2e_w}{p_w^2}\Big),$$
   and for every $j$
   $$\sum_{w \in T}\frac{\log Nw}{[K:\Q]}\,e_w\big(\delta_j(w) + J_j(w)\big) \le E_1 = C\,E_1^u.$$
2. *Archimedean lower bound.* On the definite side the hermitian forms act on
   each isotypic piece, at each infinite place, by a positive scalar
   $\lambda_j$, and $\log\lambda_j \ge \ell_j = \ell_j^m - C\ell^u$.

The first estimate says that the images of the standard lattices fill the
$M_j$ up to an index controlled by the local data at the twisting places.
