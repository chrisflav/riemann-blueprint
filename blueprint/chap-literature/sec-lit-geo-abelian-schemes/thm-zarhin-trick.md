+++
kind  = "theorem"
title = "Zarhin's trick"
lean  = ["GlobalTheory.CompanionTheory.Ar.GR.ZarhinStatement", "PositivityTheory.HtPt.Narrow.zarhin"]
uses  = ["thm-dual-abelian-scheme"]
order = 3
+++
Let $R$ be the valuation ring of a valuation on an algebraically closed
field, and $A$ an abelian scheme over $R$ with a relatively ample line
bundle. Then $A$ is a direct factor of a principally polarised abelian
scheme $P$ over $R$: there are homomorphisms $i : A \to P$ and $r : P \to A$
with $r \circ i = \mathrm{id}_A$.

This is Zarhin's trick (1975): one may take $P = (A \times A^\vee)^4$. We
derive it from the existence of dual abelian schemes
([thm-dual-abelian-scheme]).
