+++
kind = "proof"
of   = "thm-siegel-weil-definite"
uses = ["thm-eisenstein-continuation-growth", "thm-hasse-norm-quadratic", "thm-landherr-cm", "thm-reduction-theory-unitary"]
+++
First, the constant term of every Siegel Eisenstein series along a maximal
parabolic splits: for $\Re z$ large it is an Eisenstein series on the Levi
factor of smaller rank, plus a term $c_2$ that transforms under the dilations
$y_\tau$ of the parabolic by $c_2(y_\tau x) = e^{\tau(n - 2z)}c_2(x)$; this is
proved directly. Second, Poisson summation for the twisted Weil
representation follows from the classical Poisson summation formula on the
adelic Schwartz space. Then argue by induction on $n$: Poisson summation
computes the constant terms of the theta integral, and the splitting computes
those of the Eisenstein series; they agree by induction. The difference of
the two sides is then a cusp form orthogonal to all cusp forms, hence zero.
The bound on Eisenstein series ([thm-eisenstein-continuation-growth]),
reduction theory on Siegel sets ([thm-reduction-theory-unitary]) and the norm
theorems of Hasse and Landherr ([thm-hasse-norm-quadratic],
[thm-landherr-cm]) give convergence and the local factors.
