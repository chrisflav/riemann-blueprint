+++
kind  = "theorem"
title = "The l-adic character of an algebraic Hecke character"
lean  = ["GlobalTheory.Published.HeckeLAdicCharacter", "PositivityTheory.Stage1.PM.heckeLAdicCharacter"]
order = 1
+++
Let $\chi$ be an algebraic Hecke character of $E$ of type $n$. There is a
unique continuous character $r_{\chi,\iota} : \Gal(\bar E/E) \to \Qlbar^\times$
such that
$$ r_{\chi,\iota}(\sigma) = \iota^{-1}\Big(\chi(x)\prod_\phi \phi(x_\infty)^{-n_\phi}\Big)\cdot \prod_{\phi}\iota^{-1}\phi(x_l)^{n_\phi} $$
whenever $\mathrm{Art}_E(x)$ is the image of $\sigma$ in
$\Gal(\bar E/E)^{\mathrm{ab}}$; here $x_\infty$ and $x_l$ are the components
of the idele $x$ at the infinite places and at the places above $l$.

This is the construction of Weil (1955) and Serre (1968).
