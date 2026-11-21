+++
id    = "thm-rational-test-vectors-theta"
kind  = "theorem"
title = "Rational test vectors for twisted theta lifts"
provenance = "new"
lean  = ["GlobalTheory.RowClaim.Join.thetaLift_row_properties_conj"]
order = 111
+++
For all large scales $x$ and every choice of test data for the twisted
theta lifts on the families at scale $x$:

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
