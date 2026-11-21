# Levent Alpöge's proof of the Riemann Hypothesis: a reading blueprint

A blueprint, an informal mathematical account, of **Levent Alpöge's** proof
of the Riemann Hypothesis and of the Generalised Riemann Hypothesis for
Dirichlet $L$-functions. Alpöge announced the proof on 2026-11-20 at
<https://alpo.ge/remark.pdf>, together with a formal proof in Lean. This
blueprint follows the community mirror of that formal proof,
[leanprover-community/riemann-hypothesis](https://github.com/leanprover-community/riemann-hypothesis)
at commit `8c90877c` (pinned in `lakefile.toml`).

**Read it at <https://riemann.fuxi.merten.dev>.**

The announcement contains no mathematical exposition and the formal proof
has no comments, so everything here was reconstructed by reading the formal
statements. This is a reader's account of Alpöge's proof, not his own
exposition of it. Where
we could not tell what an object is, the text says so.

## Contents

461 statements in four chapters, each object one Markdown file with TOML
front matter under `blueprint/`:

1. **The main theorems.** The five theorems of the formal proof, and their
   reduction to a single statement: no Dirichlet $L$-function vanishes in
   $\Re s > \tfrac12$.
2. **Outline of the proof.** A sketch of the whole argument, refined down to
   detail. The directory tree under `blueprint/architecture/` is the
   refinement tree: a node's details sit inside its directory.
3. **Common foundations.** Results that both halves of the proof use.
4. **Published results.** The classical theorems the proof uses, each in the
   form proved in the formalisation, with a note wherever that form is a
   special case or weaker than the published theorem.

`blueprint/architecture/rem-points-to-check.md` lists the statements a reader
should check first.

The prose is mathematics: Lean appears only in the `lean = [...]` front
matter, which links each object to the formal declarations it stands for.

## How it was made

No build of the formal proof was used, because the project is too large to
build on the machine where this was written. Instead, a static analysis of
the source text (`tools/`) indexed all 1,051,598 declarations and resolved the
identifiers in each one. A declaration became a node when at least 1,000
other declarations of the proof can be reached only through it. The `uses`
edges are that reference graph reduced to the nodes.

Known limits:

* The `uses` edges come from resolving identifiers in source text. False
  matches through generic names were filtered out, but some edges are still
  wrong.
* A `lean` name may occasionally point at a different declaration than the
  one described. At least one node (`lem-local-lattice-counts-isometries`) was
  written from a declaration whose name the indexer mis-attributed.
* Every derived status reads *absent*, because no Lean facts were extracted.

Running `blueprint extract` against built oleans, then `blueprint check
--lean`, would confirm or correct the edges and names and fill in the
statuses (see below).

## Working with it

The [blueprint](https://github.com/chrisflav/blueprint) tool reads this
repository:

```
blueprint check  --root .        # structural checks
blueprint serve  --root .        # the website on localhost
blueprint site   --root .        # the static site in _site/
```

With the formal proof built (about 100 GB of disk and hours of CPU, or the
mirror's community build cache, with the trust caveats in its README):

```
lake exe blueprint extract       # lean-facts.json; imports all of Main, expect very high memory use
lake exe blueprint check --lean
```

`tools/README.md` describes the scripts that chose the nodes and edges.
`tools/writer-spec.md` and `tools/fix-spec-no-published-hypotheses.md` are the
writing briefs the text follows.

## Attribution

* **The proof, the formal proof and the announcement** are the work of
  **Levent Alpöge**, published at <https://alpo.ge/remark.pdf> and as the Lean
  archive linked there. The mathematics this blueprint describes is his. The
  formal proof
  was published without a license; this repository contains none of its
  source, only commentary on it and the names of its declarations.
* **The community mirror**
  [leanprover-community/riemann-hypothesis](https://github.com/leanprover-community/riemann-hypothesis)
  and its maintainers provided the source this blueprint was read from, and
  its verification notes (`verification/NOTES.md`), which the introduction
  draws on for the size of the source and its static scan.
* **The blueprint tool** [chrisflav/blueprint](https://github.com/chrisflav/blueprint)
  defines the format, checks it, and builds the website.
* **[Mathlib](https://github.com/leanprover-community/mathlib4)** and
  **[Lean](https://lean-lang.org)** underlie the formal proof. The statements
  of the main theorems use Mathlib's definitions of $\zeta$, Dirichlet
  $L$-functions and the Riemann Hypothesis.
* **The classical results** in the published-results chapter are attributed
  to their authors in the text of each node.

A node here says nothing about whether the formal proof of it is correct.
That question belongs to the independent kernel checks described in the
mirror's verification notes.
