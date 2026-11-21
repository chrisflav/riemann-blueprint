+++
id    = "thm-wach-lifting-theorem"
kind  = "theorem"
title = "Local lifting theorem for Wach lattices"
lean  = ["Formalism.MainNotions.N.Ln03.corollary_local_exists_constant", "Formalism.MainNotions.N.Ln03.local_corollary_of_de_rham", "GlobalTheory.T.theoremE_corollaryA_closing_all_data", "GlobalTheory.ThmECorA.closing"]
uses  = ["thm-bloch-kato-local", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-duality-l-adic"]
order = 1
+++
Assume the local theory of Bloch and Kato, local Tate duality and the local
Euler characteristic formula. There is $C_0$ such that for every member the
following hold at every prime $l$.

* (*Lifting theorem*) Let $l \ge 5$, $K/\Q_l$ finite with maximal
  unramified subfield $K_0$, and $F : T_1 \to T_2$ a surjection of
  crystalline lattices whose Hodge–Tate weights lie in prescribed windows of
  length $h$, clustered according to a cyclic labelling of the embeddings
  of $K_0$. Then $l^e H^1_f(T_2) \subset F(H^1_f(T_1))$ with
  $$e \le 800\Big(\frac{h}{(l-1)^{j+1}} + g\,\ell_{\max} + \log_l h\Big),$$
  where $j$, $g$ and $\ell_{\max}$ measure the clusters of weights.
* (*Corollary*) For $l \ge 11$ and every $C \ge C_0$, the cokernel of
  $H^1_f(T_1) \to H^1_f(T_2)$ has length at most
  $C(n+1)\,\mathrm{rk}\,T_2\big(h/(l-1)^{j+1} + (g+1)(j+1) + \log_l h\big)$
  plus a term of the same kind, in units of the length of $O/l$.

*We read* the length in the corollary as the length of this cokernel.
