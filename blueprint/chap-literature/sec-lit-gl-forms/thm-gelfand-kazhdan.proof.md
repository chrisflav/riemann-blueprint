+++
kind = "proof"
of   = "thm-gelfand-kazhdan"
uses = ["thm-cusp-bounded-gl", "thm-jacquet-shalika-strong-mult-one"]
+++
The case $n = 0$ is empty, and twisting by a character reduces to $\pi$
with unitary central character. The functions
$g \mapsto \overline{\varphi({}^tg^{-1})}$, $\varphi \in \pi$, form a cuspidal
representation with the same Satake parameters as $\pi$ at almost all
places, so strong multiplicity one [thm-jacquet-shalika-strong-mult-one]
gives an isomorphism $J$ from it to $\pi$. Cusp forms are bounded
[thm-cusp-bounded-gl], hence square-integrable, and the required pairing
$B(\varphi, \psi)$ is the $L^2$ inner product of $\varphi$ with the image
under $J$ of $g \mapsto \overline{\psi({}^tg^{-1})}$.
