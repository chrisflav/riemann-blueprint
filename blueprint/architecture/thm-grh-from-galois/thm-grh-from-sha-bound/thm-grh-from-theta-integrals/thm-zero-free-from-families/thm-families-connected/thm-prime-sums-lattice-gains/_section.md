+++
id    = "thm-prime-sums-lattice-gains"
kind  = "theorem"
title = "Prime sums are bounded by lattice gains"
provenance = "new"
lean  = ["Formalism.L2.G.linkG_concrete5"]
order = 11
+++
Let $\mathcal C$ be a class of families ([def-family-data]). Suppose that,
for all small $\varepsilon$ and all large enough families of $\mathcal C$,
every member eventually satisfies *group compatibility* (its lattices are
compatible with the unitary group and its level structure) and the second
admissibility condition ([thm-twisted-admissibility]). Then,
in the same sense, every family of $\mathcal C$ satisfies the *local link*:
there are $C$, $x_0$ and $\delta(x) \to 0$ such that for $x \ge x_0$ and
every member, with the scale $b = e^{x^\varepsilon}$ of [def-slope-data]:

* at each place $w$ and lattice $u$ away from the type of $u$, the local
  length of $u$ at $w$ is at most $d(u)(\tau_w + \iota_w)$, where $\tau_w$
  and $\iota_w$ are the local budgets, and all three vanish where no orbit is
  served;
* at each prime $p$ inert in the auxiliary field and not too large, the
  gains $g_j(w)$ of the theta lifts satisfy $0 \le g_j(w) \le 4|T|a/p$, and
  $$\sum_j\sum_t\big(\Lambda_{j,t}(p) - \ell(p)\big) - m\,\phi(p) \le \sum_j g_j(w) - \tau_w,$$
  where $\Lambda_{j,t}(p)$ are the von Mangoldt class sums of the identity in
  [def-slope-data], and $\ell(p)$, $\phi(p)$ are explicit lower terms
  involving $C$ and $b^{\delta(x)}$;
* the sums over served orbits are at most $2m N_v(p)a/p$, the served orbits
  are contained in the expected set, and the mean of the local defects is
  bounded.

This is the local inequality from which the slope inequality of
[def-slope-data] is assembled.
