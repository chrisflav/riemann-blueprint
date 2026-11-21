+++
id    = "twisted-multiplicity-one"
kind  = "theorem"
title = "Equal multiplicities on inner forms"
lean  = ["GlobalTheory.MultEqFinal.twisted_multiplicity_eq", "GlobalTheory.T.twisted_multiplicity_one",
         "UpperTheory.Lit.I5.unitary_theory_of_harishChandra_langlands_alt"]
uses  = ["bernstein-zelevinsky-finiteness", "cusp-rapid-decay", "cusp-trace-class",
         "discrete-series-classification", "dixmier-malliavin-factorisation", "flath-factorisation",
         "geometric-lemma", "green-cuspidal", "harish-chandra-analyticity", "harish-chandra-finite"]
order = 121
+++
Assume the results of Harish-Chandra on analyticity and finiteness
([harish-chandra-analyticity], [harish-chandra-finite]), the classification of
discrete series [discrete-series-classification], rapid decay and trace
class of cusp forms ([cusp-rapid-decay], [cusp-trace-class]), the
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
