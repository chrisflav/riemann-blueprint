+++
kind  = "lemma"
title = "Period matrices of a p-divisible group"
provenance = "new"
lean  = ["GlobalTheory.QLog.WindowMat.window_matrices"]
order = 10
+++
Let $C$, $\mathcal O_C$ and $\varepsilon$ be as in [thm-dieudonne-theory-oc],
and let $G$ be a $p$-divisible group over $\mathcal O_C$ of height $h$,
connected with connected dual, of dimension $d$ with $d + k = h$. For every
frame $(B, \sigma, \theta)$ over $A_{\inf}$ there are matrices $U$ (invertible,
size $h \times h$), $Y$ and $\Gamma$ over $B$, a $\Z_p$-basis of the Tate
module of $G$ with a dual basis of that of $G^\vee$, and bases of
$\omega_G$ and $\mathrm{Lie}(G^\vee)$, such that
$$\sigma(Y) = \begin{pmatrix} p & 0 \\ 0 & 1\end{pmatrix} U^{T} Y, \qquad \Gamma\,Y = \mu \cdot 1,$$
the Frobenius matrices are topologically nilpotent modulo $\theta$, and
$\theta$ applied to the entries of $Y$ and $\Gamma$ gives the Hodge–Tate map
and the logarithm $d\log$ in the chosen bases.
