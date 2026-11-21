+++
kind = "proof"
of   = "thm-geometric-galois-odd-rank"
uses = ["thm-eigenspaces-crystalline", "thm-fontaine-bcris", "thm-hodge-tate-weights-eigenspaces", "thm-kuga-sato-unitary-shimura",
        "thm-transfer-unitary-shimura", "thm-galois-reps-hecke-eigenspaces"]
+++
Transfer $U$ to a Hecke eigensystem $\theta$ in the cohomology of a compact
unitary Shimura variety of signature $(1, a-1)$ at one infinite place and
$(0, a)$ at the others, twisted by an algebraic Hecke character
([thm-transfer-unitary-shimura]). The Kuga–Sato varieties over these Shimura varieties form
a tower of smooth projective varieties with finite étale Hecke
correspondences, with good reduction, the Eichler–Shimura congruence relation
and Hodge numbers read off the weight ([thm-kuga-sato-unitary-shimura]). The
last property rests on the holomorphic Lefschetz fixed-point formula of
Atiyah and Bott for finite étale correspondences, which the proof supplies as
a hypothesis and proves separately.

The general results on Hecke eigenspaces in étale cohomology
([thm-galois-reps-hecke-eigenspaces]) then give $\rho$: the congruence relation gives the
Frobenius eigenvalues, the crystalline comparison ([thm-eigenspaces-crystalline]) and
the Hodge–Tate decomposition ([thm-hodge-tate-weights-eigenspaces]) give the properties at
$l$. Twisting by the $l$-adic character of the Hecke character undoes the
twist.
