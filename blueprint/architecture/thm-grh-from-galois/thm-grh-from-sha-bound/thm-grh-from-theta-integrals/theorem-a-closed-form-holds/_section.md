+++
id    = "theorem-a-closed-form-holds"
kind  = "theorem"
title = "Fock lattices are nearly unimodular on average"
lean  = ["Formalism.MainNotions.G.GramWindowAlt.theorem_A_closed_form_holds"]
order = 10
+++
For a lattice $L$ over a discrete valuation ring $\mathcal O$ with a pairing
$B$ into its fraction field, a saturated sublattice $L_1$ is *good at depth
$D$* if every primitive vector $u$ of $L_1$ has a partner $u' \in L$ with
$v_p(B(u, u')) \le D$. The *bad share* of $L$ at depth $D$ is
$1 - \max\operatorname{rk}L_1/\operatorname{rk}L$ over good $L_1$.

Let $p$ be a prime, $\mathcal O' / \mathcal O$ an unramified quadratic
extension of discrete valuation rings attached to a member, and consider the
lattices of polynomials in the local construction, with the *Fock pairing*
$$\langle f, g\rangle = \sum_\alpha \alpha!\,f_\alpha g_\alpha$$
weighted on each block by explicit constants. Then, with the constants of
the construction chosen in a fixed order, each large in terms of the
previous ones, there is $C$ such that for every
admitted local datum the mean of the bad share at depth
$$D = C\,Y^2N_1^2(r+1)^2\big(\log_p(8a + r) + 1\big) + 4N_t(r+1)\log_p a$$
over the admissible range of exponents is at most $C(t+1)N_1/Y$.
