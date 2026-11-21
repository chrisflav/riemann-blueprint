+++
kind  = "theorem"
title = "Cuspidal characters of GL(d) over a finite field"
source = "Green [green-1955]"
lean  = ["GlobalTheory.Published.GreenRegularCharacters", "PositivityTheory.Stage1.PM.greenRegularCharacters"]
order = 1
+++
Let $g$ be a prime, $d \ge 1$ and $\mathbb F_{g^d}$ the field with $g^d$
elements. To each character $\theta$ of $\mathbb F_{g^d}^\times$ there is a
class function $\tau_\theta$ on $\GL_d(\mathbb F_g)$ such that:

* if $\theta$ is regular (its $d$ Frobenius conjugates $\theta^{g^i}$ are
  distinct), $\tau_\theta$ is a cuspidal irreducible character of degree
  $\prod_{i=1}^{d-1}(g^i - 1)$, and at an elliptic element $y$ whose
  characteristic polynomial has a root $z \in \mathbb F_{g^d}^\times$,
  $$
  \tau_\theta(y) = (-1)^{d-1}\sum_{i=0}^{d-1}\theta\big(z^{g^i}\big);
  $$
* for regular $\theta, \theta'$, $\tau_\theta = \tau_{\theta'}$ if and only
  if $\theta' = \theta^{g^i}$ for some $i < d$;
* every cuspidal irreducible character is some $\tau_\theta$ with $\theta$
  regular.
