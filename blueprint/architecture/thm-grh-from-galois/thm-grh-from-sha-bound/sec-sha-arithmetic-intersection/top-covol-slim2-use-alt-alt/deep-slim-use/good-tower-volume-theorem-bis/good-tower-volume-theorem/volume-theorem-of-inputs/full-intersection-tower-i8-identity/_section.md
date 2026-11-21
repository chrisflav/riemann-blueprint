+++
id    = "full-intersection-tower-i8-identity"
kind  = "lemma"
title = "Weyl antisymmetry of arithmetic intersection numbers"
lean  = ["GlobalTheory.CompanionTheory.Ar.Top.full_intersection_tower_I8_relation", "GlobalTheory.T.full_intersection_tower_I8_identity", "SquareStatements.good_tower_antisymmetry"]
uses  = ["ar-calc", "semi-abelian-hom-extension"]
order = 10
+++
Let $T$ be a good tower of [good-tower-volume-theorem] over a global model,
$p, q \ge 1$, with a full arithmetic intersection theory. For a weight $\lambda$
let $\mathcal L(\lambda)$ be the corresponding combination of root line
bundles, $n$ the relative dimension of the tower, and on each component $c$
put
$$\Delta_c(\lambda) = \widehat{\mathcal L(\lambda)}^{\,n+1}_c - \mathrm{vol}(c)\, h(\lambda),$$
the arithmetic self-intersection less its main term $h(\lambda)$. Then for
every simple reflection $s$ of the Weyl group that exchanges $a$ and $a + 1$
in one embedding, with $a + 1$ not the index $p$ of the signature,
$$\Delta_c(s\lambda) = -\Delta_c(\lambda).$$
