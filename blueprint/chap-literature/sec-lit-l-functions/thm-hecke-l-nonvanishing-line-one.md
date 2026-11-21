+++
kind  = "theorem"
title = "Partial Hecke L-functions do not vanish on Re s >= 1"
provenance = "published"
source = "Hecke [hecke-1920]; Landau [landau-1918]"
lean  = ["GlobalTheory.Published.HeckeLPartialContinuation", "PositivityTheory.Stage1.PM.heckeLPartialContinuation"]
order = 4
+++
Let $K$ be a number field and $T$ a finite set of finite places.

* For a unitary Hecke character $\chi$ not of the form $|\cdot|^{it}$, the
  partial $L$-function $L^T(s, \chi)$, with the Euler factors at $T$
  removed, extends to an entire function that does not vanish on
  $\Re s \ge 1$.
* The function $(s-1)\,\zeta_K^T(s)$ extends to an entire function that does
  not vanish on $\Re s \ge 1$.

This is the non-vanishing of Hecke $L$-functions on the line $\Re s = 1$,
the input to the prime ideal theorem in arithmetic
progressions.
