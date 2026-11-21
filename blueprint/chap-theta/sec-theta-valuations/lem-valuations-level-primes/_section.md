+++
id    = "lem-valuations-level-primes"
kind  = "lemma"
title = "Valuations at the level primes"
provenance = "new"
lean  = ["GlobalTheory.Fc.Cv.row_level_valuations", "GlobalTheory.LvT.Built.TrueCols.closing_true_cols", "GlobalTheory.LvT.Built.TrueCols.row_true", "GlobalTheory.LvT.Built.TrueCols.trueColumns_chain_last_step_sharp_bound", "GlobalTheory.T.levelPrimeColumnValuations_bundlePoints_overColumns", "GlobalTheory.T.trueColumns_row_sharp_bounds"]
order = 1
+++

Let the data come from standard constructions. For every member $u$ with
level prime $\ell_u$ and every place $w$ of the field of definition over
$\ell_u$, with ramification index $e_w$ and exponent $E_{u,w}$:

1. every $c$ with $\mathrm{ord}_w(c) \ge e_w\,m\,E_{u,w}$ maps the vectors of
   the reference chain into the last lattice $S_m$;
2. for every tuple $\mu \ne \mu_0$ in use, with $\ell_u$ outside its
   exceptional set, the twisted vectors have $w$-valuation at least
   $-m\,E_{u,w}$.

Here $m$ is the length of the lattice chain.
