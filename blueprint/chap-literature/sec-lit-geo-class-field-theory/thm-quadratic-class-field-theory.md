+++
kind  = "theorem"
title = "Class field theory of quadratic extensions"
provenance = "published"
source = "classical; see Cassels–Fröhlich [cassels-frohlich-1967]"
lean  = ["GlobalTheory.Published.QuadraticClassFieldTheory", "PositivityTheory.Stage1.PM.quadraticClassFieldTheory"]
order = 7
+++
Let $L/K$ be a quadratic extension of number fields. For a completion $K_v$
let $\eta_v : K_v^\times \to \{\pm1\}$ send $x$ to $1$ exactly when $x$ is a
norm from $L \otimes_K K_v$. Then:

* each $\eta_v$ is a character;
* (norm theorem) $t \in K^\times$ is a norm from $L$ if and only if it is a
  local norm at every place;
* (product formula) for $t \in K^\times$, $\eta_v(t) = 1$ for almost all $v$
  and $\prod_v \eta_v(t) = 1$;
* (exact sequence) a family $(x_v)$ of local elements, almost all local norms,
  is a global element times a family of local norms if and only if
  $\prod_v \eta_v(x_v) = 1$, and some family has product $-1$.

Moreover the characters are compatible with base change: if $F \subset K$
and $L = KE$ for a quadratic extension $E/F$, then
$\eta_{L/K}(x) = \eta_{E/F}(N x)$ for $x$ in any finite extension of a
completion of $F$.

These are the results of Hilbert and Hasse on the quadratic norm residue
symbol, equivalent to quadratic class field theory.
