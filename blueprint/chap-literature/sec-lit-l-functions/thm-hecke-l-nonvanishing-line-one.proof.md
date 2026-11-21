+++
kind = "proof"
of   = "thm-hecke-l-nonvanishing-line-one"
uses = ["thm-hecke-l-entire"]
+++
Remove the finitely many Euler factors from the entire function of
[thm-hecke-l-entire]; they are entire and do not vanish on
$\Re s > 0$. For $\Re s > 1$ the Euler product does not vanish. At
$s = 1 + it$ we have $L(1 + it, \chi) = L(1, \chi|\cdot|^{it})$, and
$\chi|\cdot|^{it} \ne 1$, so the second part of
[thm-hecke-l-entire] applies; the same argument with
$\chi = 1$ and $t \ne 0$, together with the pole of $\zeta_K$ at $s = 1$,
gives the statement for $\zeta_K^T$.
