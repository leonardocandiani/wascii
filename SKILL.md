---
name: wascii
description: The art of ASCII for WhatsApp. Teaches an agent to render flawless monospace visuals — boxes, bars, charts, tables, leaderboards and title banners — inside WhatsApp chat bubbles without the alignment ever breaking. Codifies the unsafe-vs-safe Unicode set, the 26-column rule, the fenced-block requirement, and a gallery of copy-paste templates. Use whenever output is going to WhatsApp (or any monospace-capable chat) and you want structured visuals that actually line up on a phone.
---

# wascii — ASCII that survives WhatsApp

WhatsApp will render a perfectly aligned box on your desktop and shatter it on a
phone. The difference between art and garbage is a handful of rules about width,
fences, and which glyphs are exactly one cell wide. This skill encodes those
rules so the output lines up the first time, every time.

Apply this skill whenever you are about to send a structured visual — a box, a
table, a bar, a chart, a ranking, a titled header — to WhatsApp.

## The seven rules (non-negotiable)

**R0 — Always wrap it in a fenced code block.**
WhatsApp only monospaces text inside triple backticks. Outside the fence the font
is proportional and every column drifts. No fence → no alignment → no art. This is
rule zero because nothing else matters without it.

**R1 — Never exceed 26 characters per line.**
The narrowest mainstream iPhone (SE / mini) fits ~26 monospace glyphs in a bubble
before WhatsApp soft-wraps the line — and a wrap detonates the whole drawing. 26
is the bulletproof ceiling. ~30 survives on most modern phones; never assume more.
Count *visible glyphs*, not bytes.

**R2 — One glyph, one cell — or don't use it.**
Alignment only holds if every character occupies exactly one monospace cell.
Box-drawing (`─│┌┐`) and block elements (`█▓░`) are 1 cell. Emoji, CJK, and many
symbols are double-width or variable — they shove every following column out of
line. If a glyph isn't on the safe list in `reference/characters.md`, treat it as
unsafe.

**R3 — Pad every inner line to the same visible width.**
A box stays square only when each content line is padded with spaces to one fixed
inner width. Decide the inner width once, pad the rest to match, then the right
border lands in the same column on every row.

**R4 — Pick one border family and commit.**
Don't mix light (`┌─┐`), heavy (`┏━┓`) and double (`╔═╗`) corners in the same
frame — the junctions won't meet. Rounded (`╭─╮`) reads softest and is the house
style.

**R5 — Spaces only. No tabs.**
Tabs expand to different stops across clients. One stray tab ruins the grid.

**R6 — Emoji live outside the frame.**
Put them before or after the code block, or alone on a line — never inside a row
you need to align. An emoji inside a box is the single most common way ASCII
breaks on WhatsApp.

**R7 — Test on the narrowest target.**
If it survives an iPhone SE bubble, it survives everywhere. When in doubt, shrink.

## How to apply (the loop)

1. **Choose a template** from `examples/` that matches the data (box, table, bar,
   chart, leaderboard, banner).
2. **Set the inner width** ≤ 24 (so the frame total is ≤ 26 with both borders).
3. **Lay out the rows**, padding each to the inner width with spaces (R3).
4. **Audit every glyph** against `reference/characters.md` (R2). Strip emoji into
   the surrounding text (R6).
5. **Wrap in a fence** (R0) and **count the widest line** (R1). If any line > 26,
   shrink or restructure.
6. **Ship it.**

## Width accounting (the part everyone gets wrong)

The visible width of a row is the number of monospace cells it occupies, which is
**not** its byte length and **not** always its character count:

- Box-drawing and block glyphs are multi-byte in UTF-8 but **1 cell** each.
- A plain check `✓` (U+2713) is 1 cell; the emoji `✔️` (U+2714 + VS16) is 2 cells.
  Always use the text variant inside frames.
- Right-align numbers by left-padding with spaces, not by trailing the label.

A box `╭` + 24 dashes + `╮` is 26 cells wide — the maximum. Keep inner content to
24 and you never wrap.

## What NOT to do

- ❌ Don't send ASCII without a code fence "because it looked fine in the editor."
- ❌ Don't drop an emoji into a table cell to make it pop — it breaks the column.
- ❌ Don't build an 80-column terminal banner and hope it fits — it won't.
- ❌ Don't mix corner styles.
- ❌ Don't use tabs to align.

## Files

- `reference/characters.md` — the full safe/unsafe Unicode palette, grouped.
- `reference/rules.md` — the rules with worked before/after examples.
- `examples/boxes.md` — frames, cards, titled boxes.
- `examples/bars-and-charts.md` — progress bars, bar charts, sparklines.
- `examples/tables.md` — key/value and columnar tables.
- `examples/leaderboards.md` — rankings and stat blocks.
- `examples/titles-and-banners.md` — the art of titles and section headers.

Every drawing in this repo obeys its own rules: ≤ 26 columns, one border family,
zero emoji inside a frame. Copy them as-is and they will line up on a phone.
