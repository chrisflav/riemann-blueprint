+++
kind = "proof"
of   = "smooth-of-relative-dimension-rep-fam-of-is-q-proj-over"
uses = ["abelian-de-rham", "abelian-de-rham-page", "abelian-lifting", "dual-abelian-scheme",
        "exists-universal-tangent-harris-taylor-representing-family", "grothendieck-deformation"]
+++
Use the infinitesimal lifting criterion over artinian rings: by Grothendieck's
deformation theory a point lifts along a square-zero thickening once the Hodge
filtration lifts, and the obstruction vanishes. The relative tangent spaces have
dimension $a(n-1)$ by [exists-universal-tangent-harris-taylor-representing-family].
