+++
id    = "lem-hilbert-samuel-block"
kind  = "lemma"
title = "Arithmetic Hilbert–Samuel for a block of coordinates"
lean  = ["PositivityTheory.LocalParametersCuspidal.MB.HSM.theoremHSMBlock"]
uses  = ["thm-arithmetic-intersection-theory"]
order = 10
+++
Assume the existence of an arithmetic intersection theory and resolution in
projective space ([thm-arithmetic-intersection-theory]). Let $X$ be an arithmetic variety of dimension
$D + 1$ embedded by a block of multihomogeneous coordinates, with a hermitian
line bundle $\bar A$. Then the arithmetic Euler characteristic of $A^n$
differs from $\bar A^{D+1} n^{D+1}/(D+1)!$ by $o(n^{D+1})$, and there is $C$
with
$$\frac{|f(z)|}{h_A(z)^n} \le C\, n^{D/2}\, \|f\|_{L^2}$$
for every section $f$ of degree $n$ and every point $z$ (Gromov's inequality).
