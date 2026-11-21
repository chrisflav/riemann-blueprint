+++
kind  = "theorem"
title = "Holomorphic discrete series are lowest weight modules"
source = "Harish-Chandra [harish-chandra-1955], [harish-chandra-1956]"
lean  = ["GlobalTheory.HolDS.holomorphicDiscreteSeries_holds", "GlobalTheory.Published.HolomorphicDiscreteSeries"]
order = 14
+++
Let $G = \U(p,q)$ and $\lambda$ a Harish-Chandra parameter in the
holomorphic chamber: $\lambda_b < \lambda_a$ whenever $a$ is a positive and
$b$ a negative index of the signature. Let $\mathfrak p^\pm$ be the
holomorphic and antiholomorphic parts of the complexified tangent space.
Every discrete series representation $\sigma$ with parameter $\lambda$ is a
lowest weight module:

* every $K$-type is the lowest $K$-type plus a sum of roots of
  $\mathfrak p^+$;
* $K$-finite vectors are smooth, and $\mathfrak p^-$ kills the lowest
  $K$-type;
* the $K$-finite vectors are exactly the span of the raising operators
  from $\mathfrak p^+$ applied to the lowest $K$-type.
