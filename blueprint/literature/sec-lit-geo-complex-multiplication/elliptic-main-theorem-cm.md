+++
kind  = "theorem"
title = "Shimura's main theorem of complex multiplication"
lean  = ["GlobalTheory.Published.EllipticMainTheoremCM", "PositivityTheory.Prw.ellipticMainTheoremCM_holds"]
order = 3
+++
Let $K \subset \C$ be an imaginary quadratic field with Artin map
$\mathrm{Art}_K$. Let $\sigma \in \mathrm{Aut}(\C/K)$ and let $s$ be an idele
with $\mathrm{Art}_K(s) = \sigma|_{K^{\mathrm{ab}}}$; write $t$ for its finite
part. Let $X$ be an elliptic curve over $\C$ and
$\xi : \C/\mathfrak a \cong X(\C)$ an analytic isomorphism for a fractional
ideal $\mathfrak a$. Then there is a unique analytic isomorphism
$\xi' : \C/t^{-1}\mathfrak a \cong X^\sigma(\C)$ such that
$$ \sigma\big(\xi(x)\big) = \xi'(t^{-1}x) \qquad \text{for all } x \in K/\mathfrak a. $$

This is the main theorem of complex multiplication (Shimura 1971) for
elliptic curves with complex multiplication by $\mathcal O_K$.
