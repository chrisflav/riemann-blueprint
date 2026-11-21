# Fix brief: no published results as hypotheses

The blueprint at /home/christian/riemann-hypothesis-blueprint/blueprint/ follows the formal
proof's hypothesis structure too faithfully. The formal proof threads published results
through its theorems as hypotheses ("Assume global Artin reciprocity, local Tate duality, …").
In a mathematical exposition that is confusing: a published theorem is simply true, and it is
*used in a proof*, not *assumed in a statement*.

The style rules of /home/christian/.claude/jobs/61974794/tmp/writer-spec.md still hold: Orwell,
no Lean in prose, links point to mathematical objects. Read it if you have not.

## The rule

1. **Never state a published or classical result as a hypothesis of a theorem.** Remove
   "Assume X", "Suppose X holds", "Given X", "Under the hypotheses of …", "If the published
   results … hold" and similar, wherever X is a known result: anything in
   `blueprint/chap-literature/`, or any classical theorem (Artin reciprocity, Chebotarev,
   Tate duality, Siegel–Weil, Howe duality, Bernstein–Zelevinsky, Harish-Chandra, Kato, …).
   State the theorem unconditionally. Mention the published result in the **proof** file
   instead ("By local Tate duality [thm-…] …").
2. **Hypotheses that are results proved elsewhere in the GRH argument may stay**, but only when
   they make the structure clearer: for example "If polarized pairs have Galois
   representations, then …" in the outline chapter. Where a hypothesis is an internal result
   that is simply proved elsewhere, prefer to state the theorem unconditionally and cite the
   internal result in the proof as well.
3. **Bundles.** Some nodes are nothing but a bundle of results ("the published inputs", "the
   local representation theory package", "the hypotheses on the members follow from the
   published inputs"). Do not present a bundle as a hypothesis or as a definition of
   anything. Rewrite such a node as `kind = "remark"` (keep its `lean` list, drop `uses` from
   its statement) whose body says in one or two sentences which results are used together and
   where, with links. If a "theorem" only says "the published results imply the bundle", it is
   also a remark of that kind. A remark has no proof file: delete its `.proof.md` if it has
   one, after moving any `uses` you want to keep into a sentence of the remark.
4. **Hypotheses that genuinely belong to the statement stay**: conditions on the objects
   (a prime $l > C$, a CM field, a regular algebraic representation), and quantitative
   inputs that are part of what the statement says. When in doubt, ask whether a reader would
   think the hypothesis could fail. A published theorem cannot fail; drop it.
5. Statement `uses` must not list published theorems (a script has already moved them into the
   proof files; do not move them back). Proof `uses` should list what the proof uses.
   Statement `uses` may list definitions needed to state the result.
6. Some proof files contain only the placeholder `TODO-PROOF`. They were created to receive the
   moved `uses`. Replace the placeholder with 1–5 sentences saying how the proof goes, naming
   the results in its `uses` with links. Read the formal statement if you need to (the `lean`
   names are in the statement's front matter; locate them with
   `rg -n -g '*.lean' '<last component of the name>' /home/christian/riemann-hypothesis/src`,
   read-only).

Also apply the same thinking to the proof files of the nodes you edit: a proof should say
"by X" rather than "X is a hypothesis, so".

Keep each node's mathematical content, ids, `lean` lists, titles (unless a title says "under
published hypotheses" or similar) and file locations. Do not touch files outside your list
except the proof files belonging to statements in your list.

## Checking

Run `/home/christian/.claude/jobs/61974794/tmp/bp/.lake/build/bin/blueprint check --root /home/christian/riemann-hypothesis-blueprint`
when done and fix anything in your files. Then `grep -n 'TODO-PROOF'` over your directories and
over your files: none may remain. Other writers are editing other files at the same time;
ignore their errors.

## Report

Under 300 words: files changed, nodes turned into remarks, any hypothesis you kept and why,
anything you could not resolve.
