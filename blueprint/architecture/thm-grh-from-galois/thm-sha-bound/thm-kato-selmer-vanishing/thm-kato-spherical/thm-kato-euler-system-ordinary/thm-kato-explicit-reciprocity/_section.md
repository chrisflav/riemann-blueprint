+++
id    = "thm-kato-explicit-reciprocity"
kind  = "theorem"
title = "Kato's explicit reciprocity law"
lean  = ["UpperTheory.V.Z.Kato.Joint.SmoothedZetaClassHodgeTateLawStatement",
         "UpperTheory.V.Z.Kato.K5.smoothedZetaClass_hodgeTateLaw", "UpperTheory.V.Z.Kato.K5.top"]
order = 11
+++
Let $W$, $g$ and the data on modular functions be as in
[thm-kato-zeta-integral], and let $(Y_r)$ be a norm-compatible system
of integral zeta classes there. Let $\lambda$ be a linear functional on
$q$-expansions that is equivariant for the admissible Hecke operators with
the eigenvalues of $g$, and $d_0 \ge 2$ prime to $l$. Then there are
$m_0, c_1$, a constant $\kappa \ne 0$ and units $v_m$ with
$v_{m+1} \equiv v_m \bmod l^m$ such that the *smoothed* classes
$Y_r - d_0\,Y_r(\,\cdot\,d_0)$ obey the following law at $l$: at level $m$,
their image under the Hodge–Tate map is congruent, modulo $l^{m - c_1}$, to
$$(1 - d_0\psi^{-1}(d_0))\,v_m\,\kappa\,\Big(\sum_{a \bmod l^m}\psi(a)z^a\Big)\,\psi^{-1}(N)\;\lambda\big(E_{m}\big),$$
where $z$ is a formal variable and $E_m$ is an explicit combination, with
the coefficients $c_x$, of Eisenstein series of level $Nl^m$ built from $c, d$
and a character $\psi$ of conductor $l^m$.

This is Kato's explicit reciprocity law (Kato, 2004), in a congruence form
at each finite level.
