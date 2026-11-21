+++
kind  = "theorem"
title = "The contragredient is the inverse transpose (Gelfand–Kazhdan)"
lean  = ["GlobalTheory.Published.GelfandKazhdanDual", "PositivityTheory.JMult1.gelfandKazhdanDual_of_rigidity"]
uses  = ["cusp-forms-bounded-gl", "jacquet-shalika-rigidity"]
order = 7
+++
Let $E$ be a totally complex number field and $\pi$ a cuspidal automorphic
representation of $\GL_n(\A_E)$. There is a non-degenerate pairing
$B : \pi \times \pi \to \C$ with
$B(\pi(g)\varphi, \pi({}^tg^{-1})\psi) = B(\varphi, \psi)$ at the finite
places, the corresponding identity at the archimedean maximal compact
subgroup, and $B(X\varphi,\psi) + B(\varphi, X'\psi) = 0$ for $X$ in the Lie
algebra and $X' = -{}^tX$. In other words $\pi^\vee \cong \pi\circ\theta$
with $\theta(g) = {}^tg^{-1}$ (Gelfand–Kazhdan, 1975). It is deduced from
strong multiplicity one [jacquet-shalika-rigidity], multiplicity one and
the boundedness of cusp forms [cusp-forms-bounded-gl].
