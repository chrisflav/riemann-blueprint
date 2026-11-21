+++
id    = "thm-zero-free-from-windows"
kind  = "theorem"
title = "Zero-freeness from bounds on windows"
provenance = "new"
lean  = ["Formalism.HC.zeroFreeOn_of_tiedWin_cyc", "Formalism.HC.level_of_tiedWin"]
uses  = ["def-chebyshev-weighted", "def-zero-free-primitive"]
order = 3
+++
Suppose that for every primitive $\psi$ and every small $\varepsilon$ there
are windows $[Y, Y^\lambda]$ of arbitrarily large $Y$ on which
$$G_m(x) \le x^{1/2 + c\varepsilon},$$
with $c$ independent of $\varepsilon$. Then primitive $L$-functions do not
vanish right of the critical line.
