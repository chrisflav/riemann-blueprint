+++
kind = "proof"
of   = "lemma-k-lit-n-alt"
uses = ["b-odd", "cheb", "chebotarev-degree-one", "local-finiteness-k", "local-tate-duality-k",
        "poitou-tate-normalised"]
+++
Cycles of cyclic subgroups give classes in the homology of
$\GL_n(\mathcal O_L)$. Reduced at primes of $L$, they are detected by explicit
cocycles on $\GL_n$ of finite fields, which take the value
$x^{e+1}v(g)$ on the class of an element of order $q$ twisted by $x$. *We
read* this as a form of Soulé's comparison between the homology of
$\GL_n(\mathcal O_L)$ and Galois cohomology of Tate twists. The rank bound of
Borel type ([b-odd]) limits how many independent classes there are;
[Chebotarev's theorem](@chebotarev-degree-one) supplies primes of degree one
at which to reduce. The [Poitou–Tate sequence](@poitou-tate-normalised),
[local Tate duality](@local-tate-duality-k) and [local finiteness](@local-finiteness-k)
turn the result into the bound on $H^2$.
