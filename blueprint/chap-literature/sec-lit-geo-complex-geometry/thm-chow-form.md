+++
kind  = "theorem"
title = "Existence and uniqueness of Chow forms"
source = "Chow–van der Waerden [chow-van-der-waerden-1937]"
lean  = ["GlobalTheory.Published.ChowFormExists", "GlobalTheory.Published.chowFormExists_holds"]
order = 1
+++
Let $k$ be a field of characteristic $0$ and $I \subset k[x_1, \dots, x_N]$ a
homogeneous ideal that stays prime over $\bar k$, with
$\dim k[x]/I = D + 1$; so $I$ defines a geometrically irreducible projective
variety $X$ of dimension $D$ and degree $d$. Then $X$ has a Chow form: a
polynomial $f$ in $D+1$ sets of $N$ variables, of degree $d$ in each,
vanishing exactly on the $(D+1)$-tuples of hyperplanes that meet on $X$.
It is unique up to a non-zero scalar.
