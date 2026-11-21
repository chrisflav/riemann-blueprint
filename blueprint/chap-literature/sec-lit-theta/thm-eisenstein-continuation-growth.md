+++
kind  = "theorem"
title = "Meromorphic continuation of Siegel Eisenstein series"
provenance = "modified"
source = "special case of Langlands [langlands-1976]; Bernstein–Lapid [bernstein-lapid-2019]; see Piatetski-Shapiro–Rallis [piatetski-shapiro-rallis-1987]; Tan [tan-1999]"
lean  = ["GlobalTheory.ThK.Dbl.EisBL", "PositivityTheory.RgEis.Hd.eisBL",
         "GlobalTheory.Published.SiegelEisensteinContinuation", "PositivityTheory.RgEis.Sp.Hd.siegelEisensteinContinuation"]
order = 9
+++
Let $E/F$ be a CM extension and $Y$ a hermitian or skew-hermitian space
over $E$ with a good integral structure. For a Hecke character $\chi$ and a
holomorphic section $f$ of the degenerate principal series of the Siegel
parabolic subgroup:

* the Eisenstein series $\hat E(s, x) = \sum_\gamma f_s(\gamma x)$
  converges for $\Re s > t$ and is holomorphic there;
* near every $s_0$ there is $k$ such that $(s - s_0)^k\hat E(s, \cdot)$ is a
  holomorphic family of functions of moderate growth, holomorphic after
  pairing with every continuous functional on the space of such functions.

In the doubling setting: let $V$ be a hermitian space of positive rank over
a CM field, $V \oplus (-V)$ its doubled space and $P$ the Siegel parabolic
subgroup of $\U(V\oplus(-V))$. For a unitary Hecke character $\mu$ and a
section $\varphi$ of the degenerate principal series induced from
$\mu|\det|^{s_1}$, the Eisenstein series $E(g, s)$ of the flat section
through $\varphi$ continues meromorphically in $s$, and at each $s_0$ some
power $(s - s_0)^k E(g, s)$ is regular.

This is the meromorphic continuation of Eisenstein series, for Siegel
parabolic subgroups; the first form, with control of growth, is that of
Bernstein and Lapid.
