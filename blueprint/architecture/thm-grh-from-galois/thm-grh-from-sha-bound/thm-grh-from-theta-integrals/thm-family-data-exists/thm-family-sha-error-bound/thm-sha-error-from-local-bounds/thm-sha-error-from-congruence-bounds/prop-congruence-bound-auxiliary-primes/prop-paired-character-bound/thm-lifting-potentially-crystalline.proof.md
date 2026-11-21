+++
kind = "proof"
of   = "thm-lifting-potentially-crystalline"
uses = ["lem-lifting-crystalline-lattices", "thm-bhatt-scholze-coefficients", "thm-bhatt-scholze-crystalline-lattices", "thm-bloch-kato-local", "thm-fontaine-bcris", "thm-tate-euler-characteristic-l-adic", "thm-tate-local-duality-l-adic"]
+++
Reduce to the crystalline case over the field cut out by $\Sigma$ and apply
[lem-lifting-crystalline-lattices]. The reduction uses
[Fontaine's period ring](@thm-fontaine-bcris), the theorem of Bhatt and
Scholze [thm-bhatt-scholze-crystalline-lattices], the
[local theory of Bloch and Kato](@thm-bloch-kato-local),
[local Tate duality](@thm-tate-local-duality-l-adic) and the
[local Euler characteristic formula](@thm-tate-euler-characteristic-l-adic).
