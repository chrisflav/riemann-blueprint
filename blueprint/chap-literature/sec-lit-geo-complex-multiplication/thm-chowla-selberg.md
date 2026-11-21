+++
kind  = "theorem"
title = "The Chowla–Selberg formula"
provenance = "published"
source = "Chowla–Selberg [chowla-selberg-1967]"
lean  = ["GlobalTheory.chowla_selberg_eta", "GlobalTheory.chowla_selberg_lattice",
         "GlobalTheory.chowla_selberg_discriminant", "GlobalTheory.T.meanLogPeriod_chowlaSelberg"]
order = 5
+++
Let $K$ be an imaginary quadratic field of discriminant $-d$ with $d > 4$,
class number $h$ and quadratic character $\chi$. For each ideal class $c$
choose $\tau_c$ in the upper half-plane such that the lattice of an ideal in
$c$ is homothetic to $\Z\tau_c + \Z$. Then
$$\frac1h\sum_{c}\log\big(4\pi\,\Im(\tau_c)\,|\eta(\tau_c)|^4\big)
= \gamma + \log\frac{2\pi}{\sqrt d} - \frac{L'}{L}(1,\chi),$$
where $\eta$ is Dedekind's eta function. Equivalently, for ideals
$\mathfrak a_c$ in the classes $c$, with lattices $L_c \subset \C$ and
invariants $g_2, g_3$, the mean over $c$ of
$$\log\frac{\mathrm{covol}(L_c)}{\pi} + \frac16\log|g_2^3 - 27g_3^2|$$
is $\gamma + \log(2\pi/\sqrt d) - \frac{L'}{L}(1,\chi)$, and the mean of
$\log\big(N(\mathfrak a_c)^6\,|g_2^3 - 27g_3^2|\big)$ is
$12\log 2\pi - 6\log d + 6\gamma - 6\,\frac{L'}{L}(1,\chi)$.
