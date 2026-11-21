+++
kind  = "theorem"
title = "A de Rham representation has as many Hodge–Tate weights as its dimension"
source = "classical; see Fontaine [fontaine-1994b]"
lean  = ["GlobalTheory.HeightCounting.HtCard", "GlobalTheory.HtCardProof.htCard"]
order = 6
+++
Let $r : G_E \to \GL_a(\Qlbar)$ be a continuous representation of the Galois
group of a CM field $E$, $w$ a place above
$l$ and $\tau : E \to \Qlbar$ an embedding inducing $w$. If $r|_{G_w}$ is de
Rham, then its multiset of $\tau$-Hodge–Tate weights has exactly $a$ elements,
counted with multiplicity. This is a basic fact of $p$-adic Hodge theory:
the graded pieces of the filtration on $D_{\mathrm{dR}}$ have
total dimension $a$.
