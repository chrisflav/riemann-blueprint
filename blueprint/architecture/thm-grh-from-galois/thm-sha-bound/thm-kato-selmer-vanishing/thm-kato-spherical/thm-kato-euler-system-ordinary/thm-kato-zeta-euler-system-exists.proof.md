+++
kind = "proof"
of   = "thm-kato-zeta-euler-system-exists"
uses = ["thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one"]
+++
Glue the two hypotheses. Build the tower of modular curves with its
ordinary Eisenstein eigenfunctional and choose a measure on
$(\Z/l^r)^\times$; smooth the zeta classes by $1 - d_0\langle d_0\rangle$;
average over Frobenius elements, which [Chebotarev's theorem](@thm-chebotarev-degree-one-frobenius) supplies;
and compare the resulting values with the reciprocity law term by term. The
admissible Hecke operators act on both sides through the eigenvalues of $g$.
