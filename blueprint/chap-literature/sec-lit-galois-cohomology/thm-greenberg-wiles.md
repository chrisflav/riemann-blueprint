+++
kind  = "theorem"
title = "The Greenberg–Wiles formula"
provenance = "published"
source = "Greenberg; Wiles [wiles-1995]; see Darmon–Diamond–Taylor [darmon-1997]"
lean  = ["ReciprocityTheory.Gal.GreenbergWiles", "UpperTheory.Lit.greenbergWiles"]
order = 11
+++
Let $F$ be a number field, $l$ an odd prime, $S$ a finite set of finite
places containing those above $l$, $M$ a finite $\Z/l^r$-module with a
continuous action of $G_S$, and $M^* = M^\vee(1)$. For a family
$\mathcal L = (L_v)_{v \in S}$ of subgroups $L_v \subseteq H^1(F_v, M)$, with
dual family $\mathcal L^\perp$,
$$
\frac{|H^1_{\mathcal L}(F, M)|}{|H^1_{\mathcal L^\perp}(F, M^*)|}
= \frac{|H^0(F, M)|}{|H^0(F, M^*)|}
\prod_{v \in S}\frac{|L_v|}{|H^0(F_v, M)|}
\prod_{v \mid \infty}\frac{1}{|H^0(F_v, M)|}
$$
The archimedean local conditions are zero, which
is automatic since $l$ is odd.
