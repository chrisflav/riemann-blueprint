+++
kind = "proof"
of   = "thm-unitary-rigid-boundary-charts"
uses = ["lem-unitary-boundary-separation", "lem-unitary-boundary-prechart", "thm-abelian-variety-torsion-count",
        "thm-semi-abelian-hom-extension", "thm-gaga-sections"]
+++
Start from the minimal compactification and the separation property of the
boundary ([lem-unitary-boundary-separation]), and let $S$ be the blow-up
that $\varphi$ determines. By [lem-unitary-boundary-prechart] every boundary
point of $S$ has a pre-chart. Extension of homomorphisms of semi-abelian
schemes ([thm-semi-abelian-hom-extension]) and the existence of Serre's
holomorphic sections ([thm-gaga-sections]) turn pre-charts into rigid charts
and give the ample bundle; multiplication by $n$ on abelian schemes enters
along the way.
