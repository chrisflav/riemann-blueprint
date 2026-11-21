+++
kind  = "theorem"
title = "Hecke L-functions are entire and do not vanish at s = 1"
provenance = "published"
source = "Hecke [hecke-1918], [hecke-1920]; Landau [landau-1918]"
lean  = ["GlobalTheory.Published.HeckeLEntireAndNonzeroAtOne", "PositivityTheory.Stage1.PM.heckeLEntireAndNonzeroAtOne"]
order = 6
+++
Let $K$ be a number field and $\chi$ a unitary Hecke character of $K$.

* If $\chi$ is not of the form $|\cdot|^{it}$ for a real $t$, the Euler
  product $L(s, \chi)$, convergent for $\Re s > 1$, extends to an entire
  function.
* If $\chi \ne 1$, the Euler product extends analytically to a
  neighbourhood of $s = 1$ and $L(1, \chi) \ne 0$.
