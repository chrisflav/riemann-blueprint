+++
id    = "lem-siegel-weil-singular-coefficients"
kind  = "lemma"
title = "Singular Fourier coefficients in the Siegel–Weil formula"
provenance = "new"
lean  = ["GlobalTheory.CompanionTheory.WeilSiegel.Deg.siegelDeg", "PositivityTheory.GramSchwartzFunctions.BC.SiegelDeg"]
order = 10
+++
Let $V$ be a hermitian space and $\varphi$ a Schwartz function on
$V^r$ satisfying the standing hypotheses. For every singular hermitian
matrix $\beta$ of size $r$, the $\beta$-th Fourier coefficient of the theta
integral,
$$\int_{\U(V)(F)\backslash\U(V)(\A)}\ \sum_{x \in V^r,\ \mathrm{rk}\,x = r,\ (x,x) = \beta}\varphi(h^{-1}x)\,dh,$$
equals the $\beta$-th Whittaker coefficient $W_\beta(\varphi)$ of the Siegel
Eisenstein series.
