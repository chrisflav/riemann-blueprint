+++
kind  = "proposition"
title = "Existence of the intermediate constructions"
lean  = ["GlobalTheory.HeightCounting.Up.all_stages_of_specializations_alt", "GlobalTheory.T.all_stages_at_member_of_specializations_alt"]
uses  = ["automorphic-forms-finite-gl", "base-change-definite-unitary-group", "bernstein-unitary-product-irreducible", "bernstein-zelevinsky-finiteness", "car-u-alt", "casselman-wallach", "cheb", "chebotarev-degree-one", "cusp-rapid-decay", "cusp-u-alt", "de-rham-potentially-semistable", "def-local-parameters", "depth-zero-jacquet-injective", "discrete-series-cover", "discrete-series-exists", "doubling-method-local-zeta-integrals", "ess-square-integrable-segments", "generic-unitary-dual-gl", "geometric-lemma", "global-artin-reciprocity", "green-cuspidal", "harish-chandra-finite", "harish-chandra-modules", "hecke-l-adic-character-above", "hecke-l-adic-parameter-above-alt", "hecke-l-partial-continuation", "jacquet-shalika", "published-siegel-weil-unitary-convergent", "ray-character-artin", "ray-class-field-st", "regular-algebraic-purity", "schur-orthogonality-square-integrable", "unlinked-product-irreducible", "unramified-doubling-gl", "weil-representation-unitary-pair", "weil-unitary"]
order = 1
+++
Assume the Casselman–Wallach theorem, the theory of Harish-Chandra modules,
the Weil representation of unitary dual pairs, existence and uniqueness of
discrete series of $\U(p, q)$ with given parameter, the covering and
multiplicity hypotheses, and the published inputs on Galois representations
and theta series. Let $\rec$ be a system of local parameters
([def-local-parameters]) that satisfies an archimedean comparison and a
statement on points. Then from every saturated starting configuration one
reaches, one step at a time:

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
