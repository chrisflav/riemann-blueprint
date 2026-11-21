+++
kind  = "definition"
title = "The weighted Chebyshev function"
lean  = ["Formalism.Gz", "Formalism.HC.Level.Gm", "Formalism.HC.Level.cyc"]
order = 1
+++
Let $\psi$ be a primitive character and $o$ the order of the group
$\langle\psi\rangle$ it generates. Put
$$G_z(y) = \sum_{n \le y}\Lambda(n)\Big(\frac yn - 1\Big) - y\log y + (1+\gamma)y,$$
$$g_\chi(y) = \sum_{n \le y}\Lambda(n)\chi(n)\Big(\frac yn - 1\Big) + y\,\frac{L'}{L}(1,\chi),$$
where $\chi$ runs over the primitive characters inducing the elements of
$\langle\psi\rangle$, and
$$G_m(y) = G_z(y) + \frac{1}{3o+1}\sum_{\chi \ne 1}\Re\, g_\chi(y).$$

Each function is a von Mangoldt sum with weight $(y/n - 1)_+$ and its main
terms removed. The Mellin transform of the weight is $y^s/(s(s-1))$, so
$G_m$ is the function of the explicit formula of Guinand and Weil. The
weight $1/(3o+1)$ makes the Dirichlet coefficients of the combination
non-negative.
