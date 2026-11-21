+++
id    = "thm-membership-with-origin"
kind  = "theorem"
title = "Membership for the construction data with origin"
lean  = ["GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_prime_alt", "GlobalTheory.T.member_exists_baseLattice_alt"]
uses = ["def-local-parameters"]
order = 2
+++
Suppose that every starting configuration has a saturated refinement with
no local conditions. Let $\rec$ be a system of local parameters
([def-local-parameters]) satisfying the archimedean comparison and the
statement on points of [prop-intermediate-constructions-exist], and let $c$
be real. Let $p$ be the construction data obtained from $\rec$ by
restricting to origin data for $c$.

Suppose the *multiplicity condition* holds for $p$: at every point of the
families, for inner forms $G_0, G_i$ of the definite unitary groups involved
that are isomorphic at the finite adèles by $\Phi$, every irreducible
admissible representation $\sigma$ occurs in the cuspidal spectrum of $G_0$
with the same multiplicity as $\sigma \circ \Phi^{-1}$ in that of $G_i$.

Then the families built from $p$ satisfy the membership conditions of
[thm-family-membership-admissible-data], and at every good constructed
point there is an admissible datum compatible with $p$.

[thm-inner-form-multiplicities-equal] proves the multiplicity condition, and
the proof of [thm-family-membership-admissible-data] uses it to remove
this hypothesis.
