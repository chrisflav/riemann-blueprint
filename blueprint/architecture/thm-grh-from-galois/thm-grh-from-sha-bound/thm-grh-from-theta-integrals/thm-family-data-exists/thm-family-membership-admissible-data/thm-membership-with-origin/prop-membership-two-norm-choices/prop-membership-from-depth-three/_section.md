+++
id    = "prop-membership-from-depth-three"
kind  = "proposition"
title = "Membership from depth-three constructions"
lean  = ["GlobalTheory.Mem.Top.Closing.memberE_closing_alt_alt"]
uses  = ["thm-casselman-wallach", "thm-gross-cm-curves", "thm-cusp-rapid-decay", "def-local-parameters", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary", "thm-siegel-main-theorem-hermitian", "thm-weil-representation-auxiliary-pairs"]
order = 2
+++
Assume Weber's theorem on ray class fields, the principal ideal theorem,
the existence of CM elliptic curves with good reduction outside a prime, the
infinitesimal characters, existence and uniqueness of discrete series of
$\U(p, q)$, Harish-Chandra's finiteness theorem, rapid decay of cusp forms,
the Siegel–Weil formula, the formal degree formula, the Siegel mass ratio
of [thm-family-membership-admissible-data], the Weil representation of
unitary pairs, the Casselman–Wallach theorem and the theory of
Harish-Chandra modules.

Let $N_g \subseteq N$ be choices of norms for a system of local parameters
([def-local-parameters]) as in [prop-membership-two-norm-choices], with
construction data $p$ and $p_g$. Suppose that depth-three partial
constructions for $p$ exist from every start, that the level-three upgrade
holds for $p$ and $p_g$, that constructed points for $p$ have the twisting
property, and that from them one can pass to an enlarged base with
depth-three partial constructions for $p_g$. Then the families built from $p$
satisfy the membership conditions.
