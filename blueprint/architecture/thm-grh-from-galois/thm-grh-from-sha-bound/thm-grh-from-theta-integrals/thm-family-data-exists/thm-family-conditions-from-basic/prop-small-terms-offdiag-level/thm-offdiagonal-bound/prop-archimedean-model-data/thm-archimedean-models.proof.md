+++
kind = "proof"
of   = "thm-archimedean-models"
uses = ["lem-radial-operator-transfer"]
+++
The equations of the local coordinates give smoothness of the transported
test functions. The shift operators of the archimedean model act radially
by polynomials: for $K$-types $\pi \to \rho$ there are $n$ and a polynomial
$q$ with
$$(|\zeta|^2 - T)^n\,S(\zeta) = q\big(\sqrt{|\zeta|^2 - T}\big)\,\theta(\zeta)$$
on the $\rho$-component. This polynomial dependence gives, for every frame
$e$ adapted to the gauge at an admissible archimedean setting, fibre maps
for each shift $1 \le l \le k-1$.

The rotation generator acts on transported functions as
$z\partial_z - \bar z\partial_{\bar z} + m$ for an integer $m$. This
invariance under the maximal compact subgroup gives a frame that carries
each operator of the real place ($\zeta$, $\bar\zeta$, their inverses, the
gradients, $\kappa$ and the shifts) to the corresponding model operator
([lem-radial-operator-transfer]). With the fibre maps, this bounds the model
operators and gives the models.
