+++
kind = "proof"
of   = "lem-twisted-theta-unfolding"
uses = ["thm-cusp-rapid-decay", "lem-grid-steps-preserve-cusp-forms", "lem-twisted-vacua-real-points", "thm-hasse-norm-quadratic"]
+++
Write the integral over the last row as an iterated integral, which is a
constant times a finite sum, and pass the relations between cell sums to the
integrals. At large depth the row period groups split into real and finite
parts, the unfolded integrand is invariant on both sides and is supported
on cells, and off the twisting places only one coset contributes. The
values on cells come from the Fock-model computation of
[lem-twisted-vacua-real-points]. A change of measures, the cell masses against the level
volumes and the reduction of periods to Fock vectors then give the stated
sum. Convergence uses [thm-cusp-rapid-decay] and [lem-grid-steps-preserve-cusp-forms].
