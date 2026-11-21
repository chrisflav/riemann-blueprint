+++
id    = "thm-eigenspaces-crystalline"
kind  = "theorem"
title = "Eigenspaces with good reduction are crystalline"
provenance = "new"
lean  = ["GlobalTheory.GalV.VFin", "UpperTheory.Gal.G3.vFin_holds", "UpperTheory.Gal.Int.Geo.CrysStep",
         "UpperTheory.Gal.Seam.MatIn", "UpperTheory.Gal.Seam.crysStep_holds", "UpperTheory.Gal.Seam.crysStep_of",
         "UpperTheory.Gal.Seam.matIn_holds"]
order = 12
+++
Let $Z$ with its correspondences be a Hecke tower over a number field $E$
([thm-galois-reps-hecke-eigenspaces]), $\theta$ a system of eigenvalues and $\rho$ a subquotient of the
eigenspace $V_\theta$. Let $w \mid l$, and suppose that over $E_w$ the variety $Z$
is a finite étale Galois cover of the generic fibre of a smooth projective
$\mathcal O_w$-scheme $Y$, whose deck transformations are Hecke
correspondences with eigenvalue $1$. Then $\rho|_{G_{E_w}}$ is crystalline.

On the way: for $X$ proper over an algebraically closed field in which $l$ is
invertible, $H^n(X, \Z_l(i))$ is a finitely generated $\Z_l$-module and
$H^n(X, \Q_l(i))$ is finite-dimensional.
