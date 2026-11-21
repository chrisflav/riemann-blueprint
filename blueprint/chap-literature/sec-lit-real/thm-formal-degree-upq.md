+++
kind  = "theorem"
title = "Harish-Chandra's formal degree formula for U(p, q)"
provenance = "modified"
source = "after Harish-Chandra [harish-chandra-1966]"
lean  = ["GlobalTheory.Published.FormalDegreeCompactDual", "PositivityTheory.RgFd.B.formalDegreeCompactDual"]
order = 17
+++
Fix Haar measures on the groups $\U(p, q)$, $p + q = N$, compatible with a
fixed measure on the compact dual. Let $\sigma$ be a discrete series
representation of $\U(p, q)$ with Harish-Chandra parameter
$\lambda_1 > \dots > \lambda_N$, $\lambda_a \in \Z + (N-1)/2$. Then for every
non-zero vector $w$,
$$ \frac{\|w\|^4}{\int_{\U(p,q)} |\langle w, \sigma(g) w\rangle|^2\, dg} = \prod_{a < b}\frac{|\lambda_a - \lambda_b|}{b - a}. $$

The left side is the formal degree of $\sigma$. The measure is normalised by
the compact dual $\U(N)$,
where the right side is the Weyl dimension formula.
