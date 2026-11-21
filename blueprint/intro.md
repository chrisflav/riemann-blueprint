+++
kind  = "matter"
title = "About this blueprint"
order = 0
+++
This blueprint sets out Levent Alpöge's proof of the Riemann Hypothesis, and
of the Generalised Riemann Hypothesis for Dirichlet $L$-functions. Alpöge
announced the proof on 20 November 2026 [alpoge-2026], together with a
formal proof in Lean. The proof and its formalisation are his work. This
blueprint follows the
community mirror of the formal proof,
[leanprover-community/riemann-hypothesis](https://github.com/leanprover-community/riemann-hypothesis),
at commit `8c90877c`.

The announcement gives no mathematical account of the proof, and the
formal proof has no comments: it runs to 175,187 files and about 15.5
million lines, with 818,755 theorems. Everything here was reconstructed from
the formal statements. So this blueprint is a reader's account of
Alpöge's proof, not his own exposition of it. Where we could not tell what an object is, we say so.

The blueprint runs from sketch to detail. [main-theorems] states the
theorems and reduces them to one statement, [thm-half-plane].
[architecture] outlines its proof, and every later node refines the step of
the proof it belongs to. [chap-foundations] collects results that both
halves of the proof use, and [chap-literature] the published results.

We chose the nodes by the structure of the formal proof. A result is a node
when at least 1000 other results of the proof can be reached only through it.
Each node links to the formal statements it stands for, and its uses list
what those statements refer to. No build of the formal proof was used to
make the blueprint, so the uses come from reading the source and are
approximate. Statuses read *absent* until the formal proof is built and
checked against the blueprint.

A node in this blueprint says nothing about whether the formal proof of it
is correct. That question belongs to the independent kernel checks described
in the mirror's verification notes.

*Credits.* The proof, the formal proof and the announcement are the work of
Levent Alpöge. We read the proof from the community mirror and draw on its
verification notes. The blueprint tool by [@chrisflav](https://github.com/chrisflav)
builds this site. The sources are at
<https://github.com/chrisflav/riemann-blueprint>.
