+++
kind  = "lemma"
title = "Minimal compactification and boundary separation for unitary varieties"
provenance = "new"
lean  = ["GlobalTheory.T.unitaryToroidalSeparation_of_base", "GlobalTheory.UChart.UStB", "GlobalTheory.UPoincTop.uPoinStX_sep", "GlobalTheory.UPoincTop.uStB"]
order = 10
+++
In the situation of [thm-toroidal-compactification-unitary] there are:

* a minimal compactification $Z$ of $X$, projective and normal over $F$,
  with an ample line bundle that pulls back to $\omega^N$ on every toroidal
  model, and such that every semi-abelian degeneration of the universal
  abelian scheme over a complete normal local base extends to a map into
  $Z$;
* the normalised blow-up $S \to Z$ along an ideal supported on the boundary
  with the valuations of $\varphi$, on which $\omega^k(-\Delta)$ is ample for
  large $k$;

such that the boundary of $S$ *separates Mumford families*: two Mumford
families through the same point of $S$, with the same cone, give the same
point of every geometric fibre.
