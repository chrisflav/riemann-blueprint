+++
kind  = "theorem"
title = "Pseudo-coefficients of discrete series of unitary groups"
provenance = "modified"
source = "after Clozel–Delorme [clozel-delorme-1984]"
lean  = ["GlobalTheory.PsCo.Pc.LocalPC", "GlobalTheory.PsCo.Pc.localPC_holds",
         "GlobalTheory.T.localPseudoCoefficientExistence_unitaryGroup"]
order = 1
+++
Let $r$ be odd, $\U(\varepsilon)$ the real unitary group of the diagonal form
with signs $\varepsilon \in \{\pm 1\}^r$, and $D$ a discrete series
representation with Harish-Chandra parameter $\lambda \in \Z^r$ whose gaps
are large. Then there is a smooth, compactly supported, bi-$K$-finite
function $f$ on $\U(\varepsilon)$ with $\mathrm{tr}\,D(f) = 1$ and
$\mathrm{tr}\,\pi(f) = 0$ for every irreducible unitary representation $\pi$
not equivalent to $D$.

This is the existence of pseudo-coefficients, here only for parameters
far from the walls.
