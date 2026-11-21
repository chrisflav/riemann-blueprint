+++
kind  = "definition"
title = "Harish-Chandra parameters and dominant weights"
provenance = "new"
lean  = ["Formalism.BasicNotions.HCParam", "Formalism.BasicNotions.DomWeight",
         "Formalism.BasicNotions.hcToWeightQ"]
uses  = ["def-family-ranks"]
order = 2
+++
Fix rank data $(k, m, t)$ as in [def-family-ranks]. A *parameter* consists of
$$u \in (\tfrac12 + \Z)^k,\quad v \in \Z^{k-1},\quad b, e \in \Z^m$$
such that
$$u_1 > v_1 > u_2 > v_2 > \dots > v_{k-1} > u_k > -b_1 > -e_1 > -b_2 > \dots > -b_m > -e_m,$$
with gaps $e_j - b_j \ge (t+3)/2$ and $b_{j+1} - e_j \ge (t+3)/2$. So $v$
interlaces $u$, as in the branching law from $\U(k)$ to $\U(k-1)$, and the
$b_j, e_j$ continue the sequence downwards with large gaps. A member of a
family ([def-family-member]) carries one parameter for each embedding in
the CM type of the auxiliary field; *we read* these as the archimedean
Harish-Chandra parameters of the representations in its theta tower. At
the top places the extreme entries are tied to the weights of
[def-family-scale]: $u_1 = a_\tau + \tfrac{k-1}{2}$ and
$u_k = -b_\tau - \tfrac{k-1}{2}$.

A *dominant weight* of $\GL_N$ is a non-increasing $\lambda \in \Z^N$. A
Harish-Chandra parameter $\mu \in \Q^N$ gives the weight $\mu - \rho_N$, where
$\rho_N = \big(\tfrac{N-1}{2} - i\big)_{0 \le i < N}$; the parameter is
*integral* if this weight lies in $\Z^N$.
