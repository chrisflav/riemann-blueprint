# Node selection tools

Static analysis of the formal proof's source text, no Lean needed. Run from a scratch
directory, with `SRC` the mirror's `src/`:

```
python3 index.py $SRC full.pkl     # declaration index + reference graph (~40 min, ~4 GB RAM)
python3 clean.py                   # drop references to junk root-level names
python3 analyse.py full.pkl ana.pkl   # closure from Main's theorems
python3 dom.py > dom.txt           # dominator tree (needs networkx)
python3 select.py                  # nodes dominating >= 1000 declarations, abstracted uses
python3 gen.py                     # per-chapter packets; reads lean names already in ../blueprint
```

`writer-spec.md` is the brief the chapter writers followed.
