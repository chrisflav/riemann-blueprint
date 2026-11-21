+++
kind = "proof"
of   = "thm-labesse-base-change"
uses = ["thm-base-change-unitary", "thm-bz-finiteness", "thm-jacquet-irreducible-admissible", "thm-bz-derivative-leibniz"]
+++
Start from the isobaric base change of [thm-base-change-unitary], which gives
the local component of $\pi$ as a subquotient of the product of the local
components of the $\Pi_i$. These are unitarisable, so their product is
irreducible, and the subquotient is the whole product. The proof works with
the Grothendieck ring of [thm-bz-finiteness], admissibility
[thm-jacquet-irreducible-admissible] and the Leibniz rule for the order of
vanishing of Bernstein–Zelevinsky derivatives [thm-bz-derivative-leibniz];
*we read* these as the inputs to the irreducibility.
