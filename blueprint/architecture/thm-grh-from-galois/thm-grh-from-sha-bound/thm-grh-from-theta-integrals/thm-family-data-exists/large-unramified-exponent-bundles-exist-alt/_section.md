+++
id    = "large-unramified-exponent-bundles-exist-alt"
kind  = "theorem"
title = "Membership and admissible data for the families"
lean  = ["GlobalTheory.Fc.StageOneU.member_bundles_large_unramified_exponents_alt", "GlobalTheory.T.large_unramified_exponent_bundles_exist_alt"]
uses  = ["def-local-parameters", "thm-grh-from-theta-integrals"]
order = 10
+++
Assume the published results on unitary groups and theta lifts used in
[thm-grh-from-theta-integrals], and that test vectors are rational: at the
real data of the construction, finitely many linear functionals separate the
space of theta values and take values in the base field on the theta lifts
of rational vectors. Let $\rec$ be a system of local parameters
([def-local-parameters]) and $c$ a real number. Let $A$ be a condition on
twisting data that holds for all sufficiently large auxiliary data (in the
proof of [thm-family-data-exists], $A$ asks that grids of evaluation points
of a given size can be completed). Let $p$ be the construction data for the
families obtained from $\rec$ by restricting the auxiliary choices to those
with origin data for $c$ and imposing $A$. Then:

1. *Siegel mass ratio.* Let $K$ be a CM field such that $K/K^+$ is
   unramified at every finite place, and let $L_M = \mathcal O_K^M$ with the
   hermitian form $h(x, y) = \sum_i \bar x_i y_i$. Write
   $m(L_M) = \sum_{[L]} 1/|\mathrm{Aut}(L)|$, the sum running over the classes
   in the genus of $L_M$. For every $M \ge 3$,
   $$\frac{m(L_M)}{m(L_{M-1})} = \frac{\big((M-1)!\,(v_K/\pi)^M\big)^{d}}{(2v_K)^{d/2}}\,L(M, \eta^M),$$
   where $d = [K^+ : \Q]$, $v_K = \tfrac12|d_K|^{1/[K:\Q]}$, $\eta$ is the
   quadratic character of $K/K^+$, and $L(M, \eta^M)$ is the Euler product
   over the primes of $K^+$.
2. *Membership.* The families built from $p$ satisfy the membership
   conditions:
   * there are auxiliary base data containing any prescribed finite sets of
     algebraic numbers, and admissibility is stable under enlarging the base;
   * for untwisted twisting data, every starting datum extends to a
     constructed point of a family;
   * every constructed point has the *twisting property*: for each twisting
     index $i$ there is a ray class character $\psi$ such that $\psi^a$ is a
     good twist for every integer $a$ prime to the prime $\ell_i$ of $i$
     ([twist-all-powers-of-galois-cohomology-class-field]);
   * after enlarging the base and choosing twisting data that avoid any given
     finite set of primes, the constructed points are good and their twists
     are good at every place.
3. *Admissible data.* At every good constructed point of these families there
   is an admissible datum compatible with $p$.

The step is named after large unramified exponents. *It is not clear*
which exponents are meant. *We read* them as the exponents
$k$ of the $\ell$-power twisting characters, which are large for large
auxiliary data.
