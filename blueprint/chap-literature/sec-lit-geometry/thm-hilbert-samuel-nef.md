+++
kind  = "theorem"
title = "Hilbert–Samuel asymptotics for nef multidegrees"
provenance = "modified"
source = "after the asymptotic Riemann–Roch theorem; see Lazarsfeld [lazarsfeld-2004]"
lean  = ["GlobalTheory.CompanionTheory.Ar.Pub.NefRR", "PositivityTheory.Tls2.Nef.nefRR"]
order = 13
+++
Let $X \subset \prod_k \mathbb P^{n_k}_\Z$ be a flat integral closed
subscheme of relative dimension $D$ over $\Z$, given by a generic point $y$
that generates its function field, and let $a = (a_k)$ be a multidegree
whose line bundle $\mathcal O(a)$ has non-negative degree on every curve in
the generic fibre. Let $V_\tau$ be the $\Q$-span of the rational functions
that are integral over every standard affine chart after multiplication by
the chart's $y^{-\tau a}$; these are the sections of $\mathcal O(\tau a)$
on the normalisation of $X_\Q$. Then each $V_\tau$ is finite-dimensional and
$$ \dim_\Q V_\tau = \deg_{\mathcal O(a)}(X_\Q)\,\frac{\tau^D}{D!} + o(\tau^D). $$

This is the asymptotic Riemann–Roch (Hilbert–Samuel) theorem for nef line
bundles, stated in the multiprojective setting.
