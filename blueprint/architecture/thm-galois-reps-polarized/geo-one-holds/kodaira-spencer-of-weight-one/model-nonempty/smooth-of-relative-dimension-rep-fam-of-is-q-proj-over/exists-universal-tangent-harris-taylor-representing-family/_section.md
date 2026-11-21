+++
id    = "exists-universal-tangent-harris-taylor-representing-family"
kind  = "theorem"
title = "Universal first-order deformations"
lean  = ["GlobalTheory.HTUniv.main", "GlobalTheory.T.exists_universal_firstOrder_deformation_harrisTaylor",
         "GlobalTheory.T.exists_universal_tangent_harrisTaylor_representingFamily",
         "GlobalTheory.UPel.HT.RepTangent.exists_univ_tangent"]
order = 10
+++
Let $X$ be a smooth quasi-projective representing scheme as in
[model-nonempty], $k$ an algebraically closed field and $x \in X(k)$. Put
$r = a(n-1)$. There is a point $u$ of $X$ with values in
$k[\varepsilon_1, \dots, \varepsilon_r]/(\varepsilon_i\varepsilon_j)$, lifting $x$ over the
base, through which every first-order deformation
$v \in X(k[\varepsilon]/(\varepsilon^2))$ of $x$ over the base factors by a unique linear
map $k^r \to k$. So the relative tangent space at $x$ has dimension $r$.
