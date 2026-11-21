+++
id    = "prop-membership-two-norm-choices"
kind  = "proposition"
title = "Membership from two choices of norms"
lean  = ["GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_pair_alt"]
uses = ["def-local-parameters"]
order = 2
+++
Let $\rec$ be a system of local parameters ([def-local-parameters]) as in
[thm-membership-with-origin], and let $N_g \subseteq N$ be two choices of
norms for it: every choice allowed by $N$ refines the choice with a
Bloch–Kato law, and every choice allowed by $N_g$ is allowed by $N$ and is
good. Let $p$ and $p_g$ be the construction data for $N$ and $N_g$. Suppose
that:

* every starting datum extends to a depth-three partial construction for
  $p$, and the level-three upgrade holds for $p$ and for $p_g$;
* partial constructions for $p$ move with changes of the division data;
* at constructed points for $p$ one can pass to an enlarged base at which
  depth-three partial constructions for $p_g$ exist;
* the multiplicity condition of [thm-membership-with-origin] holds
  for $p$.

Then the families built from $p$ satisfy the membership conditions, and at
every good constructed point there is an admissible datum compatible
with $p$.
