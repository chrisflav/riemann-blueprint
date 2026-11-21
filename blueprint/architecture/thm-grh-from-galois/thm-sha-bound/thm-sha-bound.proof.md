+++
kind = "proof"
of   = "thm-sha-bound"
uses = ["thm-base-change-unitary"]
+++
Split the bound into two parts. We read them as the eigenspaces of complex
conjugation; the statements do not say so.

The first part grows polynomially in $t$. It comes from the growth of
Tate–Shafarevich groups in the layers of the cyclotomic
$\Z_l$-extension, where the theorem of Ferrero and Washington applies.

The second part is at most $(\mathrm{cond}\cdot t)^C + C\exp(x^{4\varepsilon/5})$.
It comes from bounds on the $\psi$-isotypic Selmer groups of
$\psi \otimes \Z_l(e)$, in five cases according to $l$, $e$ and the order of
$\psi$:

* one case from Kato's Euler system: the Bloch–Kato Selmer group of a
  newform of weight $2e+1$ vanishes;
* two cases from automorphy of Galois representations with values in
  $\mathrm{GSp}_4$;
* one case from an $R = T$ theorem for 3-dimensional representations over
  an imaginary quadratic field, which needs base change from unitary
  groups ([thm-base-change-unitary]);
* components with trivial character vanish.

A bound $\log|H^2(\Z_l(e+1))| \le \exp((2e[L:\Q])^C\log 2D_L)$ controls the
rest.

*We read* the vanishing of the trivial components as the "significant
weakening of Vandiver's conjecture" in the announcement.
