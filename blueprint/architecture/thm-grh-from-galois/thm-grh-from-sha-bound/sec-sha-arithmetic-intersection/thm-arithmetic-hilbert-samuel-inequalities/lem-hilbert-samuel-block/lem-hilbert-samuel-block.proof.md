+++
kind = "proof"
of   = "lem-hilbert-samuel-block"
uses = ["lem-flag-cover-pullback", "lem-hilbert-samuel-block-assembly", "thm-arithmetic-intersection-theory", "thm-hironaka-resolution"]
+++
By [lem-hilbert-samuel-block-assembly] it suffices to check its list of statements about blocks:
finiteness of the modules involved, the Hilbert function of each piece,
compatibility with changes of model and graphs, the degree of
resolutions and their images, and integrability at points. Each is proved,
mostly by flag covers ([lem-flag-cover-pullback]), using resolution in
projective space ([thm-hironaka-resolution]) and the properties of
arithmetic intersection numbers ([thm-arithmetic-intersection-theory]).
