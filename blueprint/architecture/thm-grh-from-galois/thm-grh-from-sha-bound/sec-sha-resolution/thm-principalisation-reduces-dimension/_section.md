+++
id    = "thm-principalisation-reduces-dimension"
kind  = "theorem"
title = "The principalisation algorithm reduces on dimension"
lean  = ["FunctorialResolution.EmbeddedResolution.canonicalAlgorithmRules_isCorrect", "FunctorialResolution.EmbeddedResolution.isCorrect_canonicalAlgorithmRules"]
order = 10
+++
Consider the canonical principalisation algorithm for marked ideals with
boundary on smooth varieties in characteristic zero, in the form of
Villamayor and Włodarczyk: one alternates a reduction of the maximal order
with a reduction of the boundary divisors, both taken inside a hypersurface
of maximal contact of smaller dimension. Use, for the blow-ups, the fact that
the strict transform of a closed subscheme is the blow-up of that subscheme
along the restricted centre.

Then the rules of the algorithm *reduce inductively on dimension*: if the
rules in dimensions $< n$ reduce the maximal order, then in dimension $n$
the boundary step reduces the boundary divisors, does not depend on their
positions, and the order step and the maximal-order step reduce the order
and the maximal order.
