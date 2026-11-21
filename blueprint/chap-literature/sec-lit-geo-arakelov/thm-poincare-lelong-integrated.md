+++
kind  = "theorem"
title = "Integrated Poincaré–Lelong formula"
source = "after Bost–Gillet–Soulé [bost-1994]"
lean  = ["GlobalTheory.CompanionTheory.Hypotheses₂.PoincareLelongInv", "PositivityTheory.Tls2.Pl.poincareLelongInv"]
order = 3
+++
Let $X$ be an arithmetic variety of dimension $n + 2$ in multiprojective
space, $\bar L_1, \dots, \bar L_n$, $\bar A$, $\bar B$ smooth hermitian line
bundles invariant under complex conjugation, with $B$ of degree zero (so its
metric is a positive function $h_B$), and $s$ a section of $A$. Write
$\omega = c_1(\bar L_1) \wedge \dots \wedge c_1(\bar L_n)$ for the product of
curvature forms. Then
$$ \int_{X(\C)} \log\|s\|_A \; dd^c \log h_B \wedge \omega = \sum_{W} m_W \int_{W(\C)} \log h_B\; \omega \;-\; \int_{X(\C)} \log h_B \; dd^c\log h_A \wedge \omega, $$
where $W$ runs over the horizontal components of the divisor of $s$, with
multiplicities $m_W$.

This is the Poincaré–Lelong formula $dd^c \log\|s\|^2 = \delta_{\mathrm{div}\,s} - c_1(\bar A)$,
integrated against $\log h_B \cdot \omega$, as in the inductive definition
of heights. The normalisation of $dd^c$ is the
one fixed by the formula.
