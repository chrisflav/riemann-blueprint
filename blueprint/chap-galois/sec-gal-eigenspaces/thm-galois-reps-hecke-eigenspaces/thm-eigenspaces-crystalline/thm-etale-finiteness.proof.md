+++
kind = "proof"
of   = "thm-etale-finiteness"
uses = ["thm-additive-characteristic-classes", "thm-projective-bundle-formula",
        "thm-proper-base-change"]
+++
The proof follows the classical route of SGA 4. It computes the cohomology of
curves with the Kummer sequence and the Picard group of a normal proper model,
kills cohomology classes by finite covers, and compares filtrations in a
spectral sequence; *we read* the passage to higher dimension as fibring by
curves. Along the way it uses about twenty-five basic statements of étale
cohomology. Among them are the projective bundle formula
[thm-projective-bundle-formula], the additive characteristic classes of
[thm-additive-characteristic-classes] and proper base change
[thm-proper-base-change], all proved in this blueprint, together with
Mayer–Vietoris sequences, homotopy invariance, the bound $1$ on the
cohomological dimension of smooth affine curves, and the identification of
the étale cohomology of a field with Galois cohomology. We have not checked
each of the others.
