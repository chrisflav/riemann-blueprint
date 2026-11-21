+++
kind = "proof"
of   = "thm-kuga-sato-unitary-shimura"
uses = ["thm-abelian-variety-torsion-count", "thm-de-rham-abelian-schemes", "lem-hodge-filtration-abelian-scheme", "thm-abelian-scheme-lifting-divided-powers", "thm-dual-abelian-scheme",
        "thm-hecke-fixed-points-kuga-sato", "thm-grothendieck-messing", "thm-hodge-numbers-eigenspaces", "thm-unitary-shimura-integral-models",
        "thm-semi-abelian-hom-extension", "thm-semistable-reduction", "thm-semi-abelian-theta-models"]
+++
The integral models of the Shimura varieties come from [thm-unitary-shimura-integral-models]: a
smooth quasi-projective moduli scheme, proper because the datum is compact.
Fibre powers of the universal abelian scheme are smooth and projective, and
the Hecke correspondences are finite étale. Good reduction uses the
semistable reduction theorem, extension of homomorphisms of semi-abelian
schemes and [thm-semi-abelian-theta-models]. The Hodge exponents
come from [thm-hodge-numbers-eigenspaces], which compares the holomorphic
Lefschetz formula of Atiyah and Bott (1968) with the fixed points of
[thm-hecke-fixed-points-kuga-sato]. For a finite étale correspondence on a
smooth projective complex variety $Z$ with transversal fixed points, that
formula says that the alternating sum over $b$ of the traces on
$H^b(Z, \Omega^a)$ equals the sum, over the fixed points $y$, of the
coefficient of $X^a$ in $\det(1 + XA_y)/\det(1 - A_y)$, where $A_y$ is the
action on the tangent space.
