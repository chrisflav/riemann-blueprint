+++
kind  = "lemma"
title = "The constant term of a theta integral on the big cone"
provenance = "modified"
source = "after Rallis [rallis-1984]"
lean  = ["GlobalTheory.T.exists_isCT_integral_eq_cone_integral_add_hasLaw", "GlobalTheory.ThK.unfoldCTBigCone"]
order = 1
+++
Let $E/F$ be a CM extension and consider a theta tower step from
$\U(W_1)$, $\dim W_1 = b$, to $\U(W)$, $\dim W = b + 2$, with an isotropic plane
$H \subset W$ and a Levi decomposition of its stabiliser. Fix a compact open
stabiliser $K$ and Haar measures. Then there is $C \ne 0$ such that for
every triple of representations related by theta lifts and every
polynomial Schwartz function $\Phi$ there is a function $A_0$ on $\U(W)$
transforming with exponent $(b+2)/2$ under the Levi factor such that the
constant term along $H$ of the theta integral of $\Phi$ is
$$I_W(\Phi)_H(h) = C\, I_{W_1}\big(\kappa(\omega(1,h)\Phi)\big) + A_0(h),$$
where $\kappa$ is the partial Fourier transform along the cone (with shift
$(b + 2 - a')/2$).

This is the constant-term part of Rallis' tower property.
