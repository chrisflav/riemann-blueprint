+++
id    = "lem-local-models-constructed-points"
kind  = "lemma"
title = "Local models at constructed points"
provenance = "new"
lean  = ["GlobalTheory.Svd.modelsAt_bpt", "GlobalTheory.Svd.modelsAt_of_part",
         "GlobalTheory.T.tuplesHaveLocalModels_at_constructedPoint_over_trueColumns",
         "GlobalTheory.T.tuplesHaveLocalModels_of_standardColumnObjects",
         "GlobalTheory.T.jointSite_chain_compared_carries_admittedSystem",
         "GlobalTheory.T.thetaLocalModels_of_splitUnramified_joints",
         "GlobalTheory.TwV.modelsOK_of_joints", "GlobalTheory.TwV.site_cmpLite_siteAdm"]
order = 2
+++

Let a point of a family come from a standard construction. Then the twisted
hermitian forms of the point have local models: for every tuple $\mu$ in
use, every member $u$ and every place $w$ over the level prime of $u$
outside the exceptional set of $\mu$, there is a chain of lattices at $w$
that is compatible with the comparison maps and admissible at $w$, provided
the rank satisfies $2r_G \le k$.
