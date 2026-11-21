+++
kind  = "theorem"
title = "The logarithmic derivative of a Dirichlet L-function at s = 1"
source = "classical; see Davenport [davenport-2000]"
lean  = ["GlobalTheory.LogDerOneProof.logDerOne_holds", "GlobalTheory.Mem.An.LogDerOne"]
order = 5
+++
There is a constant $C$ such that for every primitive Dirichlet character
$\chi$ of conductor $q > 1$,
$$
\left|\frac{L'}{L}(1, \chi) - \sum_{\rho} \frac{1}{1 - \rho}\right| \le C\log(3q),
$$
where $\rho$ runs over the non-trivial zeros of $L(s, \chi)$ with
$|\Im\rho| \le 1$, counted with multiplicity. It is a consequence of the
Hadamard product and the zero count in a unit window.
