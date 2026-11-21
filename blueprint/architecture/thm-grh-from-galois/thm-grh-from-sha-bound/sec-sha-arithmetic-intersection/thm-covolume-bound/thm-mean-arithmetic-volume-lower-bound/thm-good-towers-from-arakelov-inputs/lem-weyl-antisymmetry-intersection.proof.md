+++
kind = "proof"
of   = "lem-weyl-antisymmetry-intersection"
uses = ["thm-abelian-variety-torsion-count", "lem-flag-cover-pullback", "thm-arithmetic-intersection-theory", "thm-semi-abelian-hom-extension"]
+++
For a simple reflection $s$, the flag bundle is a $\mathbb P^1$-bundle over a
partial flag bundle, and the square formed by its two projections exchanges
$\lambda$ and $s\lambda$. Flag covers ([lem-flag-cover-pullback]) realise this
square by flag models, and on such a fibre square
$\Delta(\lambda) + \Delta(s\lambda)$ vanishes. To pass from the flag models to
the tower one needs, besides the existence of the flag models and their
algebraic and height properties, that the metrics of the root line bundles on
the flag models agree with the base metric along every orbit outside the
boundary; this and the remaining base and comparison statements are proved
with the properties of arithmetic intersection numbers
([thm-arithmetic-intersection-theory]), extension of homomorphisms of
semi-abelian schemes ([thm-semi-abelian-hom-extension]) and multiplication by
$n$ on abelian schemes.
