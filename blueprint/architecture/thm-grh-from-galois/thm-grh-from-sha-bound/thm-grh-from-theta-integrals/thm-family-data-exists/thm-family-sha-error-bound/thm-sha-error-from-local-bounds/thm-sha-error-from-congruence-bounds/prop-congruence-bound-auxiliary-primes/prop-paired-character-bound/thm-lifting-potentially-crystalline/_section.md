+++
id    = "thm-lifting-potentially-crystalline"
kind  = "theorem"
title = "Lifting finite classes along potentially crystalline lattices"
provenance = "new"
lean  = ["GlobalTheory.InertiaEigenvalues.theoremT_all_records", "GlobalTheory.T.crystallinePeriodBound_all_constant_ge_forty", "GlobalTheory.T.liftingStep_theoremT_of_bhattScholze_fontaine", "GlobalTheory.TheoremTClosing.main"]
order = 1
+++
Let $C \ge 40$, and let $F : T_1 \to T_2$ be a surjection of
$G_{\Q_l}$-stable lattices in potentially crystalline representations with
coefficients in a finite extension of $\Q_l$. Suppose:

* inertia acts on both through a Frobenius-stable set $\Sigma$ of characters
  with $1 \in \Sigma$ and $|\Sigma| \le N$, $N \ge 2$;
* the Hodge–Tate weights lie in a set $U \ni 0$ with $|U| \le N + 1$ and
  $U \subset [-\eta, H]$, $1 \le \eta < H$;
* $l > C(HN^2 + N^3)$.

Let $r'$ be the largest Frobenius orbit length of the characters
$\chi\chi'^{-1}$, $\chi, \chi' \in \Sigma$. Then $4r' \le N^2$, and for every
class $c \in H^1_f(G_{\Q_l}, T_2)$,
$$l^{\,C(Nr' + \eta(N + r'))}\,c \in F\big(H^1_f(G_{\Q_l}, T_1)\big).$$
