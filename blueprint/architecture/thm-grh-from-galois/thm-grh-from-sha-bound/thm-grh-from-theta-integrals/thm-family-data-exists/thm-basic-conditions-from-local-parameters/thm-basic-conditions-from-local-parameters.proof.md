+++
kind = "proof"
of   = "thm-basic-conditions-from-local-parameters"
uses = ["thm-bz-finiteness", "thm-borel-casselman", "thm-casselman-wallach", "thm-cusp-rapid-decay",
        "thm-cusp-trace-class", "thm-depth-zero-support", "thm-hc-discrete-series-classification", "thm-discrete-series-parametrisation",
        "thm-discrete-series-exist", "thm-dixmier-malliavin", "thm-zelevinsky-segments",
        "thm-flath-unramified", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-green-parametrisation",
        "thm-green-regular-characters", "thm-hc-analyticity-density", "thm-hc-finiteness-unitary",
        "thm-hc-modules-unitary", "thm-hasse-norm-quadratic", "thm-jacquet-irreducible-admissible",
        "prop-isometric-period-identity", "thm-inner-form-multiplicities-equal",
        "thm-weil-representation-auxiliary-pairs", "prop-defect-condition"]
+++
Each of the twelve conditions comes from its own group of published results.

* Primitivity and decomposition points hold by construction of the data.
* Compatibility conditions come from the existence of the Weil representation of unitary dual
  pairs, Harish-Chandra's finiteness theorem, the theory of discrete series
  and the rapid decay of cusp forms. With primitivity and decomposition
  points they also give the selection jumps.
* The multiplicity condition is the isometric period identity of
  [prop-isometric-period-identity], which rests on unramified
  Howe duality, the Siegel–Weil formula, the doubling method and strong
  approximation. The same results give the divisor condition.
* The $\lambda'$ and $\kappa$ conditions come from the representation theory
  of the real groups: Harish-Chandra's analyticity theorem, Dixmier–Malliavin
  factorisation, Flath's theorem, the geometric lemma of Bernstein and
  Zelevinsky and Green's classification ([thm-green-parametrisation]).
* Goodness and labels come from the local parameters and Green's regular
  characters; weak geometric compatibility comes from the compatibility conditions and the
  divisor condition through class field theory.
* The defect condition is [prop-defect-condition].
