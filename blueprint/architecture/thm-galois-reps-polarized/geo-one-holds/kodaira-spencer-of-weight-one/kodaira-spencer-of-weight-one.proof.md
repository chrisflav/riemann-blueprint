+++
kind = "proof"
of   = "kodaira-spencer-of-weight-one"
uses = ["ab-mul-n-st", "abelian-de-rham", "abelian-de-rham-page", "abelian-lifting", "dual-abelian-scheme",
        "fix-k-holds", "grothendieck-deformation", "ks-hodge-of-geo", "model-nonempty",
        "semi-abelian-hom-extension", "semistable-reduction-st", "zarhin-geometric-of-semistable-reduction"]
+++
The integral models of the Shimura varieties come from [model-nonempty]: a
smooth quasi-projective moduli scheme, proper because the datum is compact.
Fibre powers of the universal abelian scheme are smooth and projective, and
the Hecke correspondences are finite étale. Good reduction uses the
semistable reduction theorem, extension of homomorphisms of semi-abelian
schemes and [zarhin-geometric-of-semistable-reduction]. The Hodge exponents
come from [ks-hodge-of-geo], which compares the holomorphic Lefschetz
formula with the fixed points of [fix-k-holds].
