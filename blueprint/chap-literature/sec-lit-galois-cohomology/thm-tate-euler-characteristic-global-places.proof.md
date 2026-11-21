+++
kind = "proof"
of   = "thm-tate-euler-characteristic-global-places"
uses = ["thm-tate-euler-characteristic-l-adic"]
+++
The decomposition group is the absolute Galois group of the completion
$F_v$, a finite extension of $\Q_p$, with $[F_v : \Q_p]$ the local degree.
If $p = l$, apply [thm-tate-euler-characteristic-l-adic]. If $p \ne l$, use the formula
$\# H^1 = \# H^0 \cdot \# H^2$ for $l$-power modules over finite extensions
of $\Q_p$, which we prove separately.
