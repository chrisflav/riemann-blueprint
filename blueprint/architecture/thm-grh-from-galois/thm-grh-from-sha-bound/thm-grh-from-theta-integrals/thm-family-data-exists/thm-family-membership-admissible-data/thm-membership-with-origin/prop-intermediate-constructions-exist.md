+++
kind  = "proposition"
title = "Existence of the intermediate constructions"
lean  = ["GlobalTheory.HeightCounting.Up.all_stages_of_specializations_alt", "GlobalTheory.T.all_stages_at_member_of_specializations_alt"]
uses  = ["thm-hc-finiteness-gl", "thm-labesse-base-change", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-galois-reps-csd-above-l", "thm-casselman-wallach", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-cusp-rapid-decay", "thm-galois-reps-polarized-cuspidal", "thm-p-adic-monodromy", "def-local-parameters", "thm-depth-zero-jacquet-injective", "thm-discrete-series-parametrisation", "thm-discrete-series-exist", "thm-doubling-method", "thm-zelevinsky-segments", "thm-tadic-generic-unitary-dual", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-green-parametrisation", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-character-local-parameter-above-l", "thm-hecke-l-nonvanishing-line-one", "thm-jacquet-shalika", "thm-siegel-weil-convergent-doubling", "thm-ray-class-characters-galois", "thm-ray-class-field", "thm-clozel-regular-algebraic", "thm-godement-schur-orthogonality", "thm-disjoint-support-product-irreducible", "thm-unramified-doubling-gl", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range"]
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
