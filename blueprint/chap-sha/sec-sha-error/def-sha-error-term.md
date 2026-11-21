+++
kind  = "definition"
title = "The Tate–Shafarevich error term"
provenance = "new"
lean  = ["Formalism.MainNotions.LinkN"]
order = 1
+++
A family satisfies the *Tate–Shafarevich error bound* if eventually, for
every member whose odd Tate–Shafarevich groups are finite,
$$\eta_j \le d_j\Big(C\big(f m b L^2 + N\log^2 x\big) + \sum_l \log l\sum_{e<t}\mathrm{len}\,Ш^1_l(E, e)\Big),$$
where $\eta_j$ is the error of the $j$-th [member](@def-family-member) and $f, m, b, L, N$ are the
[size parameters](@def-family-scale) of the family. This is the only place where the
Tate–Shafarevich bound enters the estimates for families.
