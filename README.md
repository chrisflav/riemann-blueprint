# The Riemann Hypothesis formalisation: a reading blueprint

An informal blueprint of
[leanprover-community/riemann-hypothesis](https://github.com/leanprover-community/riemann-hypothesis),
the mirror of the Lean formalisation announced on 2026-11-20 that claims a
proof of the Riemann Hypothesis and of GRH for Dirichlet $L$-functions. It is
kept with the [blueprint](https://github.com/chrisflav/blueprint) tool: each
object is one Markdown file with TOML front matter under `blueprint/`.

The source has no comments and the announcement no mathematics, so the prose
here was reconstructed from the Lean statements. The nodes and `uses` edges
come from a static analysis of the source text, not from a build (see
`blueprint/intro.md` and `tools/`). Treat edges as approximate until
`blueprint extract` has been run against built oleans.

Pinned to mirror commit `8c90877c` (`lakefile.toml`).

## Contents

461 statements in four chapters: the main theorems, an outline of the proof
refined from sketch to detail (the directory tree under `blueprint/` is the
refinement tree), common foundations, and the published results the proof
uses. `blueprint/architecture/rem-points-to-check.md` lists the statements a
reader should check first.

Known limits of the static analysis:

* `uses` edges come from resolving identifiers in source text. False matches
  through generic names were filtered, but some edges are still wrong.
* A `lean` name may occasionally point at a different declaration than the
  one described: at least one node (`lem-local-lattice-counts-isometries`)
  was written from a declaration whose name the indexer mis-attributed.
  `blueprint check --lean` after an `extract` will report such cases.

## Working locally

Without the project built (what this repository was made with):

```
lake exe blueprint check        # structural checks
lake exe blueprint serve        # the site on localhost; every status reads "absent"
```

With the project built — about 100 GB of disk and hours of CPU, or use the
mirror's community cache (`lake exe cache get` inside `.lake/packages/tree`,
see its README for the trust caveats):

```
lake exe blueprint extract      # lean-facts.json; imports all of Main, so expect very high memory use
lake exe blueprint check --lean # missing names, declared-vs-actual uses
lake exe blueprint serve
```

## Regenerating the node selection

`tools/` holds the scripts that chose the nodes and computed the edges:
`index.py` (declaration index and reference graph over all `.lean` files),
`clean.py` (drops junk root-level names), `analyse.py` (closure from `Main`), `dom.py` (dominator tree, needs
`networkx`), `selectnodes.py` (node selection, abstracted `uses`) and `gen.py`
(per-chapter packets), `style-scan.py` (checks prose for Lean names and jargon). They read the mirror's `src/` and do not need Lean.
