+++
kind = "proof"
of   = "lem-h2-tate-twists-bound"
uses = ["thm-borel-type-rank-bound", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-tate-local-finiteness-padic", "thm-tate-local-duality-l-adic",
        "thm-poitou-tate"]
+++
Cycles of cyclic subgroups give classes in the homology of
$\GL_n(\mathcal O_L)$. Reduced at primes of $L$, they are detected by explicit
cocycles on $\GL_n$ of finite fields, which take the value
$x^{e+1}v(g)$ on the class of an element of order $q$ twisted by $x$. *We
read* this as a form of Soulé's comparison between the homology of
$\GL_n(\mathcal O_L)$ and Galois cohomology of Tate twists. The rank bound of
Borel type ([thm-borel-type-rank-bound]) limits how many independent classes there are;
[Chebotarev's theorem](@thm-chebotarev-degree-one) supplies primes of degree one
at which to reduce. The [Poitou–Tate sequence](@thm-poitou-tate),
[local Tate duality](@thm-tate-local-duality-l-adic) and [local finiteness](@thm-tate-local-finiteness-padic)
turn the result into the bound on $H^2$.
