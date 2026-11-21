+++
kind  = "lemma"
title = "Counting first-order deformations"
provenance = "new"
lean  = ["GlobalTheory.HTCount.count", "GlobalTheory.HTCount.ksDim_at_point", "GlobalTheory.HTRho.rhoCount",
         "GlobalTheory.T.harrisTaylor_firstOrder_deformations_basis_count",
         "GlobalTheory.T.harrisTaylor_kodairaSpencer_directions_dim",
         "GlobalTheory.T.harrisTaylor_rho_part_deformation_dim"]
order = 1
+++
Let $A_0$ be an abelian variety with $\mathcal O_D$-action, polarisation and level
structure, of the type of [thm-unitary-shimura-integral-models], over an algebraically closed field
$k$. There are $r = a(n-1)$ endomorphisms $f_1, \dots, f_r$ of
$H^{\mathrm{dR}}_1(A_0)$ such that every first-order deformation of $A_0$ with its
structure lifts the Hodge filtration by $x \mapsto \sum_j c_j f_j(x)$ for a unique
$c \in k^r$, and every $c$ arises. Equivalently, the Kodaira–Spencer directions
have dimension $r$.
