+++
id    = "thm-arithmetic-hilbert-samuel-inequalities"
kind  = "theorem"
title = "Arithmetic Hilbert–Samuel inequalities and Moriwaki's theorem"
lean  = ["PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsChain"]
order = 10
+++
Let $X$ be an arithmetic variety of dimension $D + 1$ and $\bar L$ a hermitian
line bundle on $X$, semipositive, nef on the fibres and invariant under
complex conjugation. Then:

* (Moriwaki) $\bar L^{D+1} \le \widehat{\mathrm{vol}}(\bar L)$, for $D \ge 1$ and
  for arithmetic curves;
* (arithmetic Kleiman) if $\bar L$ has non-negative degree on every
  arithmetic curve in $X$, then $\bar L^{D+1} \ge 0$;
* (arithmetic Hilbert–Samuel, upper bound) the number of small sections
  satisfies
  $$\limsup_{n \to \infty} \frac{\log \#\{s \in H^0(X, L^n) : \|s\|_{\sup} \le 1\}}{n^{D+1}/(D+1)!} \le \bar L^{D+1},$$
  with equality and a limit when the small sections generate.

These are theorems of Gillet–Soulé, Zhang and Moriwaki (2000–2009).
