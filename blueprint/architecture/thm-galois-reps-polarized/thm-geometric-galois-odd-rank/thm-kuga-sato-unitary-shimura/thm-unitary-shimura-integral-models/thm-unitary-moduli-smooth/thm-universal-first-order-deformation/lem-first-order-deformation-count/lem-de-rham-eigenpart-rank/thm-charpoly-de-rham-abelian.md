+++
kind  = "theorem"
title = "Characteristic polynomials on de Rham homology"
lean  = ["GlobalTheory.DeRham.charpoly_push_eq", "GlobalTheory.DeRham.charpoly_push_eq_map_charpoly",
         "GlobalTheory.DeRhamCharpolyP.charpoly_push",
         "GlobalTheory.T.charpoly_deRhamHomology_abelianVariety_charP",
         "GlobalTheory.T.charpoly_deRhamHomology_endomorphism_eq_map_ladic"]
order = 10
+++
Let $A$ be an abelian variety over an algebraically closed field $k$, $f$ an
endomorphism, and $l$ a prime invertible in $k$. Let $L$ be a free $\Z$-module of
finite rank with an endomorphism $\varphi$ and compatible surjections
$L \to A[l^j]$ with kernel $l^jL$ that carry $\varphi$ to $f$. Then the characteristic
polynomial of $f$ on $H^{\mathrm{dR}}_1(A)$ is the image in $k[X]$ of the characteristic
polynomial of $\varphi$. This holds in every characteristic; it is the classical
fact that the characteristic polynomial of an endomorphism has integer
coefficients independent of the cohomology used (Weil; Mumford, *Abelian
varieties*, §19; Katz–Messing in characteristic $p$).
