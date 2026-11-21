+++
kind  = "lemma"
title = "Lifting finite classes along crystalline lattices"
lean  = ["GlobalTheory.T.lift_surjection_good_crystalline_lattices", "GlobalTheory.TheoremT.liftF_of_isGood"]
uses  = ["bhatt-scholze-crystalline-lattices", "fontaine-bcris"]
order = 1
+++
Assume the theorem of Bhatt and Scholze on crystalline lattices and
Fontaine's crystalline period ring. Let $K$ be a tamely ramified extension
of $\Q_l$ with ramification index $e$, given with a uniformiser, and let
$F : T_1 \to T_2$ be a surjection of good crystalline lattices for $G_K$.
Here *good* means that inertia acts through a set $\Sigma$ of tame characters
and the Hodge–Tate weights lie in a set $U$, with $N, \eta, H$ bounding
$|\Sigma|$, $|U|$ and the weights as in
[crystalline-period-bound-all-constant-ge-forty], and $l$ large. Let $P$ be
the largest period of the characters in $\Sigma$. Then every class in
$H^1_f(G_K, T_2)$, multiplied by $l^{7(NP + \eta(N + P))}$, lies in the image
of $H^1_f(G_K, T_1)$.
