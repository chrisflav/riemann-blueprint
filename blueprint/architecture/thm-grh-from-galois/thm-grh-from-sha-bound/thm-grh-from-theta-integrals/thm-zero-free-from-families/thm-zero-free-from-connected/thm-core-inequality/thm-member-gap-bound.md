+++
kind  = "theorem"
title = "Each member bounds its von Mangoldt sums by their main terms"
provenance = "new"
lean  = ["Deduction.ch_top", "Formalism.LFunctionChainParameters.WeightedSlopeBounds.each_unit_bound_statement"]
uses  = ["def-slope-data", "def-family-member", "thm-chain-averaging"]
order = 2
+++
Suppose there are slope data at a large $x$ ([def-slope-data]), with
constants $e_D, e_L$. Then for every member $u$ of the family
([def-family-member]) the gap of [thm-chain-averaging] satisfies
$$\Delta(u) = \sum_{t \in T}\sum_{j < m}\big(S(a_t, t, w_{u,j}) - M(a_t, w_{u,j})\big)
\le x^{(e_D + e_L + 3)\varepsilon}\Big(|T|\,a\Big(1 + \frac{m^2}{k}\Big) + m\,(B_0 + N_c)\Big),$$
where $B_0 \le 2nmb\,x^{\varepsilon}$ and $N_c \le |T_2|\,k\,b\,x^{2\varepsilon}/n^2$
are error sizes of the slope data. So the hypothesis of
[thm-chain-averaging] holds with $C = e_D + e_L + 3$.

In words: a member carries $m|T|$ von Mangoldt sums over the primes inert
in $E$, one for each step of its chain of theta lifts and each twist, and
their total exceeds the total of the main terms by little. The main terms
grow linearly in $m$, while the error term $|T|a$ does not grow with $m$; this
is the gain of the chain. The terms in $m^2$ are its cost.
