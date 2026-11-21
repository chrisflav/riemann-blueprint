+++
kind  = "theorem"
title = "Ohsawa–Takegoshi L2 extension from points"
provenance = "modified"
source = "after Ohsawa–Takegoshi [ohsawa-takegoshi-1987]; Demailly [demailly-2000]"
lean  = ["GlobalTheory.Published.L2ExtensionLogCanonical", "GlobalTheory.l2ExtensionLogCanonical'"]
order = 4
+++
Let $Y$ be a compact complex manifold of dimension $n$ with a hermitian line
bundle of positive curvature. Let $L$ and $E$ be hermitian line bundles and
$s = (s_1, \dots, s_n)$ sections of $L$ with $|s| \le 1$, whose common zero
set $Z$ is finite and non-degenerate (non-zero Jacobian). Put
$\psi = n \log |s|^2$ and suppose that, for some $\delta > 0$, the weight of
$E$ plus $\alpha\psi$ is plurisubharmonic off $Z$ for every
$\alpha \in [1, 1+\delta]$. Then every function $f$ on $Z$ extends to a
section $F$ of $K_Y \otimes E$ with
$$ \int_Y \frac{2^n\, |F|^2 e^{-\psi}}{1 + \delta^2\psi^2} ;\le; \frac{34}{\delta}\cdot\frac{2^{n+1}\pi^n}{(n-1)!} \sum_{P \in Z} \frac{|f(P)|^2}{|\mathrm{Jac}_s(P)|^2}, $$
where the norms at $P$ are taken in the metrics of $E$ and $L^{n}$.

This is the $L^2$ extension theorem in Demailly's form for subvarieties cut
out by sections with log canonical
weight, specialised to a finite set of points.
