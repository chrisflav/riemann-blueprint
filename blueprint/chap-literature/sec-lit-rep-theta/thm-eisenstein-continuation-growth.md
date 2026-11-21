+++
kind  = "theorem"
title = "Meromorphic continuation of Siegel Eisenstein series with growth"
provenance = "modified"
source = "special case of Langlands [langlands-1976]; Bernstein–Lapid [bernstein-lapid-2019]"
lean  = ["GlobalTheory.ThK.Dbl.EisBL", "PositivityTheory.RgEis.Hd.eisBL"]
order = 8
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

This is the meromorphic continuation of Eisenstein series, for Siegel
parabolic subgroups, in the form of Bernstein and Lapid with control of
growth.
