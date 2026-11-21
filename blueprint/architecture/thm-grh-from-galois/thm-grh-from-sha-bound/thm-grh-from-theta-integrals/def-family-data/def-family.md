+++
kind  = "definition"
title = "Families"
provenance = "new"
lean  = ["Formalism.MainNotions.FamCore", "Formalism.MainNotions.FamP",
         "Formalism.MainNotions.FamClass"]
uses  = ["def-family-member", "def-family-scale"]
order = 7
+++
Fix $0 < \varepsilon < 1/52$. A *family* consists of a threshold $x_1 > 1$, an
unbounded set $\mathcal W$ of scales, and for every $x$ a finite index set
$I(x)$, non-empty for $x \in \mathcal W$, with a member $D(x, i)$
([def-family-member]) and size data at the scale $(x, \varepsilon, J)$
([def-family-scale]) for each $i \in I(x)$, such that:

* for fixed $x$ all members share the rank data, the primes $q, d$, the
  integer $Q$, the Artin map, the root discriminant, the level primes
  $g_0, g_1, p, p'$, the top and thick sets, and their words; $J$ and several
  constants are the same for all $x$;
* the order of $\psi$ and $Q/n$ stay bounded;
* the members *cover the weights*: for every base element of $A$ and every
  choice of integers $a_\tau, b_\tau$ in the windows of [def-family-scale],
  some member $D(x, i)$ has exactly these weights;
* for $x > x_1$ each member carries a choice of further parameters whose
  constants are the same for the whole family, the divisibility and
  comparison data of the slope argument, and a set of dropped primes,
  which are exactly the primes other than the $T_u$ that give no gain.

A *class of families* is a property of families. The family hypotheses
([def-family-data]) are conditions on a class.
