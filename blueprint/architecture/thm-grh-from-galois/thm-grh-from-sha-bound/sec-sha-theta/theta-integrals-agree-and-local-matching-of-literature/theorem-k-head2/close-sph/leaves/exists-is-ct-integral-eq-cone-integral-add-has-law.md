+++
kind  = "lemma"
title = "The constant term of a theta integral on the big cone"
lean  = ["GlobalTheory.T.exists_isCT_integral_eq_cone_integral_add_hasLaw", "GlobalTheory.ThK.unfoldCTBigCone"]
uses  = ["bernstein-unitary-product-irreducible", "bernstein-zelevinsky-finiteness", "borel-casselman", "casselman-wallach", "complex-multiplication-j-st", "cusp-bounded", "cusp-decay-bound", "cusp-decay-sobolev", "cusp-rapid-decay", "cusp-trace-class", "cuspidal-mirabolic", "cuspidal-spectrum-gl", "discrete-series-cover", "discrete-series-cover-exists", "discrete-series-exists", "discrete-series-hermitian-unique", "discrete-series-lowest-k-type", "discrete-series-upq-exists", "dixmier-malliavin-factorisation", "flath-factorisation", "formal-degree-compact-dual", "geometric-lemma-filtration", "gk-globalisation", "gl-howe-duality", "green-cuspidal", "harish-chandra-finite", "harish-chandra-modules", "hecke-l-entire-and-nonzero-at-one", "hecke-l-partial-continuation", "hecke-tate-functional-equation", "hermitian-hasse-principle", "hermitian-local-global", "holomorphic-discrete-series", "howe-duality-real", "ideal-invariants-one-orbit-st", "jacquet-shalika", "k-finite-vectors-unitary", "kudla-splitting-split-unitary", "linnik", "log-der-one", "metaplectic-representation", "quadratic-class-field-theory", "radford-shuffle-polynomial", "rallis-inner-product-convergent", "real-metaplectic-representation", "schur-orthogonality-square-integrable", "siegel-set-unitary", "stone-von-neumann", "strong-approx-su", "theta-rational-invariance", "unramified-doubling-gl", "weil-representation-exists", "weil-representation-unitary-pair", "weil-unitary", "weyl-branching"]
order = 10
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
