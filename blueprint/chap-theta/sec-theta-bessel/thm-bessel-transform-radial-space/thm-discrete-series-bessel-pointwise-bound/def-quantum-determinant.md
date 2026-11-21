+++
kind  = "definition"
title = "The quantum determinant"
provenance = "published"
source = "Capelli; in the form of Molev [molev-2007]"
lean  = ["Formalism.REAL.GlRel", "Formalism.REAL.Tm", "Formalism.REAL.qminor",
         "Formalism.REAL.qdet"]
order = 1
+++
Let $\mathcal A$ be a complex algebra and $E = (E_{ab})_{a,b \le n}$ elements
satisfying the commutation relations of $\mathfrak{gl}_n$,
$$[E_{ab}, E_{cd}] = \delta_{bc}E_{ad} - \delta_{ad}E_{cb}.$$
Put $T(u) = u + E$ for $u \in \C$. The *quantum minors* and the *quantum
determinant* are
$$T^{a_1\dots a_t}_{b_1\dots b_t}(u) = \sum_{\sigma \in S_t}\operatorname{sgn}\sigma\ \prod_{s=1}^{t} T(u - s + 1)_{a_{\sigma(s)}b_s},\qquad \operatorname{qdet}T(u) = T^{1\dots n}_{1\dots n}(u),$$
the product taken in order. The quantum determinant is central, satisfies a
comatrix identity, and acts on a highest weight vector of weight $\nu$ by
$\prod_{s=1}^{n}(u - s + 1 + \nu_s)$: this is Capelli's identity. The
archimedean estimates apply it with $E_{ab}$ the action of the Lie algebra
of $\U(p,q)$ on a representation; *we read* it as the source of the
eigenvalues of the invariant differential operators acting on discrete
series coefficients and their Bessel transforms
([def-archimedean-bessel-data], [thm-discrete-series-bessel-pointwise-bound]).
