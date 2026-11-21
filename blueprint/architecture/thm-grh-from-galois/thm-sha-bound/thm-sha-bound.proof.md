+++
kind = "proof"
of   = "thm-sha-bound"
uses = ["thm-base-change-unitary", "thm-hilbert-modular-inputs", "thm-sha-bound-from-hilbert-inputs"]
+++
The Galois representations, with weak descent, give the standard inputs
for Hilbert modular forms ([thm-hilbert-modular-inputs]). Weak descent is
proved elsewhere by a trace formula. From these inputs,
[thm-sha-bound-from-hilbert-inputs] proves the bound as follows.

Split the bound into two parts. We read them as the eigenspaces of complex
conjugation; the statements do not say so.

The *first part* grows polynomially in $t$. It comes from a bound
$\log|H^2(\Z_l(e+1))| \le \exp((2e[L:\Q])^C\log 2D_L)$, the growth of
Tate–Shafarevich groups in the layers of the cyclotomic $\Z_l$-extension
(where the theorem of Ferrero and Washington applies), and unramified
orthogonality.

The *second part* is at most $(\mathrm{cond}\cdot t)^C + C\exp(x^{4\varepsilon/5})$.
It comes from bounds on the $\psi$-isotypic Selmer groups of
$\psi \otimes \Z_l(e)$, which also use the bound on $H^2$. There are four
cases:

* For $l$ outside an exceptional set and $l - 1 \nmid 2e$, Kato's Euler
  system: the Bloch–Kato Selmer group of a newform of weight $2e+1$
  vanishes. This needs automorphy of 2-dimensional representations over
  imaginary quadratic fields. Kato's Euler system and his explicit
  reciprocity law are proved here, not assumed.
* Two cases from automorphy of Galois representations with values in
  $\mathrm{GSp}_4$.
* For $l$ in the exceptional set and $e = 1$, an $R = T$ theorem for
  3-dimensional representations over an imaginary quadratic field. It
  needs base change from unitary groups ([thm-base-change-unitary]).
* For $l \ge 5$, $e$ even and $l - 1 \mid 2e$, the components with trivial
  character vanish.

*We read* the vanishing of the trivial components as the "significant
weakening of Vandiver's conjecture" in the announcement.
