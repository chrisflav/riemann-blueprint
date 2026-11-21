+++
id    = "thm-de-rham-abelian-schemes"
kind  = "theorem"
title = "De Rham cohomology of abelian schemes"
provenance = "published"
source = "Oda [oda-1969]; Mazur–Messing [mazur-messing-1974]; Berthelot–Breen–Messing [berthelot-1982]"
lean  = ["GlobalTheory.Published.AbelianDeRham", "PositivityTheory.DualRT.abelianDeRham"]
order = 7
+++
Let $A$ be an abelian scheme of relative dimension $g$ over a ring $R$. Then:

* $H^1_{dR}(A/R)$ is finite projective of rank $2g$, all its classes are
  primitive, and cup product gives $\wedge^2 H^1_{dR} \cong H^2_{dR}$;
* the Hodge filtration $\omega_A \subset H^1_{dR}(A/R)$ is a direct summand of
  rank $g$, with $H^1_{dR}/\omega_A \cong \mathrm{Lie}(A^\vee)$;
* both are compatible with base change;
* (rigidity) for a nilpotent divided-power thickening $R \to R_0$, the map
  from $H^1_{dR}(A/R)$ to the crystalline cohomology of $A_0 = A \otimes R_0$ is
  bijective;
* (duality) the pairing of a polarisation makes $\omega_A$ isotropic, and is
  perfect when the polarisation is principal.
