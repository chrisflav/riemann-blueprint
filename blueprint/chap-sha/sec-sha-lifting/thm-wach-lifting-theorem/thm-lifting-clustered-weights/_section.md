+++
id    = "thm-lifting-clustered-weights"
kind  = "theorem"
title = "Local lifting bound for clustered weights"
provenance = "new"
lean  = ["GlobalTheory.T.localLiftingTheoremB_of_blochKato_tateDuality_eulerChar", "GlobalTheory.theoremB_closing"]
order = 1
+++
Let $C \ge 320$, let $l \ge 11$, let $K$ be an unramified extension of $\Q_l$
of degree $n$, and let $F : T_1 \to T_2$ be a surjection of crystalline
lattices with Wach modules. Suppose that at each embedding the Hodge–Tate
weights of $T_1$ lie in $[-\eta, \eta]$ or in a window of length $S$ at
distance $s_i > \eta$ from $0$, that at most $m$ weights of $T_2$ are small,
and that the windows are either *thick* ($b \le s_i \le b + \eta$) or have
$s_i \le w$, with $20w, 20\eta, 20S \le b$ and not every window thick. Then
the cokernel of $H^1_f(T_1) \to H^1_f(T_2)$ has length at most
$$C(n+1)\,\mathrm{rk}\,T_2\Big(\frac{h}{l^2} + \frac{w+\eta}{l} + S + 1 + \log_l 2h + \eta\beta\Big) + Cnm\,e'$$
when the windows alternate in direction and no three consecutive ones are
thick, and a similar bound with factors $R^2$ when runs of thick windows
have length less than $R$. Here $h$ is an explicit height, $\beta \in
\{0,1\}$ and $e'$ is a lifting exponent of $T_1$.
