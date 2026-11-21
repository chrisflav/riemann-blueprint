+++
kind = "proof"
of   = "thm-arithmetic-volume-bound"
uses = ["thm-arithmetic-hilbert-samuel", "thm-arithmetic-intersection-theory", "thm-kawamata-viehweg"]
+++
Arithmetic intersection theory [thm-arithmetic-intersection-theory] gives an
auxiliary hermitian line bundle $\bar P$ with
$\widehat{\deg}\big((\bar L^{m}\otimes\bar P)^{D+1}\big)/m^{D+1} \to a$, and
the numerics of nef bundles from [thm-kawamata-viehweg] control the
geometric degrees on the generic fibre. The arithmetic Hilbert–Samuel
theorem [thm-arithmetic-hilbert-samuel] then gives, for every $\varepsilon > 0$
and infinitely many $m$, at least $\exp\big((a-\varepsilon)\,m^{D+1}/(D+1)!\big)$
small sections of $L^m$, which is the lower bound on the volume.
