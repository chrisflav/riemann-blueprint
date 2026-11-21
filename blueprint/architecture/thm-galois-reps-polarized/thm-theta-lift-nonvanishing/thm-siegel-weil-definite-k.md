+++
kind  = "theorem"
title = "The Siegel–Weil formula for a definite space"
provenance = "published"
source = "Weil [weil-1965]; Kudla–Rallis [kudla-rallis-1988]; Ichino [ichino-2004] for unitary groups"
lean  = ["GlobalTheory.ThK.Dbl.SiegelWeilStd_k", "PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_k",
         "PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_ct_k",
         "PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_pre_k"]
order = 10
+++
Let $E/F$ be a quadratic extension of number fields, $A$ a hermitian (or
skew-hermitian) space of dimension $m$ whose signatures $(r, s)$ have
$\min(r, s) = 0$, and $Y$ a skew-hermitian (or hermitian) space of dimension
$n$; let $\chi$ be a splitting Hecke character. For every $K$-finite Schwartz
function $\Phi$ on the doubled space,
$$E\Big(g, \tfrac{m-n}{2}, \Phi\Big) = c \int_{\U(A)(F)\backslash \U(A)(\A_F)} \theta(g, h, \Phi)\, dh,$$
with $c = 1$ if $n < m$ and $c = 2$ otherwise; here $E$ is the Siegel Eisenstein
series, $\theta$ the theta function and the measure is the normalised Haar
measure on a fundamental domain.
