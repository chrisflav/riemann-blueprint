+++
id    = "exp-st-of-num-sum-exp-model"
kind  = "lemma"
title = "Exponent bounds from lattice inclusions"
lean  = ["GlobalTheory.ExpTie.Asm.expSt_of_alt", "GlobalTheory.ExpTie.Asm.hasExpBound_at", "GlobalTheory.T.expSt_of_num_sumExp_model"]
order = 2
+++
Assume:

* a cutting inequality for $l$-adic exponents: for a partition $\lambda$ of
  length $N$, a prime $l$ and $a \le N$, the exponent attached to $\lambda$
  is at most the sum of the exponents of its first $a$ and last $N-a$ parts
  plus $a(N-a)\log_l w$, where $w$ bounds the spread of the parts;
* numerical conditions relating the parameters and weights at each index
  $j$ to the size data of the point;
* inclusions $l^{J}\Lambda \subseteq \Lambda'_w$ of the cut lattices in the
  localised reference lattices at every twisting place, with prescribed
  exponents $J$;
* local models ([model-statement-of-crystalline-chebotarev-frame-gal]) at
  the twisting places in the weight range.

Then the exponent bounds of [exp-st-of-base-change-and-crystalline-lattices]
hold with $E_J = 30\,t\,m\,b\,L^2 + 2mb$, where $L = x^\varepsilon$, $b = e^L$
and $t$ is the size of an auxiliary set of places.

*We read* the first condition as a subadditivity of exponents of
Weyl-module lattices. Its definition is not unfolded here.
