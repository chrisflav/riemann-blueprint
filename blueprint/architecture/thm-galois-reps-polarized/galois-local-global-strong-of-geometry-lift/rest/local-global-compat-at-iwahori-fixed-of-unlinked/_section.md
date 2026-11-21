+++
id    = "local-global-compat-at-iwahori-fixed-of-unlinked"
kind  = "theorem"
title = "Compatibility at depth-zero places"
lean  = ["UpperTheory.Gal.ToralGalois.R2.ToTor",
         "UpperTheory.Gal.ToralGalois.R2.localGlobalCompatAtIwahoriFixed_of_unlinked",
         "UpperTheory.Gal.ToralGalois.R2.toTor_holds"]
order = 10
+++
Let $(\pi, \chi)$ be a polarized regular algebraic cuspidal pair on $\GL_n(\A_E)$
and $r$ a continuous representation attached to $\pi$ at almost all places.
Assume that $r$ is de Rham at the places above $l$ where $\pi_w$ is a principal
series from characters no two of which differ by $|\cdot|$. Let $w$ be a place
where $\pi_w$ has non-zero vectors fixed by
$K_1 = \ker(\GL_n(\mathcal O_w) \to \GL_n(k_w))$, and suppose either that $\pi_w$ is such
a principal series, or that $E_w \cong \Q_g$ and the cuspidal support of $\pi_w$ has
no two segments of length at least $2$ in the same unramified orbit. If the
local parameter $\rec(\pi_w)$ of [thm-local-parameters-exist] has $N = 0$, then:

* for $w \nmid l$, the Weil–Deligne representation of $r|_{G_{E_w}}$ has $N = 0$ and
  inertia acts on it with the characteristic polynomials of $\rec(\pi_w)$;
* for $w \mid l$, $r$ is de Rham and potentially semistable at $w$, with the
  same conclusion for its Weil–Deligne representation.

On the way: for $E_w \cong \Q_g$ and $\pi_w$ of mixed depth-zero type, there are a
solvable extension $K/E$ and a polarized pair on $\GL_n(\A_K)$ with the same
infinitesimal characters, attached to $r|_{G_K}$, whose component above $w$ is
such a principal series with the same inertial characteristic polynomials.
