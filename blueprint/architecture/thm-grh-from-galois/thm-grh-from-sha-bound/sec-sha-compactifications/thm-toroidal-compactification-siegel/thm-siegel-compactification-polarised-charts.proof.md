+++
kind = "proof"
of   = "thm-siegel-compactification-polarised-charts"
uses = ["thm-abelian-variety-torsion-count", "lem-siegel-minimal-blowup-smooth", "thm-semi-abelian-hom-extension", "thm-semistable-reduction", "thm-gaga-sections", "thm-semi-abelian-theta-models", "thm-degenerations-mumford-uniformisation", "thm-complex-theta-uniformisation"]
+++
Take the minimal compactification $Z$ of $A_{g,n}$ and the normalised blow-up
$S \to Z$ along the ideal that $\varphi$ determines. By
[lem-siegel-minimal-blowup-smooth], $S$ is smooth with charts at
every point. The semi-abelian scheme extends over $S$ by Mumford's
construction, which near the boundary describes every degeneration
([thm-degenerations-mumford-uniformisation]); the
[theta uniformisation](@thm-complex-theta-uniformisation) of complex abelian
varieties also enters. Homomorphisms of semi-abelian schemes extend, and the ample
bundle on $Z$ pulls back to a power of $\omega$. The polarisation of
$\varphi$ makes $\omega^{Nk}(-\Delta)$ ample.
