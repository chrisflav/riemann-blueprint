+++
kind = "proof"
of   = "thm-good-towers-from-arakelov-inputs"
uses = ["thm-abelian-variety-torsion-count", "lem-flag-cover-pullback", "thm-arithmetic-intersection-theory",
        "thm-semi-abelian-hom-extension", "thm-zarhin-trick", "thm-arithmetic-hilbert-samuel-inequalities", "thm-fargues-hodge-tate-sequence",
        "thm-gaga-sections", "lem-absolute-siegel-lemma", "thm-hasse-norm-quadratic", "thm-landherr-cm",
        "lem-de-rham-hodge-tate-flag-comparison", "thm-unitary-integral-models", "thm-semistable-reduction",
        "lem-weyl-antisymmetry-intersection", "lem-volume-theorem-from-tower-identities"]
+++
*The tower.* Build the tower from the integral models
([thm-unitary-integral-models]) and the Hodge bundles, using Hasse's and
Landherr's norm theorems ([thm-hasse-norm-quadratic], [thm-landherr-cm]) and
semistable reduction ([thm-semistable-reduction]) to control the reductions.
The flat realisation uses the integral models with compatibility of
toroidal compactifications under change of level and Hecke operators, a key
formula for arithmetic degrees and numerical Segre classes
([thm-arithmetic-intersection-theory], with resolution in projective space),
the arithmetic Hilbert–Samuel inequalities and Moriwaki's theorem
([thm-arithmetic-hilbert-samuel-inequalities]), extension of homomorphisms of
semi-abelian schemes ([thm-semi-abelian-hom-extension]), Fargues' Hodge–Tate
sequence ([thm-fargues-hodge-tate-sequence]), GAGA for sections
([thm-gaga-sections]), the properties of flag models, analytic estimates,
Zhang's bounds for heights on Grassmannians and a perturbation lemma for
antisymmetric forms. It also uses a slope bound for hermitian lattices,
which follows from lines of large degree ([lem-absolute-siegel-lemma]): a
line of degree at least $\mu - \tfrac12\log i - \varepsilon$ in every
sublattice bounds the maximal slope.

*Two properties of the universal abelian scheme.* Fargues' sequence,
quotients of abelian schemes by finite flat group schemes, Zarhin's theorem
([thm-zarhin-trick]) and a statement on ordinary curves show that the de Rham
and Hodge–Tate lattices of the universal abelian scheme come from families of
Dieudonné lattices; by [lem-de-rham-hodge-tate-flag-comparison] the Chern
classes of the de Rham and Hodge–Tate flags then agree at good primes.
Arithmetic intersection numbers are invariant under Galois twists of the
datum, by the inputs on flag models, a comparison statement proved by prime
avoidance and resolution, and the uniformity of theta functions of abelian
varieties. Resolution also gives integrability of Green functions at points.

*The volume theorem.* Besides the flag comparison, it needs a geometric bound
for the nine geometric quantities of the tower, triviality of the flag bundle
on the Hodge part (from Fargues' sequence), a flat-degree statement, a
statement on twisted automorphisms and two comparison statements for
intersection numbers; the remaining ones are proved directly. With these the
tower satisfies a list of identities: proportionality, the relations
$I_1, \dots, I_8$ between arithmetic intersection numbers of root line bundles
([thm-arithmetic-intersection-theory]), nefness of the models, and a lower
bound for slopes. The Weyl antisymmetry $I_8$ is
[lem-weyl-antisymmetry-intersection], and
[lem-volume-theorem-from-tower-identities] turns the identities into the
conclusions. Multiplication by $n$ on abelian schemes and flag covers
([lem-flag-cover-pullback]) enter along the way.
