+++
kind  = "definition"
title = "Ranks of a family"
provenance = "new"
lean  = ["Formalism.BasicNotions.Ranks", "Formalism.BasicNotions.Ranks.N",
         "Formalism.BasicNotions.Ranks.r", "Formalism.BasicNotions.Ranks.nV",
         "Formalism.BasicNotions.Ranks.f", "Formalism.BasicNotions.Ranks.n"]
uses  = ["def-auxiliary-field-data"]
order = 2
+++
*Rank data* consist of the group data $(e, A, h, a_0)$ of
[def-auxiliary-field-data], with $n = |A|$ and $f = 2n$ (the size of the CM
type), and integers $k, m, t$ with
$$k, m \text{ even},\quad t \text{ odd},\quad 2 \le m,\quad m + 3 \le k,\quad m \le f \le k,$$
$$k + m + 4 \le t,\quad 3m < t,\quad m^2 \le k + m(t+1).$$
They determine
$$r = k + m - 1, \qquad n_V = r + t, \qquad N(j) = k + j(t+1) \quad (0 \le j \le m).$$
The definite unitary groups of a family have ranks $N(j)$; the other
hermitian spaces of [def-family-hermitian-spaces] have ranks $r + jt$,
$r$ and $n_V$, and signatures $(k + j - 1, m - j)$ and
$(k + m/2 - 1, m/2)$ at every infinite place. The integer $t$ is also the
number of Tate twists in the Tate–Shafarevich bound ([def-sha-bound]).
