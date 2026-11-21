# Spec for writing blueprint chapters

You are writing part of a blueprint: a **mathematical exposition** of the proof that a large
Lean formalisation gives for the Riemann Hypothesis and GRH for Dirichlet L-functions. The
formalisation is at `<mirror>/src`. It is READ ONLY: never build it,
never run lake or lean in it, never modify it. It has 175k files and no comments, so the
mathematics has to be reconstructed from statements and names. The blueprint lives at
`./blueprint/` and uses the chrisflav/blueprint tool.

Read first, as the model for voice and format:
- `blueprint/main-theorems/` and `blueprint/architecture/` (all files): the hand-written top
  layers of the proof.

## The three rules of this blueprint

1. **The prose is mathematics, not Lean.** A reader who has never seen Lean must be able to
   read every body. Never write a Lean name, a declaration, a file, a namespace, a tactic, a
   "field of a structure", or words like "the Lean", "the source", "formalised", "the
   record", "Prop" in a body or title. The connection to Lean lives only in the `lean = [...]`
   front matter. Lean coinages are not mathematical names either: where the formalisation
   calls something a "row", "window", "host", "box" or "page", find what the object is and
   name it mathematically (a "Galois representation attached to π", "a bound on
   Tate–Shafarevich groups", "an auxiliary CM field"). If an object has no standard name,
   define it in words in a definition node and give it a plain name.
2. **References point at mathematical objects.** Cross-reference with `[id]` or quiet links
   `[the Siegel–Weil formula](@id)` to the node that states or defines the thing. Write
   "by the Siegel–Weil formula [id]", never "by `siegelWeil_holds`".
3. **Sketch to detail.** The blueprint is layered. The first chapters give a sketch of the
   whole argument, and every node you write *refines* a coarser node: the one your packet
   gives as `parent`. A refining node supplies a step of its parent's proof, so its
   statement should read as a step of that proof. The parent's proof should still be
   understandable without it. The refinement tree is the logical structure of the
   blueprint, and **the directory tree is the refinement tree** (see Layout).

## Style: George Orwell, "Politics and the English Language"

Follow his six rules, read as a mathematician would:

1. Never use a metaphor, simile or other figure of speech which you are used to seeing in
   print. (No "lies at the heart of", "plays a key role", "the heavy lifting", "machinery".)
2. Never use a long word where a short one will do. ("use", not "utilise"; "shows", not
   "establishes the validity of".)
3. If it is possible to cut a word out, always cut it out.
4. Never use the passive where you can use the active. ("Landau's theorem gives…", not "It is
   obtained by an application of…". The mathematical "we" is fine.)
5. Never use a foreign phrase, a scientific word or a jargon word if you can think of an
   everyday English equivalent. Standard mathematical terms are the everyday words of this
   subject and are right; invented jargon and Lean names are not.
6. Break any of these rules sooner than say anything outright barbarous.

Before each paragraph ask his questions: What am I trying to say? What words will express it?
Could I put it more shortly? Have I said anything that is avoidably ugly? Avoid his four faults:
dying metaphors, verbal false limbs ("serves to", "makes contact with", "gives rise to" where
"gives" will do), pretentious diction, and meaningless words ("fundamental", "crucial",
"deep", "powerful", "natural" used as praise).

Honesty over fluency: state what the formalisation proves, no more. Name a classical theorem
when the statement matches (who, roughly when) and say plainly when the statement proved is
a special or weakened form. Where you cannot tell what an object is, say so in one plain
sentence, starting "*It is not clear*" or "*We read this as*". Never invent mathematics to fill
a gap.

## Your input

A JSON packet (path given in your task) listing the nodes of your chapter. Per node:
`id` (fixed, use exactly), `lean` (fixed list of Lean names for the front matter; use exactly,
don't add or drop), `kinds` (Lean declaration kind per name), `file`, `line` (1-based, relative
to `src/`), `size` (how many declarations this node dominates in the use graph: a measure of
how much of the proof sits under it), `signature` (start of the statement), `uses` (ids its
STATEMENT needs), `proof_uses` (ids its PROOF needs), `parent` (the node it refines; may be an
id from another chapter).

The edges come from a static text analysis, not from Lean. Keep them as given. You may drop an
edge only if you are sure name resolution produced it by mistake; list such drops in your
report.

## What to write

For every node, `<id>.md`:

```
+++
kind    = "theorem"          # theorem | lemma | proposition | corollary | definition
title   = "Short mathematical title"
lean    = ["Exact.Lean.Name", ...]
uses    = ["id-a", "id-b"]   # the packet's `uses`; omit the key if empty
order   = 7                  # position among the nodes refining the same parent
+++
The statement, in mathematical language, LaTeX in $...$ / $$...$$.
```

and, for anything with a proof, `<id>.proof.md`:

```
+++
kind = "proof"
of   = "<id>"
uses = ["id-c"]              # the packet's `proof_uses`; omit if empty
+++
How the proof goes: which results it combines and in what order, in 1–8 sentences.
```

Kinds: a statement proved by the formalisation is a `theorem`, `proposition` or `lemma` by
weight; a result from the classical literature is a `theorem` titled with its classical name
("Jacquet–Shalika rigidity"); a genuine definition of an object is a `definition` with no
proof file.

To understand a node, open its `file` at `line` (use `grep -v '^import'`; the import blocks
are huge), read the statement, and unfold the definitions it mentions. Locate them with
`rg -n -g '*.lean' '^(def|abbrev|structure|class|theorem|lemma) <Name>\b' <mirror>/src`,
and remember that names may sit inside `namespace` blocks. Spend effort in proportion to `size`.

Statements: usually 2–10 lines; long only where the mathematics needs it. LaTeX: inline
`$...$`, display `$$ ... $$` on their own lines, no blank lines inside display maths. KaTeX
macros available: \C \R \Q \Z \N \A \GL \U \Gal \Re \Im \Qlbar \Qbar \Fq \Qp \Ql \rec. No `+++`
inside bodies. Avoid backslashes in TOML titles.

## Layout

The directory tree is the refinement tree, as in `blueprint/architecture/`:

- A node with no refining children is a file `<id>.md`, with its proof in `<id>.proof.md`
  next to it.
- A node with refining children is a directory `<id>/`. The node itself is
  `<id>/_section.md`, with an explicit `id = "<id>"` and its real `kind`, for example
  "theorem". Its proof is `<id>/<id>.proof.md`, and its children are the other files and
  directories inside it. Files in a directory refine its `_section.md` automatically, so
  never write a `refines` key yourself.
- Your task names the directory of each top-level parent. Every node whose `parent` is that
  node goes inside that directory, and so on down the tree. The parents in your packet
  determine exactly where every file goes.
- Use `order` to order siblings, so that what a node uses comes before it where possible.
- Do not add section headings inside the tree. Where a parent has many children (more than
  about twelve), you may group them under a `kind = "section"` directory with a 2–4 sentence
  `_section.md` introduction. Do this only when the grouping is mathematically clear.

## Checking

Run the tool on the whole blueprint before finishing:

```
blueprint check --root .
```

Fix every error and warning that concerns your files (`dangling-ref`, `bad-link`, parse
failures, cycles). `info` level lints are fine. Other chapters are being written in parallel:
ignore their errors and never touch their files. Then grep your own bodies for backticks and
for "Lean" and remove what you find.

## Final report

Return, in under 600 words: the number of files written, the section structure, the nodes you
found opaque, any edges you dropped and why, and anything striking. For example: a classical
result whose proved statement is much weaker than the classical theorem, or a statement that
looks vacuous or suspicious.

## Ids

The packet ids were made from Lean names (`all-rows-of-open0-alt`), so they are not good
mathematical ids. Write your files with the packet ids exactly, because other writers link to
them. In your final report, add a JSON object mapping each of your packet ids to a short
mathematical id (`thm-howe-duality-unramified`, `def-hermitian-lattice-slopes`; lower case,
`a-z0-9-`, prefixed `thm-`/`lem-`/`prop-`/`def-`/`cor-`). The renames are applied centrally
afterwards. Only nodes you wrote; ids unique.

Links to ids of other writers (any id in `tools/packets/w-*.json`)
are fine even though those files may not exist yet; `dangling-ref`/`bad-link` reports for them
are expected while the others work. To learn what such a node is, read its entry in the packet
files (`lean`, `signature`, `file`).
