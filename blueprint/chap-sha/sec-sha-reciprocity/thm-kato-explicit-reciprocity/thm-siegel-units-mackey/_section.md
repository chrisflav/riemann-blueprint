+++
id    = "thm-siegel-units-mackey"
kind  = "theorem"
title = "Mackey decomposition of Siegel unit classes"
provenance = "new"
lean  = ["UpperTheory.Kd.L.mackey"]
order = 2
+++
For every odd prime $l$ there is $c$ with the following property. Keep the
notation of [thm-siegel-units-diamond], let $w$ be odd and $m, n \ge 1$, and let $b$ lift the
Kummer classes of the translated Siegel units, of weight $w$, modulo $l^n$.
Let $R$ be a set of representatives for the cosets of the subgroup fixing
the relevant roots of unity. Then for every unit $z \bmod l^{m+n}$ there is
an integral $\xi$ such that, for every $s$ in the inertia group at $l$ that
fixes $\mu_{l^{m+n}}$ and acts on $\mu_{l^{m+2n}}$ through $t \in \Z/l^n$, and
every $q$-expansion $\varphi$ that is the image $\Theta$ of the
corresponding class,
$$l^c\varphi_r \equiv s(\xi_r) - \xi_r + l^c\,l^{c_0}\,F_r\,t \bmod l^n,$$
where $F$ is the sum over $R$ of the Eisenstein coefficients of [thm-siegel-units-eisenstein].
