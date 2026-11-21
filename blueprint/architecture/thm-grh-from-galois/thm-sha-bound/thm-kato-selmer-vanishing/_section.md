+++
id    = "thm-kato-selmer-vanishing"
kind  = "theorem"
title = "Vanishing of Selmer groups from Kato's Euler system"
provenance = "new"
lean  = ["UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH",
         "UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH_of_rT_of_quadBC2"]
order = 11
+++
Let $l$ be an odd prime, $\epsilon$
the $l$-adic cyclotomic character, $e \ge 1$ with $l - 1 \nmid 2e$, and $K$ an
imaginary quadratic field with quadratic character $\theta$ and
$l \nmid D_K h_K$. Let $N$ be even and prime to $D_K$, $\psi$ a character of
order prime to $l$ that factors through $\Q(\mu_N)$ and has square $1$ on
inertia at $l$, and $W : G_\Q \to \GL_2(\Qlbar)$ a representation such that:

* $\det W = \theta$, $W$ has level $N|D_K|$ and is ordinary at $l$ with
  weights $(e, -e)$, upper triangular on a decomposition group at $l$;
* on inertia at $l$, $\operatorname{tr} W = \epsilon^e\psi + (\epsilon^e\psi)^{-1}$;
* $\operatorname{tr} W \equiv \theta\epsilon^e\psi + (\epsilon^e\psi)^{-1}$
  modulo the maximal ideal, while $W$ stays irreducible on $G_{K(\mu_{l^\infty})}$;
* complex conjugation $c$ satisfies $\epsilon(c)^e\psi(c) = 1$.

Suppose $W \otimes \epsilon^{-e}$ is attached to a newform of weight $2e+1$,
and that $W$ is automorphic over every imaginary quadratic field on which it
stays irreducible. Then the Bloch–Kato Selmer groups of $W$ and of
$W \otimes \theta$ vanish.
