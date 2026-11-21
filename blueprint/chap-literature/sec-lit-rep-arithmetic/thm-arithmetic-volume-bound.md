+++
kind  = "theorem"
title = "Arithmetic volume is at least the self-intersection (Gillet–Soulé, Zhang)"
lean  = ["GlobalTheory.Published.VolGe", "GlobalTheory.VolBr.volGe_of_hilbertSamuel"]
uses  = ["thm-arithmetic-intersection-theory", "thm-arithmetic-hilbert-samuel", "thm-kawamata-viehweg"]
order = 5
+++
Let $X$ be an arithmetic variety of relative dimension $D$ and $\bar L$ a
hermitian line bundle that is nef on the fibres and has semipositive
metrics. If $\widehat{\deg}(\bar L^{D+1}) = a$, then the arithmetic volume of
$\bar L$ is at least $a$. This is the arithmetic Hilbert–Samuel inequality
(Gillet–Soulé, 1992; Zhang, 1995). It follows from the arithmetic
intersection theory [thm-arithmetic-intersection-theory], the arithmetic Hilbert–Samuel formula
[thm-arithmetic-hilbert-samuel] and Kawamata–Viehweg vanishing
[thm-kawamata-viehweg].
