+++
kind = "proof"
of   = "mix-seed-of-alt"
uses = ["borel-casselman", "cheb", "chebotarev-degree-one", "geometric-lemma-filtration", "hol-wc",
        "irreducible-admissible-gl", "thm-local-parameters-exist"]
+++
An Eisenstein congruence gives a cusp form of parallel weight $k + 1$
congruent to an Eisenstein series, hence with residual representation
$1 \oplus \xi$. Weight change ([hol-wc]) raises the weight by $2t$ at the
embeddings belonging to $P$ while keeping the congruence and ordinarity.
The Galois representation of the result, from the inputs for Hilbert
modular forms and [local parameters](@thm-local-parameters-exist), has the
stated local shape; [Chebotarev's theorem](@cheb) and the irreducibility of
the residual characters give the open image.
