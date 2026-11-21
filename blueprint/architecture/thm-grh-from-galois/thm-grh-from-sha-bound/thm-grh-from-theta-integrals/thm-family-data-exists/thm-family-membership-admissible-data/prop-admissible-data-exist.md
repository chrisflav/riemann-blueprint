+++
kind  = "proposition"
title = "Admissible data exist"
lean  = ["GlobalTheory.Mem.Top.Bl.exBL_isLinked_prmR_alt", "GlobalTheory.T.geometric_parameter_uniform_alt"]
uses  = ["thm-casselman-wallach", "thm-cusp-rapid-decay", "def-local-parameters", "thm-discrete-series-parametrisation", "thm-discrete-series-exist", "thm-artin-reciprocity", "thm-green-parametrisation", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary", "thm-weber-ray-class-field", "thm-weil-representation-auxiliary-pairs"]
order = 1
+++
Assume Green's classification, the covering theorem for discrete series,
the theory of Harish-Chandra modules, the Casselman–Wallach theorem, the
Weil representation of unitary pairs, existence of discrete series,
Harish-Chandra's finiteness theorem, rapid decay of cusp forms, Artin
reciprocity and Weber's theorem on ray class fields. Let $\rec$ be a system
of local parameters ([def-local-parameters]) and $N$ a choice of norms that
refines the choice with a Bloch–Kato law. Let $p$ be the construction data
of $N$. Suppose that partial constructions for $p$ move with changes of the
division data, and that the multiplicity condition of
[thm-membership-with-origin] holds for $p$. Then at every good
constructed point of the families built from $p$ there is an admissible
datum compatible with $p$.
