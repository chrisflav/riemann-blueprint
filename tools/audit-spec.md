# Brief: fill the gaps the automatic node selection left

The blueprint (worktree /home/christian/riemann-hypothesis-blueprint/.claude/worktrees/github-publish,
edit files there) describes Levent Alpöge's Lean proof of RH/GRH, read-only at
/home/christian/riemann-hypothesis/src (never build or modify it). Its nodes were chosen
automatically: declarations that DOMINATE at least 1000 others in the reference graph. That
criterion misses (a) the central *definitions* every step uses, and (b) mechanisms that many
independent steps share. Your job is to find crucial missing content in your scope, decide
whether it is crucial, and add it.

Read first: tools/writer-spec.md (style: Orwell; no Lean in prose; links point at mathematical
objects; sketch to detail, directory tree = refinement tree), tools/fix-spec-no-published-hypotheses.md
(never state a published result as a hypothesis), and look at blueprint/architecture/ to see the
current outline. Front matter additionally carries:
- `provenance = "new" | "published" | "modified"` (required on every statement you write:
  new = no published counterpart you can identify; published = a published theorem/definition as
  published; modified = special/weakened/variant form),
- `source = "..."` for published/modified ones (citations `[ref-id]` to files in
  blueprint/references/; the index is /home/christian/.claude/jobs/61974794/tmp/references-index.txt;
  add an entry file if needed; never invent locators, pages, volumes or DOIs).

## Data you can use

- /home/christian/.claude/jobs/61974794/tmp/audit-candidates.json: unmapped declarations of the
  proof, ranked by how many source areas use them (`areas`), total uses, uses in statements,
  dominated subtree size, statement start.
- /home/christian/.claude/jobs/61974794/tmp/audit-keywords.json: declarations whose names contain
  concepts the announcement names (Stepanov, Seesaw, Bessel, GGP, Iwasawa, Mangoldt, Parseval,
  Chowla–Selberg, Behrend, Bertini, iterated lifts, Rallis…) — (dominated size, uses, mapped?, name).
- The index pickle /home/christian/.claude/jobs/61974794/tmp/full.pkl (python3 via `nix shell
  nixpkgs#python3 -c python3 …`): keys names, index (file idx, 0-based line, kind), deps,
  stmt_deps, sig, files. /home/christian/.claude/jobs/61974794/tmp/ana.pkl has `closure` (decls on
  the proof path). Use it to ask "who uses X", "what does X use".
- `rg -n -g '*.lean' …` in the source; `grep -v '^import'` when reading files.

## What to add

A node for something that a reader of the proof must know to follow it: a central object, a
statement that several steps rest on, or a mechanism the announcement names that is on the proof
path. Not: utility lemmas, coercions, notation, bookkeeping. Be selective: prefer 15 good nodes to
60 thin ones. For each node:
- place it where it belongs in the refinement tree (a definition goes inside the node whose proof
  first needs it, or in the chapter/section where it is first used); convert a file node into a
  directory node (`<id>/_section.md` with explicit `id`) if it gains children, keeping its proof
  file as `<id>/<id>.proof.md`;
- `lean = [...]` exact names (check each exists in the index);
- `uses` for statement dependencies, proof `uses` for proof dependencies, among existing node ids;
- link it from the existing nodes that use it: edit their prose minimally (a `[id]` or quiet link
  `[words](@id)` where the object is mentioned) and add it to their `uses` if they need it.

Other writers work in parallel on other scopes. Edit existing files with small, targeted
replacements and re-read a file right before editing it; never rewrite a whole existing file.

## Checking and report

Run `/home/christian/.claude/jobs/61974794/tmp/bp/.lake/build/bin/blueprint check --root /home/christian/riemann-hypothesis-blueprint/.claude/worktrees/github-publish`
and fix your errors/warnings (others' in-progress errors: ignore). Grep your new bodies for
backticks and "Lean". Do not commit.

Report (under 500 words): nodes added (id, title, provenance, where placed, why crucial), existing
nodes edited, candidates you examined and rejected (and why), anything the blueprint gets wrong
that you noticed.
