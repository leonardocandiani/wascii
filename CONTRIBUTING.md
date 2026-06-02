# Contributing to wascii

Thanks for wanting to add to the gallery. There's one hard rule and a couple of
soft ones.

## The hard rule

**Every drawing must obey its own rules.** A template that breaks on a phone is
worse than no template. Before you open a PR:

- ✅ Every line is **≤ 26 cells** wide (run the checker, below).
- ✅ **One border family** per frame — don't mix `┌`, `┏` and `╔`.
- ✅ **Zero emoji inside a frame.** Captions and emoji go *outside* the fence.
- ✅ Single-cell glyphs only inside aligned regions (see
  [`reference/characters.md`](reference/characters.md)).

The CI runs `scripts/check-width.py` and will reject any bare fenced block over
26 cells. Run it locally first:

```bash
python3 scripts/check-width.py
```

A deliberate counter-example (a "this is what breaks" block) may exceed the
limit only if the line `<!-- wascii-allow-wide -->` sits directly above its
opening fence.

## Soft rules

- Keep examples **realistic** — things people actually send: deploys, sales,
  rankings, standups, budgets.
- Prefer **rounded** corners (`╭─╮`) for the house style unless the example is
  specifically about another family.
- One template = one idea. Don't cram five layouts into one block.

## Adding an example

1. Find the right file in [`examples/`](examples) (boxes, tables, bars,
   leaderboards, titles).
2. Add your block with a short `##` heading and, if useful, a one-line note on
   the technique.
3. Run the checker.
4. Open a PR describing what the template is for.

## Reporting a glyph that breaks

If you find a character that renders double-width on some client and single on
others, open an issue with the codepoint and a screenshot. Cross-client glyph
intel is gold.
