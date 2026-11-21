+++
kind  = "definition"
title = "Members of a family"
provenance = "new"
lean  = ["Formalism.BasicNotions.D7", "Formalism.BasicNotions.Member",
         "Formalism.BasicNotions.Rows.Data", "Formalism.BasicNotions.ColumnsAtT",
         "Formalism.BasicNotions.PeriodMap"]
uses  = ["def-auxiliary-field-data", "def-family-ranks", "def-harish-chandra-parameters",
         "def-family-hermitian-spaces"]
order = 4
+++
A *member* is the datum on which every estimate for a family is stated. It
consists of the following, with many compatibilities between the parts.

* *Field and spaces.* Rank data $(k, m, t)$ ([def-family-ranks]), an
  auxiliary CM field $E$ ([def-auxiliary-field-data]), the hermitian spaces
  $X_j, Y_j, W_j, V_j$ over $E$ ([def-family-hermitian-spaces]), and a volume
  attached to each hermitian space.
* *Coefficients.* A totally complex Galois number field $L$ with an
  embedding $L \to \C$ compatible with complex conjugation, containing $E$,
  with an order $\mathcal O$ and its places.
* *Parameters.* For each embedding $\tau$ in the CM type a parameter
  ([def-harish-chandra-parameters]), and a finite set of *words* $u$, each with a binary letter for each of the
positions $2, \dots, k-1$ and
  with its own parameters, which agree with those of a base word $u_0$
  except in the entries $u_2, \dots, u_{k-1}$.
* *A chain for each word.* For each word $u$: the finite sets of lattice
  classes of the chain $X_0 \to \dots \to X_m$, with their finite
  stabilisers, and the theta kernels between functions on consecutive
  sets; a prime $T_u$ of $E$ dividing the level, with $f$ places of residue
  field $\mathbb F_{T_u}$, an action of $\mathbb F_{T_u}^\times$ on functions
  on the first set, and the subspace $M_{\mathrm{ram}}$ of functions on
  which the norm operators vanish (*we read* these as forms ramified at
  $T_u$); and a *period map*, evaluation at the anisotropic vector $z$
  followed by a pairing with a finite-dimensional space.
* *Links between words.* $c_u\bar c_u T_u = T_{u_0}$ for some $c_u \in E^\times$,
  and all $T_u$ lie in a window $[T^*, (1 + 1/fk)T^*]$.
* *Spaces of forms.* Spaces of automorphic forms at each step, for each
  twisting character, with $\mathcal O$-lattices, orthogonal projections, theta
  projections, decompositions by type, and the period pairings between
  them; and lengths $\mathrm{len}\,Ш^1_l(E, e)$ for $0 < e < t$.
* *Determinants.* A group of determinant classes with characters
  $\tilde\mu_j$ and $\chi_D$, and a relative determinant
  $\mathrm{rd}(L, L')$ of self-dual lattices, multiplicative in pairs and
  equal to $\det\gamma$ when $L' = \gamma L$ with $\gamma$ unitary. The
  restriction of $\chi_D$ to norm-one elements $z \in E$ is
  $\prod_\tau \tau(z)^{-1}$, and the scalars of the theta kernels are
  $\tilde\mu_{j+1}^{-1}\chi_D^{-N(j+1)/2}$ and $\tilde\mu_{j+1}\chi_D^{N(j)/2}$
  of the classes involved.
* *Galois data.* The congruence data ([def-congruence-data]) and the local
  data at the places above each prime $l$.

*It is not clear* what several of the remaining parts are: data attached
to chosen local situations along the chain, and further global and local
constants. They enter through the hypotheses of [def-family-data].
