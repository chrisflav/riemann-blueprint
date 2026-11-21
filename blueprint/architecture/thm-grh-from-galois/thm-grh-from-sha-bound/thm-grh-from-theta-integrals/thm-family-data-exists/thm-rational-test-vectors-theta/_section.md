+++
id    = "thm-rational-test-vectors-theta"
kind  = "theorem"
title = "Rational test vectors for twisted theta lifts"
lean  = ["GlobalTheory.RowClaim.Join.thetaLift_row_properties_conj"]
uses  = ["thm-grh-from-theta-integrals"]
order = 111
+++
Assume the published results of [thm-grh-from-theta-integrals] and the step
identities of theta towers ([def-theta-tower-step]), both for the towers
along the rows of the grid and for the towers that square them, together
with convergence of the theta integrals of Weil representations
$\omega$ of $\U(M) \times \U(X)$ whenever $\dim X < 2(\dim M - p)$, where $p$
is the smaller part of the signature of $M$ (Weil's convergence criterion).

Then, for all large scales $x$ and every choice of test data for the
twisted theta lifts on the families at scale $x$:

1. the finite sums that define the test vectors are well defined;
2. the normalising constants of the squared theta lifts are nonzero;
3. the twisted theta lifts of the test vectors converge;
4. there are a constant $\kappa \in \C$ and roots of unity $\zeta_t$ in the
   field $L$ of the family such that, at every good point $x$ and every
   index $a$,
   $$\zeta_t\,c_t\,\Psi_a\big(\vartheta_t(x)\big) = \kappa\,v_t(x, a),$$
   where $c_t$ is the total constant, $\vartheta_t$ the twisted theta lift
   and $\Psi_a$ the $a$-th test functional;
5. the values $v_t(x, a)$ lie in $L$.

So, up to one constant $\kappa$ and roots of unity, the theta lifts of the
test vectors take values in a number field. This is the rationality
step in the proof of [thm-family-data-exists].
