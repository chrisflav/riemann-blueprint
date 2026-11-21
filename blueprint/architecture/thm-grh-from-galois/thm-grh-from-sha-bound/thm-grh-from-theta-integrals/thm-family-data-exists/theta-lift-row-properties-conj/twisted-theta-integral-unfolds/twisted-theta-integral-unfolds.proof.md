+++
kind = "proof"
of   = "twisted-theta-integral-unfolds"
uses = ["cusp-rapid-decay", "cusp-step-of-large-flip-run", "flat-at-big", "hasse-norm-st"]
+++
Write the integral over the last row as an iterated integral, which is a
constant times a finite sum, and pass the relations between cell sums to the
integrals. At large depth the row period groups split into real and finite
parts, the unfolded integrand is invariant on both sides and is supported
on cells, and off the twisting places only one coset contributes. The
values on cells come from the Fock-model computation of
[flat-at-big]. A change of measures, the cell masses against the level
volumes and the reduction of periods to Fock vectors then give the stated
sum. Convergence uses [cusp-rapid-decay] and [cusp-step-of-large-flip-run].
