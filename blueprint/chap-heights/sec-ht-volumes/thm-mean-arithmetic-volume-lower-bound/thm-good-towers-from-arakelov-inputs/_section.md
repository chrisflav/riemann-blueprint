+++
id    = "thm-good-towers-from-arakelov-inputs"
kind  = "theorem"
title = "Existence of good towers and the volume theorem"
provenance = "new"
lean  = ["GlobalTheory.CompanionTheory.Ar.Link.good_tower_volume_theorem_bis", "GlobalTheory.CompanionTheory.Ar.Top.goodTower_volume_of_reduced", "GlobalTheory.T.final_theorem_of_inputs_right",
         "GlobalTheory.CompanionTheory.Ar.Top.goodTower_and_volume", "GlobalTheory.T.good_tower_volume_theorem",
         "GlobalTheory.CompanionTheory.Ar.Cusp.volumeTheoremX_of_inputs", "GlobalTheory.T.volume_theorem_of_inputs",
         "GlobalTheory.CompanionTheory.Ar.Sl.slopeBound_and_lemmaS_of_siegel", "GlobalTheory.CompanionTheory.Ar.Top.given_of_inputs",
         "GlobalTheory.T.final_theorem_of_inputs_left", "GlobalTheory.T.slope_bound_of_line_large_degree"]
order = 2
+++
Let $E$ be a CM field with a unitary Shimura datum of signature $(p, q)$,
$p, q \ge 1$, with CM type $\Phi$, and let $Y$ be a global integral model of the
unitary Shimura variety over the ring of integers of its coefficient field
(one that descends and dominates the local models of
[thm-unitary-integral-models]) with split components. Then:

1. *Good towers exist*: there is a tower $T$ of flag bundles of the Hodge
   bundles over $Y$, with line bundles indexed by $\Phi \times \{1, \dots,
   p+q\}$ (the Chern roots), and a smooth and flat realisation of it with an
   ample reference model.
2. *Volume theorem*: there is $C \ge 0$ such that, if $E$ is abelian over $\Q$,
   $p \ge 2q + 1$ and $T$ has at most $4|\Phi|(p+q)^2$ bad primes, then all
   components of $Y$ have the same volume, the arithmetic intersection
   numbers of the root line bundles are proportional to their geometric
   intersection numbers up to an error term, and for every regular weight
   $u$ the mean over components of the slopes of arithmetic volumes is at
   least $-C$ times an error built from $\log \mathrm{rd}_E$, the value of
   $L'/L$ at $1$, the number of bad primes and $u$.
