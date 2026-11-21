+++
kind  = "theorem"
title = "The Rallis inner product formula in the convergent range"
source = "Rallis [rallis-1984]; Li [li-1992]"
lean  = ["GlobalTheory.Published.RallisInnerProductConvergent", "UpperTheory.Lit.Rallis.RallisIPProof.rallis_of_dm"]
order = 10
+++
Let $(\U(A), \U(B))$ be a unitary dual pair over a CM field with
$\operatorname{rank} A < \operatorname{rank} B \le 2\operatorname{rank} A$,
and either $B$ anisotropic or $\operatorname{rank} A + \mathrm{witt}(B) < \operatorname{rank} B$
(Weil's convergent range). Let $\sigma$ be an irreducible subrepresentation
of the cusp forms on $\U(A)$ whose theta lifts to all smaller groups of the
tower vanish. For Schwartz functions $\Phi_1, \Phi_2$ and $f_1, f_2 \in \sigma$:

* the theta integrals $\theta(\Phi_i, f_i)$ converge and are square-integrable
  on $\U(B)(F)\backslash\U(B)(\A_F)$;
* the doubling zeta integral at the point $s_0$ of the section attached to
  $\Phi_1 \otimes \overline{\Phi_2}$ equals
  $\operatorname{vol}^{-1}\,\langle\theta(\Phi_1, f_1), \theta(\Phi_2, f_2)\rangle$.

It is stated in the range where the Siegel–Weil formula of Weil applies.
