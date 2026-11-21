+++
kind = "proof"
of   = "geo-one-holds"
uses = ["crys-step-holds", "fontaine-bcris", "jump-step-holds", "kodaira-spencer-of-weight-one",
        "plan-ex-holds", "steps-holds"]
+++
Transfer $U$ to a Hecke eigensystem $\theta$ in the cohomology of a compact
unitary Shimura variety of signature $(1, a-1)$ at one infinite place and
$(0, a)$ at the others, twisted by an algebraic Hecke character
([plan-ex-holds]). The Kuga–Sato varieties over these Shimura varieties form
a tower of smooth projective varieties with finite étale Hecke
correspondences, with good reduction, the Eichler–Shimura congruence relation
and Hodge numbers read off the weight ([kodaira-spencer-of-weight-one]). The
last property rests on the holomorphic Lefschetz fixed-point formula of
Atiyah and Bott for finite étale correspondences, which the proof supplies as
a hypothesis and proves separately.

The general results on Hecke eigenspaces in étale cohomology
([steps-holds]) then give $\rho$: the congruence relation gives the
Frobenius eigenvalues, the crystalline comparison ([crys-step-holds]) and
the Hodge–Tate decomposition ([jump-step-holds]) give the properties at
$l$. Twisting by the $l$-adic character of the Hecke character undoes the
twist.
