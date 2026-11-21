+++
kind  = "definition"
title = "The hermitian spaces of a family member"
provenance = "new"
lean  = ["Formalism.BasicNotions.HSpace", "Formalism.BasicNotions.Spaces",
         "Formalism.BasicNotions.CMData"]
uses  = ["def-family-ranks", "def-auxiliary-field-data"]
order = 4
+++
Let $E/F$ be a CM extension and fix rank data $(k, m, t)$
([def-family-ranks]). A *hermitian space* here is a finite-dimensional
$E$-vector space $V$ with a nondegenerate hermitian form, a basis, its
signature at each embedding $E \to \C$, and a unimodular
$\mathcal O_E$-lattice $L_0 \subset V$.

The *spaces of a member* are hermitian spaces over $E$ with a prime $T$
(the *level prime*) as follows.

* *The definite chain.* Spaces $X_0, \dots, X_m$ with $\dim X_j = N(j)$,
  definite at every infinite place. The groups $\U(X_j)$ are the definite
  unitary groups of the family.
* *The top space.* $X_m = X' \oplus \langle z\rangle$ with $z$ anisotropic and
  $\dim X' = r + mt$.
* *The intermediate spaces.* Spaces $Y_j \supset X_j$ ($j < m$) of dimension
  $r + jt$, and $Y_m \cong X'$. The first is
  $$Y_0 = X_0 \oplus \langle z_0\rangle \oplus H^{m/2-1}, \qquad \langle z_0, z_0\rangle = -T,$$
  with $H$ a hyperbolic plane, of signature $(k + m/2 - 1, m/2)$ everywhere.
* *The indefinite spaces.* Spaces $W_1, \dots, W_m$ of dimension $r$ and
  signature $(k + j - 1, m - j)$ at every infinite place, each isometric to
  $Y_0$ over the finite adeles.
* *The auxiliary spaces.* Spaces $V_1, \dots, V_m$ of dimension $n_V = r + t$
  with an orthonormal lattice for $\pm$ the form.

Theta lifts run along $X_0 \to X_1 \to \dots \to X_m$ ([def-theta-tower-step]);
*we read* the $Y_j$ and $W_j$ as the other members of the seesaw pairs
that compare consecutive steps, and the $V_j$ as the spaces whose Galois
representations of dimension $n_V$ enter the congruence bound
([thm-congruence-module-selmer-bound]).
