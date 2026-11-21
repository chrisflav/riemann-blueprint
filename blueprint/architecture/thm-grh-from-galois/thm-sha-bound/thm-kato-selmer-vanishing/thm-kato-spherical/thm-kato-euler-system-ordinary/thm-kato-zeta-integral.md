+++
kind  = "theorem"
title = "Kato's zeta classes are integral and norm-compatible"
lean  = ["UpperTheory.Kd.K4.kato_eulerSystem_integrality", "UpperTheory.Kd.K4.top",
         "UpperTheory.V.Z.Kato.Joint.KatoEulerSystemIwasawaClassStatement"]
order = 10
+++
Let $l$, $e$, $W$ and $g$ be as in [thm-kato-euler-system-ordinary]. Let $\mathcal F$ be the field of
modular functions of all levels over $\Qbar$, with its $q$-expansions, the
action of $\GL_2^+(\Q)$ and Shimura's reciprocity law. Fix a level
$N$ prime to $l$, coefficients $c_x$ on $\Z/N$ not all zero, integers $c, d$
for the Siegel units, and elements of $\Gamma_1(N)$ indexed by $(\Z/l)^\times$,
satisfying the admissibility conditions attached to $g$.

Then there are $m \ge 0$ and cocycles $Y_r$ on $G_\Q$, $r \ge 0$, with values
in $W \otimes \mathcal O[(\Z/l^r)^\times]$ and twisted by $\epsilon^{-1}$
modulo $l^r$, such that:

* $Y_r$ is the image of $Y_{r+1}$ (norm compatibility), each $Y_r$ is
  continuous and integral;
* the specialisation of $Y_r$ at $u \mapsto u^{-e}\chi(u)$ is congruent to a
  class $y$ modulo $l^r$;
* $l^m y$ is the bottom class of an Euler system for $W$ as in [thm-kato-euler-system-ordinary], and
  the $Y_r$ form compatible Iwasawa data for it.

*We read* $Y_r$ as Kato's zeta elements, built from products of Siegel
units, over the layers $\Q(\mu_{l^r})$.
