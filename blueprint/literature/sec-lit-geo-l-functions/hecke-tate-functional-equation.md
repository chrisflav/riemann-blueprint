+++
kind  = "theorem"
title = "Functional equation of Hecke L-functions over CM fields"
lean  = ["GlobalTheory.Published.HeckeTateFunctionalEquation", "GlobalTheory.Top.heckeTateFE"]
order = 3
+++
Let $E$ be a CM field with a CM type $\Phi$, and $\chi$ a unitary Hecke
character of $E$ with infinity type
$z \mapsto \prod_{\phi \in \Phi}(\phi(z)/|\phi(z)|)^{n_\phi}$, not all
$n_\phi$ zero, and conductor exponents $a_w$. Let
$$ \Lambda(\chi, s) = \prod_{\phi \in \Phi}\Gamma_\C\big(s + |n_\phi|/2\big) \cdot L(\chi, s), $$
with $\Gamma_\C(s) = 2(2\pi)^{-s}\Gamma(s)$. Then $\Lambda(\chi, s)$ and
$\Lambda(\chi^{-1}, s)$ (infinity type $-n$) extend to entire functions, and
$$ \Lambda(\chi, s) = (-i)^{\sum_\phi |n_\phi|}\,\varepsilon_f(\chi, s)\,\Lambda(\chi^{-1}, 1-s), $$
where $\varepsilon_f(\chi, s) = \prod_w \varepsilon_w(\chi, a_w, s)$ is the
product of the local root numbers at the ramified places.

This is the functional equation of Hecke (1918–20) and Tate (1950), in the
special case of a CM field and a character of non-trivial infinity type,
where the completed $L$-function has no poles.
