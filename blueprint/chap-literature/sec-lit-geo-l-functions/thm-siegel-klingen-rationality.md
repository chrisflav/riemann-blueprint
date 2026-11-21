+++
kind  = "theorem"
title = "Siegel–Klingen rationality with Deligne–Ribet integrality"
lean  = ["GlobalTheory.Published.SiegelKlingen", "GlobalTheory.Published.SiegelKlingenDeligneRibet",
         "PositivityTheory.Prw.siegelKlingenDeligneRibet_of", "PositivityTheory.Prw.siegelKlingen_holds"]
uses  = ["thm-deligne-ribet"]
order = 5
+++
Let $F$ be a totally real field, $\mathfrak f \ne 0$ an ideal and
$\varepsilon$ a rational-valued function on ideals prime to $\mathfrak f$,
constant on narrow ray classes modulo $\mathfrak f$. Then
$L(\varepsilon, s) = \sum_I \varepsilon(I) N I^{-s}$ continues to a
holomorphic function on $\C \setminus \{1\}$ whose values $L(\varepsilon, 1-k)$,
$k \ge 1$, are rational (Siegel 1970, Klingen 1962). Together with the
congruences of [thm-deligne-ribet], this is the statement used.
