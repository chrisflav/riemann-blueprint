+++
kind  = "theorem"
title = "Kummer classes of Siegel units are congruent to Eisenstein series"
lean  = ["GlobalTheory.T.siegelUnit_edgeClass_kummer_dlog_congruence", "GlobalTheory.pair_edge_dlog",
         "UpperTheory.Kd.L.one"]
order = 10
+++
For every prime $l$ there is $c$ with the following property. Let $N \ge 1$,
let $c, d$ be as in [thm-siegel-units-diamond], $m, n \ge 1$, $x \in \Z/N$, and
$\gamma \in \Gamma_0(N)$ with $l$ dividing neither entry of its first column.
Let $E$ be the Eisenstein series of level $Nl^{m+n}$ attached to $c, d, x$
and $\gamma$. Then the coefficients of $E$ are $l$-integral, and there is an
integral $\xi$ such that for every $s$ fixing the relevant roots of unity,
acting on $\mu_{l^{m+2n}}$ through $t \in \Z/l^n$, and every $q$-expansion
$\varphi$ that is the logarithmic derivative of the Kummer class of the
translate of the Siegel unit by $\gamma$,
$$l^c\varphi_r \equiv s(\xi_r) - \xi_r + l^c\,N^3\,a_r(E)\,t \bmod l^n.$$
This is the classical identity $\mathrm{dlog}\,g_{c,d} = $ Eisenstein series
of weight 2, read modulo $l^n$ through Kummer theory.
