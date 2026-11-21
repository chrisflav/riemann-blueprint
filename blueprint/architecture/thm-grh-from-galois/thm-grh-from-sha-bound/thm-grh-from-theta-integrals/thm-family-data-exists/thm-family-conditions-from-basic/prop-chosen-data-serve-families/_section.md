+++
id    = "prop-chosen-data-serve-families"
kind  = "proposition"
title = "The chosen data serve their families"
provenance = "new"
lean  = ["GlobalTheory.Svd.servH_row_linkR_alt", "GlobalTheory.Svd.servH_row_of_artin", "GlobalTheory.T.bundle_bothParts_of_standardKernel_of_globalArtinReciprocity", "GlobalTheory.T.hServ_of_linkR", "GlobalTheory.T.reciprocity_kernel_of_artin", "GlobalTheory.row_hServ_of_link_alt"]
uses = ["def-local-parameters"]
order = 2
+++
Let $p$ be construction data for the families, built on a system of local
parameters ([def-local-parameters]). Choose an admissible datum at each
point of each family, compatibly with the reciprocity data that $p$
attaches to it. Then the choice *serves the family*:

1. eventually in $x$, the twisted hermitian forms of every member have
   compatible local lattice models at the places over its level prime
   ([lem-local-models-constructed-points]);
2. at every chosen datum, the kernel attached to an elliptic curve with
   complex multiplication by $K = \Q(\sqrt{-d})$ satisfies the kernel
   conditions of [lem-kernel-conditions-standard-data].
