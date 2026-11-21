+++
kind  = "theorem"
title = "The Siegel–Weil formula for definite spaces"
provenance = "published"
source = "Weil [weil-1965]; Kudla–Rallis [kudla-rallis-1988]; Ichino [ichino-2004] for unitary groups"
lean  = ["GlobalTheory.ThK.Dbl.SiegelWeilStd", "PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd", "UpperTheory.LiteratureTheorems.siegel_weil_std_of_literature",
         "PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_ct", "PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_pre"]
order = 4
+++
Let $E/F$ be a CM extension, $A$ a hermitian space of dimension $m \ge 1$ and
$Y$ a skew-hermitian space of dimension $n \ge 1$ (or the reverse), with $A$
definite. Let $\chi$ be a Hecke character whose restriction to $\A_F^\times$ is
$\eta^m$, and $\Phi$ a Schwartz function in the doubling model that is
$K$-finite. Then the Siegel Eisenstein series of the section attached to
$\Phi$ is holomorphic at $s_0 = (m - n)/2$ and
$$E(g, s_0, \Phi) = c \int_{\U(A)(F)\backslash \U(A)(\A)} \theta(g, h; \Phi)\,dh,
\qquad c = \begin{cases} 1 & n < m,\\ 2 & n \ge m,\end{cases}$$
for the Haar measure of total volume one.
