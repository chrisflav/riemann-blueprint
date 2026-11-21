+++
kind  = "lemma"
title = "The constant term of a theta integral on the big cone"
lean  = ["GlobalTheory.T.exists_isCT_integral_eq_cone_integral_add_hasLaw", "GlobalTheory.ThK.unfoldCTBigCone"]
uses  = ["thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-borel-casselman", "thm-casselman-wallach", "thm-cm-j-hilbert-class-field", "thm-cusp-bounded-unitary", "thm-cusp-uniform-decay", "thm-cusp-decay-sobolev", "thm-cusp-rapid-decay", "thm-cusp-trace-class", "thm-gelfand-cuspidal-mirabolic", "thm-cuspidal-spectrum-gl", "thm-discrete-series-parametrisation", "thm-discrete-series-exist-cover", "thm-discrete-series-exist", "thm-discrete-series-frame-independent", "thm-discrete-series-lowest-k-type", "thm-discrete-series-exist-upq", "thm-dixmier-malliavin", "thm-flath-unramified", "thm-formal-degree-upq", "thm-geometric-lemma-filtration", "thm-hc-infinitesimal-equivalence", "thm-howe-duality-gl-gl", "thm-green-parametrisation", "thm-hc-finiteness-unitary", "thm-hc-modules-unitary", "thm-hecke-l-entire", "thm-hecke-l-nonvanishing-line-one", "thm-hecke-functional-equation-cm", "thm-hermitian-hasse-principle", "thm-landherr-hermitian-forms", "thm-holomorphic-discrete-series", "thm-howe-duality-archimedean-trivial", "thm-cm-j-one-orbit", "thm-jacquet-shalika", "thm-hc-k-finite-vectors", "thm-kudla-splitting", "thm-linnik", "thm-log-derivative-at-one", "thm-weil-representation-real", "thm-quadratic-class-field-theory", "thm-radford-shuffle", "thm-rallis-inner-product", "thm-oscillator-lie-action", "thm-godement-schur-orthogonality", "thm-reduction-theory-unitary", "thm-stone-von-neumann", "thm-strong-approximation-su", "thm-theta-rational-invariance", "thm-unramified-doubling-gl", "thm-weil-representation-unitary-exists", "thm-weil-representation-auxiliary-pairs", "thm-siegel-weil-weil-range", "thm-weyl-branching"]
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
