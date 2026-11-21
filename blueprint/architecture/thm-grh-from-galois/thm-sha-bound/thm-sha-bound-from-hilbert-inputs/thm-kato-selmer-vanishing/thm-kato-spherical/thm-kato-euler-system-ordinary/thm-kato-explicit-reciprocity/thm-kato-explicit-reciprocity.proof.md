+++
kind = "proof"
of   = "thm-kato-explicit-reciprocity"
uses = ["thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-reciprocity-fixed-exponent"]
+++
*We read* the proof as follows. The law for zeta classes of a fixed exponent ([thm-reciprocity-fixed-exponent]) gives the image of each
$Y_r$ up to an error that does not depend on $d_0$. Smoothing by
$1 - d_0\langle d_0\rangle$ removes that error and produces the factor
$1 - d_0\psi^{-1}(d_0)$; summing over the diamond operators gives the Gauss
sum $\sum_a \psi(a)z^a$. [Chebotarev's theorem](@thm-chebotarev-degree-one-frobenius) supplies the Frobenius
elements used to compare the two sides.
