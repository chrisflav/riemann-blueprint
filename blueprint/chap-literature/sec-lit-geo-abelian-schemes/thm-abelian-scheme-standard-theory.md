+++
kind  = "theorem"
title = "The standard theory of principally polarised abelian schemes"
provenance = "published"
source = "Mumford [mumford-1970]; Mumford–Fogarty–Kirwan [mumford-1994]; Faltings–Chai [faltings-chai-1990]"
lean  = ["GlobalTheory.Published.CubeTheorem", "GlobalTheory.CubeTop.cubeTheorem",
         "GlobalTheory.SpreadingModels.cubeTheorem_holds",
         "GlobalTheory.T.theoremOfCubeAbelianScheme_over_arbitrary_base",
         "ReciprocityTheory.ChartRestriction.G.Out.Laws", "ReciprocityTheory.ChartRestriction.G.Out.Laws2",
         "GlobalTheory.abelianSchemeLaws_all", "GlobalTheory.T.abelianScheme_laws_unconditional",
         "GlobalTheory.Published.KernelFiniteFlatSt", "GlobalTheory.kernelFiniteFlat_holds"]
order = 12
+++
Let $S$ be a locally noetherian scheme and $A \to S$ an abelian scheme of
relative dimension $g$.

* (Theorem of the cube.) For every line bundle $M$ on $A$, every $S$-scheme
  $T$ and points $a, b, c \in A(T)$, the line bundle
  $$
  (a+b+c)^*M \otimes (a+b)^*M^{-1} \otimes (a+c)^*M^{-1} \otimes (b+c)^*M^{-1}
  \otimes a^*M \otimes b^*M \otimes c^*M \otimes 0^*M^{-1}
  $$
  on $T$ is trivial.
* (Rigidity.) A morphism of abelian schemes over $S$ that preserves the unit
  sections is a homomorphism, and the global functions on $A$ are those of $S$.
* (Multiplication by $n$.) For $n \ge 1$, multiplication by $n$ is finite, flat
  and surjective, and étale when $n$ is invertible on $S$.

Suppose now that $A$ carries a principal polarisation, given by a line bundle
$L$ as in the introduction to this section. Then moreover:

* $[n]^*L \cong L^{n^2}$, and $t_{x+y}^*L \otimes L \cong t_x^*L \otimes t_y^*L$
  locally on the base, for points $x, y$ (theorem of the square);
* over an algebraically closed field $H^0(A, L^n)$ has dimension $n^g$ for
  $n \ge 1$; locally on $S$ the sections of $L^n$ are free of rank $n^g$ and
  their formation commutes with base change; $L^n$ is very ample for $n \ge 4$;
* a point $x$ satisfies $Nx = 0$ if and only if $t_x^*L^N \otimes L^{-N}$ is
  locally trivial;
* the Weil pairing on the $k$-torsion exists, is bimultiplicative and
  alternating, satisfies $e_{kl}(x, y) = e_k(lx, y)$, and is non-degenerate over
  algebraically closed fields in which $k$ is invertible;
* for $k = 1$ or $k \ge 4$ invertible on an algebraically closed field,
  $H^0(A, L^k)$ is an irreducible representation of the theta group of $L^k$;
  for odd invertible $k$, symmetric lifts of $k$-torsion points to the theta
  group exist and are unique;
* an automorphism of $A$ that preserves $L$ up to a locally trivial bundle and
  fixes all $M$-torsion points, $M \ge 3$, is the identity (Serre's lemma);
* over a noetherian affine base, the quotient of $A$ by a finite flat
  subgroup scheme exists and is an abelian scheme;
* for a relatively ample line bundle $M$ on an abelian scheme over a
  noetherian ring, the group $K(M)$ of points $x$ with $t_x^*M \otimes M^{-1}$
  locally trivial is a finite flat closed subgroup scheme.

These facts, with a few further ones of the same kind (base change of
polarisations, finite unramified extensions of a complete discrete valuation
ring with a given residue field, sections of twisted line bundles), are used
together in many steps of the proof.
