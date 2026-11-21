+++
kind  = "theorem"
title = "Grothendieck's existence theorem"
lean  = ["GlobalTheory.Published.FormalAlgebraisation", "PositivityTheory.FormalThickening.formalAlgebraisation"]
order = 7
+++
Let $R$ be a noetherian ring, complete for the $I$-adic topology, and
$R_e = R/I^{e+1}$.

* (Morphisms.) Let $X$ be proper over $R$ and $Z$ separated of finite type
  over $R$. Every compatible family of morphisms $X \otimes R_e \to Z$ comes
  from a unique morphism $X \to Z$.
* (Schemes.) Let $Y_e$ be proper schemes over $R_e$ with
  $Y_{e+1} \otimes R_e \cong Y_e$, and $N_e$ compatible line bundles on them
  with $N_0$ ample. Then there is a proper scheme $X$ over $R$ with an ample
  line bundle $M$ such that $X \otimes R_e \cong Y_e$ and $M$ restricts to
  $N_e$, compatibly in $e$.

This is Grothendieck's existence theorem (EGA III, 5.1.4 and 5.4.5).
