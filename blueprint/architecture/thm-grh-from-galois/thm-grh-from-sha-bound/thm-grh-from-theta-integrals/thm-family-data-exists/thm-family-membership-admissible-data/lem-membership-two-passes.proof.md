+++
kind = "proof"
of   = "lem-membership-two-passes"
uses = ["lem-constructed-points-from-depth-four", "thm-gross-cm-curves", "thm-weber-ray-class-field", "thm-siegel-main-theorem-hermitian"]
+++
Weber's theorem on ray class fields [thm-weber-ray-class-field], the
principal ideal theorem, the existence of CM elliptic curves with good
reduction outside a prime [thm-gross-cm-curves] and the ratio of masses from
Siegel's formula [thm-siegel-main-theorem-hermitian] give the condition on
base data. Every start extends to depth three, then to depth four, and then
to a constructed point by [lem-constructed-points-from-depth-four]; this
gives the condition on untwisted data. The same chain for $p'$, followed by
the passage to an enlarged base, gives the last condition.
