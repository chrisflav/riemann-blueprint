+++
kind  = "proposition"
title = "Existence of the intermediate constructions"
provenance = "new"
lean  = ["GlobalTheory.HeightCounting.Up.all_stages_of_specializations_alt", "GlobalTheory.T.all_stages_at_member_of_specializations_alt"]
uses = ["def-local-parameters"]
order = 5
+++
Let $\rec$ be a system of local parameters ([def-local-parameters]) that
satisfies an archimedean comparison and a statement on points. Then from
every saturated starting configuration one reaches, one step at a time:

* a configuration with the same Galois level, at which the theta series are
  rational and the cuspidal parameters are defined;
* three intermediate levels, then a strictly henselian acyclic level;
* finiteness: every configuration at the last level gives a depth-three
  partial construction for the construction data with a Bloch–Kato law.

Moreover, for every real $c$ the lists of settings and forms, of series and
of moduli points exist.

*It is not clear* what the intermediate levels are. The words "strictly
henselian" and "acyclic" suggest levels in a tower of integral models, but
the statement does not say.
