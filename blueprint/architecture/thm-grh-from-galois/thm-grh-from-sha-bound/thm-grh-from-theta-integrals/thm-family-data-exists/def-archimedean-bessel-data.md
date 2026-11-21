+++
kind  = "definition"
title = "Archimedean Bessel data"
provenance = "modified"
source = "Bessel models in the sense of Gan–Gross–Prasad [gan-2012]"
lean  = ["Formalism.QuantumDeterminants.Hpk", "Formalism.QuantumDeterminants.herm",
         "Formalism.QuantumDeterminants.UH", "Formalism.QuantumDeterminants.Nset",
         "Formalism.QuantumDeterminants.UWset", "Formalism.QuantumDeterminants.inWb",
         "Formalism.QuantumDeterminants.Tz", "Formalism.QuantumDeterminants.ell",
         "Formalism.QuantumDeterminants.psi", "Formalism.QuantumDeterminants.Dmin",
         "Formalism.QuantumDeterminants.Gf", "Formalism.QuantumDeterminants.Mt",
         "Formalism.QuantumDeterminants.IsBesselFunctional",
         "Formalism.QuantumDeterminants.besselJ",
         "Formalism.FourierDecayAlt.B.Mat", "Formalism.FourierDecayAlt.B.GV",
         "Formalism.FourierDecayAlt.B.RealPlaceData", "Formalism.FourierDecayAlt.M.Par"]
order = 99
+++
Let $k \ge 1$, $r \ge 0$ and $n = 2r + k + 1$. On $\C^n$ with basis
$e_1, \dots, e_r, w_0, \dots, w_k, e_r^*, \dots, e_1^*$ let $H_{k,r}$ be the
hermitian form with $\langle e_a, e_b^*\rangle = \delta_{ab}$, the $e_a$ and
the $e_a^*$ isotropic, $w_0, \dots, w_{k-1}$ orthonormal and
$\langle w_k, w_k\rangle = -1$. Its signature is $(k + r, r + 1)$; let
$G = \U(H_{k,r})$ and $W = \langle w_0, \dots, w_k\rangle$.

* For $z \in W$ put $T(z) = -\langle z, z\rangle$. When $T(z) > 0$ the
  stabiliser $W_z$ of $z$ and of all $e_a, e_a^*$ is compact, isomorphic to
  $\U(k)$.
* $N$ is the group of $g \in G$ that are unipotent upper triangular on
  $e_1, \dots, e_r$ and act trivially on $W$ modulo $\langle e_1, \dots, e_r\rangle$;
  *we read* it as the unipotent radical of the parabolic subgroup fixing the
  isotropic flag $\langle e_1\rangle \subset \dots \subset \langle e_1, \dots, e_r\rangle$.
  Its character is $\psi_z(n) = \exp\big(i\,\Re(c\,\ell_z(n))\big)$ with $c = -2i$ and
  $$\ell_z(n) = \sum_{a=1}^{r-1} n_{a,a+1} + (nz)_r,$$
  where $n_{a,b}$ are matrix entries and $(nz)_r$ is the $e_r$-coordinate of
  $nz$. $W_z$ normalises $N$ and fixes $\psi_z$.
* A *Bessel functional* for representations $\sigma$ of $G$ and $\pi$ of
  $W_z$ is a functional $\lambda$ with
  $\lambda(\sigma(hn)v \otimes \pi(h)w) = \psi_z(n)\,\lambda(v \otimes w)$
  for $h \in W_z$, $n \in N$.
* For $z, z'$ and $g \in G$, let $D_l(g)$ be the leading $l \times l$ minor of
  the Gram matrix $\big(\langle g f'_b, f_a\rangle\big)$, where
  $f = (e_1, \dots, e_r, z)$ and $f' = (e_1, \dots, e_r, z')$, and put
  $$G_{z,z'}(g) = |D_{r+1}(g)|^2 - T(z)\,T(z')\,|D_r(g)|^2.$$
  The minors and $G_{z,z'}$ are invariant under $W_zN$ on the left and
  $W_{z'}N$ on the right.

*Real-place data* consist of such $z, z'$ with $T(z), T(z') > 0$, unitary
representations $\pi, \pi'$ of $W_z, W_{z'}$, Haar measures on $G$, $W_z$,
$W_{z'}$ and $N$, a measurable section, and a smooth cutoff supported in
$(\tfrac12, 2)$ with integral $1$; they define the Bessel transform of
[thm-bessel-transform-radial-space]. The pointwise bounds use *parameter
data* $(k, r, T, T', u, u')$, two Harish-Chandra parameters with gaps, and the
interlacing patterns between them.

This is the archimedean form of the Bessel models of Gan, Gross and Prasad
for the pair $\U(k) \subset \U(k + r, r + 1)$.
