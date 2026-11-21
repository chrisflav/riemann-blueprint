+++
kind = "proof"
of   = "thm-critical-line"
uses = ["thm-half-plane"]
+++
Let $L(\chi, s) = 0$ with $0 < \Re s < 1$. If $\Re s > \tfrac12$, this
contradicts [thm-half-plane]. If $\Re s < \tfrac12$, let $\chi^*$ be the
primitive character that induces $\chi$. The two $L$-functions differ by
the factor $\prod_{p \mid N}(1 - \chi^*(p)p^{-s})$, and no term of it vanishes
for $\Re s > 0$ because $|\chi^*(p)p^{-s}| < 1$. So $L(\chi^*, s) = 0$. The
completed $L$-function of $\chi^*$ satisfies
$\Lambda(\chi^*, s) = \varepsilon\,\Lambda(\overline{\chi^*}, 1-s)$, and its
gamma factor does not vanish for $\Re s > 0$, so
$L(\overline{\chi^*}, 1-s) = 0$. As $\Re(1-s) > \tfrac12$, this contradicts
[thm-half-plane].
