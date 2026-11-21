+++
id    = "lem-membership-two-passes"
kind  = "lemma"
title = "Membership from two passes"
lean  = ["GlobalTheory.Mem.Top.Bl.memberE_of_steps2", "GlobalTheory.T.exists_member_of_construction_steps_secondPass"]
uses  = ["thm-gross-cm-curves"]
order = 2
+++
Assume Weber's theorem on ray class fields, the principal ideal theorem,
the existence of CM elliptic curves with good reduction outside a prime,
and the Siegel mass ratio of [thm-family-membership-admissible-data].
Let $p, p'$ be construction data. Suppose that for both, depth-three partial
constructions extend to depth four and ambient, division and theta data
exist, and that depth-three partial constructions for $p$ exist from every
start. Suppose that constructed points for $p$ have the twisting property,
that from them one can pass to an enlarged base with depth-three partial
constructions for $p'$, and that every point built for $p'$ is good for $p$,
with good twists at every place. Then the families built from $p$ satisfy
the membership conditions.
