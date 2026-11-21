+++
id    = "thm-inner-form-multiplicities-equal"
kind  = "theorem"
title = "Equal multiplicities on inner forms"
lean  = ["GlobalTheory.MultEqFinal.twisted_multiplicity_eq", "GlobalTheory.T.twisted_multiplicity_one",
         "UpperTheory.Lit.I5.unitary_theory_of_harishChandra_langlands_alt"]
uses  = ["thm-bz-finiteness", "thm-cusp-rapid-decay", "thm-cusp-trace-class",
         "thm-hc-discrete-series-classification", "thm-dixmier-malliavin", "thm-flath-unramified",
         "thm-geometric-lemma", "thm-green-parametrisation", "thm-hc-analyticity-density", "thm-hc-finiteness-unitary"]
order = 121
+++
Assume the results of Harish-Chandra on analyticity and finiteness
([thm-hc-analyticity-density], [thm-hc-finiteness-unitary]), the classification of
discrete series [thm-hc-discrete-series-classification], rapid decay and trace
class of cusp forms ([thm-cusp-rapid-decay], [thm-cusp-trace-class]), the
factorisations of Dixmier–Malliavin and Flath, Bernstein–Zelevinsky
finiteness, the geometric lemma and Green's classification. Let a family
member satisfy the standing hypotheses. Let $Y_0$ be the base hermitian
space and $W_i$ another hermitian space whose unitary group is isomorphic
to that of $Y_0$ at every finite place, by an isomorphism $\Phi$ matching
the level groups. Then for every irreducible admissible representation
$\sigma$ of $\U(Y_0)(\A_f)$ of good type,
$$m_{\mathrm{cusp}}(\sigma \otimes \pi_\infty) = m_{\mathrm{cusp}}(\sigma \circ \Phi^{-1} \otimes \pi'_\infty),$$
where $\pi_\infty$, $\pi'_\infty$ are the corresponding discrete series of
the two real groups.

This is a transfer of cuspidal multiplicities between inner forms, of the
kind that the simple trace formula with pseudo-coefficients gives.
