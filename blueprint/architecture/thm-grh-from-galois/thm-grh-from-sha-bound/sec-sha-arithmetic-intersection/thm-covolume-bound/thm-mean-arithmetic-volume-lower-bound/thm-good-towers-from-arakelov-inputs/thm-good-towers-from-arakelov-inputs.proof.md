+++
kind = "proof"
of   = "thm-good-towers-from-arakelov-inputs"
uses = ["thm-abelian-variety-torsion-count", "lem-volume-theorem-inputs", "lem-flag-cover-pullback", "thm-good-towers-volume-theorem"]
+++
The assumptions give the inputs of [lem-volume-theorem-inputs], hence its
package of inputs. Resolution gives integrability of Green functions at
points, prime avoidance gives sections avoiding finitely many primes, and
the theta functions of abelian varieties are uniform. Then apply
[thm-good-towers-volume-theorem], using multiplication by $n$ on abelian schemes
and flag covers ([lem-flag-cover-pullback]).
