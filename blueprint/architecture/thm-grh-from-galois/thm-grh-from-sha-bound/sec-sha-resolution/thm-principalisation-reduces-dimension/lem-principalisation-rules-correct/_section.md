+++
id    = "lem-principalisation-rules-correct"
kind  = "lemma"
title = "Correctness of the principalisation rules from their hypotheses"
lean  = ["FunctorialResolution.EmbeddedResolution.isCorrect_canonicalAlgorithmRules_of_hypotheses"]
order = 10
+++
Suppose that strict transforms of closed subschemes are blow-ups of the
transformed subschemes, that divisor reduction has its expected properties,
and that the geometric hypotheses of principalisation hold (existence of
hypersurfaces of maximal contact and the behaviour of orders under blow-up).
Then the rules of the canonical principalisation algorithm reduce
inductively on dimension, in the sense of
[thm-principalisation-reduces-dimension].
