+++
id    = "thm-theta-lift-nonvanishing"
kind  = "theorem"
title = "Theta lifts from definite unitary groups do not vanish"
provenance = "modified"
source = "after Rallis [rallis-1984]; J.-S. Li [li-1992]"
lean  = ["UpperTheory.TP.TLiftK", "UpperTheory.TP.K.tLiftK"]
order = 1
+++
Let $X$ be the hermitian space of dimension $n$ with Gram matrix $1$, and
$U$ an automorphic representation of $\U(X)$ with highest weights $\lambda$.
For all large $d$ the following holds. Let $W$ be the skew-hermitian space
with Gram matrix $\delta \cdot 1_d$, with splitting characters
$\chi_X, \chi_W$, and suppose $d + m_W \le 2\lambda_k$. Then there is an
automorphic representation $U'$ of $\U(W)$ with highest weights
$2\lambda'_k = 2\lambda_k - d - m_W + n + m_X$ whose local components at
split places are the local theta lifts of those of $U$.

The proof is Rallis' inner product argument, with the inputs of
[thm-theta-lift-ingredients]. The statement is the form needed here: the
group $\U(X)$ is definite and the weights of $U'$ are explicit.
