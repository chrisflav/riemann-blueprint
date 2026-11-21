+++
kind  = "theorem"
title = "Artin reciprocity"
lean  = ["GlobalTheory.Published.GlobalArtinReciprocity", "GlobalTheory.globalArtinReciprocity_holds"]
order = 1
+++
Let $E$ be a number field with algebraic closure $\bar E$. There is a
continuous open surjection
$$ \mathrm{Art}_E : \A_E^\times \to \Gal(\bar E/E)^{\mathrm{ab}} $$
such that:

* its kernel is the closure of $E^\times \cdot (E_\infty^\times)^\circ$;
* for every finite place $v$ and every place of $\bar E$ above it, the local
  units $\mathcal O_v^\times$ map onto the image of inertia, and a
  uniformiser at $v$ maps to the image of a geometric Frobenius;
* the closure of the image of $E_v^\times$ is the image of the
  decomposition group.

This is the reciprocity law of Artin (1927) with the existence theorem of
Takagi, in the idelic form of Chevalley, normalised so that uniformisers
go to geometric Frobenius elements.
