+++
kind  = "theorem"
title = "Primes in progressions with an exceptional zero"
provenance = "modified"
source = "after Linnik [linnik-1944] and Gallagher [gallagher-1970]"
lean  = ["Formalism.HermitianLattices.Ext.PrimesInProgressions.pnt_progressions_relative_weak_holds",
         "Formalism.HermitianLattices.Ext.PrimesInProgressions.deuring_heilbronn_finish_turan"]
order = 6
+++
There are constants $c, A, C > 0$ with the following property. Let $M$ be
divisible by $8$. A real character $\chi_1 \ne 1$ modulo $M$ with a zero
$\beta_1$ of $L(s,\chi_1)$ in $1 - 1/(8\log M) < \beta_1 < 1$ is called
exceptional. One can choose either an exceptional pair $(\chi_1, \beta_1)$,
or none when there is no exceptional pair, such that, with
$$\mathrm{main}(X; b) = \frac{\mathrm{li}(X) - \chi_1(b)\,\mathrm{li}(X^{\beta_1})}{\varphi(M)}$$
(the second term omitted when no pair is chosen), for
$b$ prime to $M$ and $\log X \ge C\log M\,\log(\log M + 2)$,
$$\big|\pi(X; M, b) - \mathrm{main}(X; b)\big| \le
A\Big(e^{-c\log X/\log M} + e^{-\sqrt{c\log X}}\Big)\,\mathrm{main}(X; b).$$

This is the prime number theorem in arithmetic progressions in Linnik's
range, with the exceptional zero kept in the main term. The range
$\log X \ge C\log M\log\log M$ is a little narrower than $X \ge M^C$.
