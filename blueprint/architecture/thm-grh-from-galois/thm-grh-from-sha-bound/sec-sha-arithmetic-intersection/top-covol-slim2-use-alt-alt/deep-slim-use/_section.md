+++
id    = "deep-slim-use"
kind  = "theorem"
title = "Lower bound for mean arithmetic volumes"
lean  = ["GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use", "PositivityTheory.HtPt.Ah.deep_slim_use"]
uses  = ["ar-calc", "fargues-exact", "nef-rr", "poincare-lelong-inv", "principalisation-char-zero", "resolution-char-zero", "semi-abelian-hom-extension", "thm-grh-from-theta-integrals", "zarhin-statement"]
order = 10
+++
Assume resolution and principalisation in characteristic zero
([resolution-char-zero], [principalisation-char-zero]), the inverse
Poincaré–Lelong formula ([poincare-lelong-inv]), the arithmetic
Hilbert–Samuel inequalities and Moriwaki's theorem, Fargues' exact
sequence ([fargues-exact]), Zarhin's theorem ([zarhin-statement]),
Riemann–Roch for nef bundles ([nef-rr]) and arithmetic degrees
([ar-calc]), extension of homomorphisms of semi-abelian schemes
([semi-abelian-hom-extension]), and the results [thm-grh-from-theta-integrals]
assumes.

Then there is $C \ge 0$ with the following property. Let $X$ be a unitary
Shimura variety of signature $(p, q)$ over a CM field $E$, attached to the
$j$-th member, $1 \le j < m$, of a family of [def-family-data] with $m^2 \le k$,
at a level with at most $15$ prime divisors. Let $u$ be a weight, strictly
decreasing in each embedding $\tau$, whose entries in positions $> p$ lie at
distance at least $g > 0$ from all other entries. Put
$B = 4|\Phi|(p+q)^2\big(1 + \max|u|/g\big)$ and
$\ell = \log \mathrm{rd}_E + |L'/L(1)|$, with $\mathrm{rd}_E$ the root
discriminant of $E$ and $L$ the Hecke $L$-function attached to $E$. Then the
mean over the connected components $Z$ of $X$ of the slopes
$\widehat{\mathrm{vol}}_Z(\omega(u)) / \deg_Z(\omega(u))$ of the arithmetic
volumes of the automorphic line bundle of weight $u$ is at least
$$-C\Big((\log B + \ell)\,\|u\|_1 + q\sum_\tau\big(\max_i u_{\tau i} - \min_i u_{\tau i}\big)\Big).$$
