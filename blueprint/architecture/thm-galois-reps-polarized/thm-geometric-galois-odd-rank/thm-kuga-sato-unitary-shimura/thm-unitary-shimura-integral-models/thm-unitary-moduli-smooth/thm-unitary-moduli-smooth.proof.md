+++
kind = "proof"
of   = "thm-unitary-moduli-smooth"
uses = ["thm-de-rham-abelian-schemes", "lem-hodge-filtration-abelian-scheme", "thm-abelian-scheme-lifting-divided-powers", "thm-dual-abelian-scheme",
        "thm-universal-first-order-deformation", "thm-grothendieck-messing"]
+++
Use the infinitesimal lifting criterion over artinian rings: by Grothendieck's
deformation theory a point lifts along a square-zero thickening once the Hodge
filtration lifts, and the obstruction vanishes. The relative tangent spaces have
dimension $a(n-1)$ by [thm-universal-first-order-deformation].
