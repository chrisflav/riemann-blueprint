+++
id    = "prop-defect-condition"
kind  = "proposition"
title = "The defect condition"
lean  = ["GlobalTheory.Fc.RL.DefSide.linkedAt_df_of_parameters",
         "GlobalTheory.Fc.RL.linkedAt_prmR_df_of_cuspRapidDecay", "GlobalTheory.T.weil_unitary_entries'"]
uses  = ["thm-cusp-rapid-decay", "def-local-parameters", "thm-discrete-series-exist", "thm-hc-finiteness-unitary",
         "thm-weil-representation-auxiliary-pairs"]
order = 2
+++
For any construction data built from a system of local parameters
([def-local-parameters]), the defect condition holds eventually at every
admissible datum of the families. The defect condition is the norm bound on
the definite side of [prop-definite-side-norm-bounds].

The statement lists the Weil representation of unitary dual pairs, the
existence of discrete series, Harish-Chandra's finiteness theorem and the
rapid decay of cusp forms as hypotheses, but the proof does not use them.
