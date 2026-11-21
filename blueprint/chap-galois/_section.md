+++
id    = "chap-galois"
kind  = "chapter"
title = "Galois representations"
uses  = ["chap-literature"]
order = 8
+++
This chapter proves [thm-galois-reps-polarized]: every polarized regular
algebraic cuspidal representation $\pi$ of $\GL_a$ over a CM field has an
$l$-adic Galois representation, with the Hodge–Tate weights read off $\pi$
and with Weil–Deligne representations that match the local parameters of
$\pi$ wherever these are determined ([rem-local-parameters-weak]). The outline
needs it in [thm-grh-from-galois]: these representations bound the
Tate–Shafarevich groups of [chap-sha] and enter the families of
[chap-families]. The statement is a weak form of the theorem of Harris–Taylor,
Shin, Chenevier–Harris, Barnet-Lamb–Gee–Geraghty–Taylor and Caraiani.

The proof starts in odd rank. We move an automorphic representation of a
definite unitary group in an odd number $a$ of variables, with a cuspidal type
at one place above $l$ and lacunary weights at another, to a Hecke eigensystem
on a compact unitary Shimura variety of signature $(1, a-1)$
([sec-gal-odd-rank]), and find it in the $l$-adic cohomology of Kuga–Sato
varieties, the fibre powers of the universal abelian scheme. General results
on Hecke eigenspaces ([sec-gal-eigenspaces]) then give a Galois
representation: the Eichler–Shimura congruence relation controls Frobenius,
and the crystalline comparison theorem and the Hodge–Tate decomposition give
the properties at $l$. [sec-gal-kuga-sato] and [sec-gal-shimura-models] build
the Kuga–Sato varieties and prove their good reduction; their Hodge numbers
come from the holomorphic Lefschetz formula, whose fixed points are CM points.

[sec-gal-assembly] extends this to all polarized pairs. The lacunary weights
and the determinant cut a piece of dimension $a$ out of the cohomology;
congruences and a limit argument in the style of Chenevier remove the
conditions at the two places above $l$; in even rank two theta lifts to odd
rank, with no character in common, isolate the representation; base change
([sec-gal-base-change]) passes from unitary groups to $\GL_a$. This gives
compatibility at the unramified places. [sec-gal-ramified] adds the ramified
places that matter, by a solvable base change that turns depth-zero
components into principal series.

The last section, [sec-gal-cuspidal], restates the theorem in the two forms the
families use. *It is not clear* how the transfer to Shimura varieties is
proved: it cites the Hasse norm theorem and no trace formula.
