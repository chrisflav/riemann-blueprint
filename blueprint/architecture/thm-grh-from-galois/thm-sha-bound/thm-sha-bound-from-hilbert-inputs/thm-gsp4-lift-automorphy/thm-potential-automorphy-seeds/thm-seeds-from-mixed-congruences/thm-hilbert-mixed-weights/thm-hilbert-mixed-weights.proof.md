+++
kind = "proof"
of   = "thm-hilbert-mixed-weights"
uses = ["thm-borel-casselman", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-geometric-lemma-filtration", "thm-hilbert-weight-change",
        "thm-jacquet-irreducible-admissible", "thm-local-parameters-exist"]
+++
An Eisenstein congruence gives a cusp form of parallel weight $k + 1$
congruent to an Eisenstein series, hence with residual representation
$1 \oplus \xi$. Weight change ([thm-hilbert-weight-change]) raises the weight by $2t$ at the
embeddings belonging to $P$ while keeping the congruence and ordinarity.
The Galois representation of the result, from the inputs for Hilbert
modular forms and [local parameters](@thm-local-parameters-exist), has the
stated local shape; [Chebotarev's theorem](@thm-chebotarev-degree-one-frobenius) and the irreducibility of
the residual characters give the open image.
