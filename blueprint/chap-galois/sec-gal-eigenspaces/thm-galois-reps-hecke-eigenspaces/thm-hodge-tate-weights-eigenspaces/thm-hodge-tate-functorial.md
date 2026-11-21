+++
kind  = "theorem"
title = "Functoriality of the Hodge–Tate decomposition"
provenance = "published"
source = "Faltings [faltings-1988]"
lean  = ["CrystallineSemistableComparison.HTSpecB.HTSpecGood", "UpperTheory.Gal.Seam.HT.htSpecGood"]
order = 2
+++
Let $K$ be a finite extension of $\Q_l$ and $n \ge 0$. For every smooth proper
$K$-variety $M$ with a smooth model and of pure dimension, there are bases
of $H^n_{\mathrm{et}}(M_{\bar K}, \Q_l)$ and of
$\bigoplus_a H^{n-a}(M, \Omega^a)$, whose sizes agree, and a matrix $\Phi_M$ over
$\C_l$ realising the Hodge–Tate decomposition
$$H^n_{\mathrm{et}}(M_{\bar K}, \Q_l) \otimes \C_l \cong \bigoplus_a H^{n-a}(M, \Omega^a) \otimes_K \C_l(-a).$$
For every morphism $u : M' \to M$ over $K$, the matrices of $u^*$ on étale and on
Hodge cohomology are intertwined by $\Phi_M$ and $\Phi_{M'}$.
