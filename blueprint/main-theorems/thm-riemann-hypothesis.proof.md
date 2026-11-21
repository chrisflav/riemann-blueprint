+++
kind = "proof"
of   = "thm-riemann-hypothesis"
uses = ["thm-half-plane", "lem-zeta-nonvanishing"]
+++
Let $\zeta(s) = 0$, with $s$ neither a trivial zero nor $1$. If
$\Re s > \tfrac12$, this contradicts [lem-zeta-nonvanishing]. Suppose
$\Re s < \tfrac12$. Then $s \ne 0$, since $\zeta(0) = -\tfrac12$. The
functional equation
$$ \zeta(1-s) = 2(2\pi)^{-s}\,\Gamma(s)\cos(\pi s/2)\,\zeta(s) $$
holds with $s$ and $1-s$ exchanged. On that side the power of $2\pi$ and
$\Gamma(1-s)$ do not vanish, and the cosine vanishes only at the trivial
zeros. So $\zeta(1-s) = 0$ with $\Re(1-s) > \tfrac12$, which again
contradicts [lem-zeta-nonvanishing].
