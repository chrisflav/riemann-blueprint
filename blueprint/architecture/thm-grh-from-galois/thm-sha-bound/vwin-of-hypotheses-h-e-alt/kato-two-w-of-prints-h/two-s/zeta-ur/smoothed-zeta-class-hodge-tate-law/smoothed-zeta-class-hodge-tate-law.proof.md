+++
kind = "proof"
of   = "smoothed-zeta-class-hodge-tate-law"
uses = ["cheb", "chebotarev-degree-one", "hco"]
+++
*We read* the proof as follows. The law for zeta classes of a fixed exponent ([hco]) gives the image of each
$Y_r$ up to an error that does not depend on $d_0$. Smoothing by
$1 - d_0\langle d_0\rangle$ removes that error and produces the factor
$1 - d_0\psi^{-1}(d_0)$; summing over the diamond operators gives the Gauss
sum $\sum_a \psi(a)z^a$. [Chebotarev's theorem](@cheb) supplies the Frobenius
elements used to compare the two sides.
