+++
kind  = "theorem"
title = "Transfer to unitary Shimura varieties"
lean  = ["UpperTheory.Gal.Int.Geo.Pl.planEx_holds", "UpperTheory.Gal.Int.Geo.PlanEx"]
order = 12
+++
In the situation of [geo-one-holds], with $U$ an automorphic representation of
the definite group $\U_a$, $a$ odd, there are: a unitary group $G$ of signature
$(1, a-1)$ at one infinite place and $(0, a)$ at the others, of the kind of
[kodaira-spencer-of-weight-one], identified with the same CM field; a level; an
algebraic Hecke character $\kappa$ of $E$ with infinity type $m$; a dominant weight
$\lambda$; and a Hecke eigensystem $\theta$ occurring in automorphic forms of weight
$\lambda$ on $G$, such that

* at all but finitely many admissible places $w \nmid l$, the eigenvalues of
  $\theta$ on the Hecke operators $T_0, \dots, T_a$ at $w$ give the Satake parameters of
  $U_w$ divided by $\kappa(\varpi_w)$;
* at $v'$, $\kappa$ is unramified, the level is good, and the numbers $k - \lambda_k$
  of the weights of $U$, shifted by $m$, are Hodge exponents of $\lambda$.

There are variants that add a prescribed place $w$, either admissible with
$w \nmid l$ or above $l$, to these conditions.
