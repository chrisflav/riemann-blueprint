+++
id    = "thm-kato-spherical"
kind  = "theorem"
title = "Kato's theorem for representations spherical at l"
lean  = ["UpperTheory.V.Z.Kato.WeilSphericalRecords.twoS"]
uses  = ["def-galois-cohomology-inputs"]
order = 10
+++
Assume the published results on Galois cohomology ([def-galois-cohomology-inputs]) and the
following: whenever $W : G_\Q \to \GL_2(\Qlbar)$, $l$ odd, is continuous,
odd, irreducible on the kernel of $\epsilon$ and $\det W$, with $\det W$
quadratic, ordinary at $l$ with weights $(e, -e)$, of level prime to $l$
after a twist, attached after a twist to a newform of weight $2e+1$, and
*spherical at $l$* (every cuspidal representation of $\GL_2(\A_\Q)$
attached to a twist of $W$ unramified at $l$ is unramified at $l$), then a
twist of $W \otimes \epsilon^{-e}\det W^{-1}$ by a character of order $l$ is
attached to an $l$-ordinary newform of weight $2e+1$ and level prime to $l$.

Then the conclusion of [thm-kato-selmer-vanishing] holds for every $W$ as there
that is spherical at $l$: the Bloch–Kato Selmer groups of $W$ and
$W \otimes \theta$ vanish.
