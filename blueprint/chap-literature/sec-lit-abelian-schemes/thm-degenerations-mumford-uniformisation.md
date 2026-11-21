+++
kind  = "theorem"
title = "Degenerating abelian varieties have Mumford uniformisations"
provenance = "published"
source = "Mumford [mumford-1972]; Faltings–Chai [faltings-chai-1990]"
lean  = ["GlobalTheory.T.exists_degenerationData_uniformisation_of_torsionCount",
         "GlobalTheory.T.exists_pel_uniformisation_complete_dvr"]
order = 13
+++
Let $V$ be a complete discrete valuation ring with fraction field $K$, and $A$
a principally polarised abelian variety over $K$. Let $G$ be a semi-abelian
scheme over $V$ with generic fibre $A$, with a cubical structure on the
extension of the polarisation, whose toric part over the special fibre is
split with character group $X$. Then there are degeneration data for $G$, in
the sense of Mumford's construction [thm-mumford-degeneration], and a Mumford
uniformisation of $A$ by these data that is compatible with the polarisation,
with the identification of $A$ with the generic fibre of $G$ and with the
cubical structure.

The same holds for abelian varieties with an action of the ring of integers of
a CM field and a compatible polarisation (the PEL case), with a uniformisation
that respects the action.

This is the converse of [thm-mumford-degeneration].
