+++
kind = "proof"
of   = "thm-zero-free-from-families"
uses = ["thm-zero-free-from-connected", "thm-families-connected", "thm-auxiliary-fields",
        "thm-primitive-suffice"]
+++
Apply [thm-zero-free-from-connected] with windows of exponent
$\lambda = 3/2$. Its two hypotheses are slope data for the families, which
[thm-families-connected] gives, and auxiliary fields, which
[thm-auxiliary-fields] gives from the Tate–Shafarevich bound at each $\psi$.
[thm-primitive-suffice] passes from primitive characters to all.
