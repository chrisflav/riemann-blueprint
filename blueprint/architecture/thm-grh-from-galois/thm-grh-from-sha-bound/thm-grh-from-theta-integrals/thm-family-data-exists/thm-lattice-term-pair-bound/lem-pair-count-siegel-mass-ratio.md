+++
kind  = "lemma"
title = "Pair counts from Siegel mass ratios"
lean  = ["GlobalTheory.T.termPairCountBound_of_siegelMassRatios", "GlobalTheory.TypeAsm.pair_count_bound_of_siegel_mass"]
order = 1
+++
Suppose:

* for every CM field $K$ unramified over its real subfield and every $n \ge
  1$ there is a constant $c$ with $\mathrm{mass}(M) = c\,\lambda(M)$ for every
  maximal lattice $M$ of a positive definite hermitian space of dimension $n$;
* (Siegel's mass ratio) for orthogonal lattices $L$ of rank $M \ge 3$ and $L'$
  of rank $M - 1$, the ratio $\mathrm{mass}(L)/\mathrm{mass}(L')$ is an
  explicit function of $K$ and $M$.

Then for the constants and data of [thm-lattice-term-pair-bound] the weighted sum over
pairs of terms,
$$\sum_{(t, t') \in S} w_t w_{t'}\,\omega_t\,\omega_{t'},$$
is at most $m_u\,A_e(j', \delta')A_e(j'', \delta'')$.
