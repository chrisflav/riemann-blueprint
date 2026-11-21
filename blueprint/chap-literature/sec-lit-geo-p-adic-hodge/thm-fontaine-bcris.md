+++
kind  = "theorem"
title = "Fontaine's theorems on the crystalline period ring"
provenance = "published"
source = "Fontaine [fontaine-1982], [fontaine-1994a]"
lean  = ["GlobalTheory.MemLoc.fontaineBcris", "GlobalTheory.Published.FontaineBcris"]
order = 1
+++
Let $l$ be a prime and let $B_{\mathrm{cris}} \subset B_{\mathrm{dR}}$ be
Fontaine's period rings over $\Qlbar$, with Frobenius $\varphi$ and
filtration $\mathrm{Fil}^\bullet$. Then:

* the map $\Qlbar \otimes_{K_0^{\mathrm{ur}}} B_{\mathrm{cris}} \to B_{\mathrm{dR}}$
  is injective, where $K_0^{\mathrm{ur}}$ is the maximal unramified extension
  of $\Q_l$; in particular $B_{\mathrm{cris}} \to B_{\mathrm{dR}}$ is
  injective, and so is $\varphi$;
* (fundamental exact sequence) $B_{\mathrm{cris}}^{\varphi = 1} \cap
  \mathrm{Fil}^0 B_{\mathrm{dR}} = \Q_l$, and
  $B_{\mathrm{dR}} = B_{\mathrm{cris}}^{\varphi = 1} + \mathrm{Fil}^0 B_{\mathrm{dR}}$;
* every $y \in B_{\mathrm{cris}}$ is $\varphi(x) - x$ for some $x$ with
  image in $\mathrm{Fil}^0 B_{\mathrm{dR}}$;
* (regularity) a non-zero $b \in B_{\mathrm{cris}}$ on which $G_K$ acts
  through a $\Q_l$-valued character, for some finite $K/\Q_l$, is a unit.
