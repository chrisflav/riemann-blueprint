+++
id    = "thm-galois-reps-hecke-eigenspaces"
kind  = "theorem"
title = "Galois representations on Hecke eigenspaces"
provenance = "new"
lean  = ["UpperTheory.Gal.Int.Geo.steps_holds"]
uses  = ["thm-eigenspaces-crystalline", "thm-hodge-tate-weights-eigenspaces"]
order = 1
+++
A *Hecke tower* over a field $k$ is a smooth projective $k$-variety $Z$ with
correspondences $Z \xleftarrow{s_g} Y_g \xrightarrow{t_g} Z$, $g \in \Gamma$, with
$s_g$ finite étale. Each correspondence acts on $H^*(Z_{\bar k}, \Q_l)$; for a
system of eigenvalues $\theta : \Gamma \to \Qlbar$ let $V_\theta$ be the common
eigenspace. Let $k = E$ be a number field.

1. $V_\theta$ has a continuous semisimple subquotient $\rho$ of $G_E$, and every
   graded piece of a $G_E$-stable filtration of $V_\theta$ qualifies.
2. If at $w \nmid l$ the tower has good reduction and the reduction satisfies a
   congruence relation: Frobenius is a root of a Hecke polynomial of degree $n$
   whose coefficients $\vartheta_i$ satisfy $\theta(\gamma_i) = m_i\vartheta_i$ for
   Hecke correspondences $\gamma_i$, then $\rho$ is unramified at $w$ and
   $\rho(\mathrm{Frob}_w)$ is killed by the polynomial with the roots of that
   Hecke polynomial.
3. At $w \mid l$, $\rho$ is crystalline when the tower has a good model
   ([thm-eigenspaces-crystalline]), its Hodge–Tate weights include the Hodge numbers seen
   by $\theta$ ([thm-hodge-tate-weights-eigenspaces]), and under the congruence relation the
   crystalline Frobenius is killed by a power of the Hecke polynomial.
4. Twisting $\rho$ by the $l$-adic character of an algebraic Hecke character
   multiplies the Frobenius eigenvalues by its values and shifts the
   Hodge–Tate weights by its infinity type, keeping the crystalline property.
