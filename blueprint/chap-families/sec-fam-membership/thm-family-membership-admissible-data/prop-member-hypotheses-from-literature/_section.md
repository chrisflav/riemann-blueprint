+++
id    = "prop-member-hypotheses-from-literature"
kind  = "remark"
title = "The published inputs used at the members"
lean  = ["GlobalTheory.MemberClose.exists_hyp_n_of_geometric_galois_compat",
         "GlobalTheory.T.hyps_e_third_layer_ser_n_of_geometric_galois"]
order = 1
+++
The steps that build the members use together the local representation
theory of $\GL_n$ ([def-local-rep-theory-package]), the automorphic forms
and their Galois representations ([def-automorphic-galois-inputs],
[def-non-endoscopic-package]), the analytic inputs of theta lifts
([def-theta-analytic-inputs]), and the Galois cohomology of
Poitou–Tate ([thm-poitou-tate]), Tate ([thm-tate-local-duality-l-adic],
[thm-tate-global-euler-characteristic]) and Greenberg–Wiles
([thm-greenberg-wiles]), with Chebotarev's theorem
([thm-chebotarev-degree-one]) and Artin reciprocity
([thm-artin-reciprocity]). From them, the non-vanishing of theta lifts
([thm-downward-theta-lift-nonvanishing]), the equality of multiplicities on
inner forms ([thm-inner-form-multiplicities-equal]) and the Hecke statements
of [prop-hecke-integrality-transformation] give a system of local
parameters ([def-local-parameters]) compatible with the archimedean local
Langlands correspondence and with the parameters at the members.
