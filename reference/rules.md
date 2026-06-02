# The rules, with worked examples

Each rule below shows the failure and the fix. The "broken" blocks are what
actually happens on a phone when you ignore the rule.

---

## R0 — Always fence

**Without a fence**, WhatsApp uses a proportional font. Spaces and letters have
different widths, so nothing lines up:

Name    Score
Ana   1240
Bruno 1110

(Notice how the columns already drift even here.)

**With a fence**, the font is monospace and the grid holds:

```
Name    Score
Ana      1240
Bruno    1110
```

Rule: if it's meant to align, it goes inside triple backticks. No exceptions.

---

## R1 — ≤ 26 columns

This is fine on desktop and **wraps into noise on an iPhone SE**, because the
line is 34 columns wide:

<!-- wascii-allow-wide -->
```
┌────────────────────────────────┐
│ this row is far too wide for a  │
└────────────────────────────────┘
```

Keep it to 26 and it survives the smallest screen:

```
┌────────────────────────┐
│ fits every phone       │
└────────────────────────┘
```

Total width = `┌` + 24 dashes + `┐` = **26**. Inner content ≤ 24.

---

## R2 + R6 — One cell per glyph; emoji outside

**Broken** — the 🏆 is two cells, so the right border on that row sits one column
off and the box looks bent:

```
┌────────────────────┐
│ 🏆 LEADERBOARD     │
├────────────────────┤
│ 1  ana       1240  │
└────────────────────┘
```

**Fixed** — emoji moves above the fence; inside stays pure single-cell:

🏆 *Leaderboard*
```
┌────────────────────┐
│ LEADERBOARD        │
├────────────────────┤
│ 1  ana       1240  │
└────────────────────┘
```

---

## R3 — Pad to a fixed inner width

**Broken** — rows padded by eye, right border ragged:

```
┌──────────────┐
│ build passing │
│ tests 128 │
└──────────────┘
```

**Fixed** — every inner line padded to the same 14 cells:

```
┌──────────────┐
│ build  pass  │
│ tests  128   │
└──────────────┘
```

---

## R4 — One border family

**Broken** — light top, double bottom; corners don't connect:

```
┌──────────────┐
│ mixed styles │
╚══════════════╝
```

**Fixed** — commit to one family (rounded here):

```
╭──────────────╮
│ one family   │
╰──────────────╯
```

---

## R5 — Spaces, never tabs

A single `\t` between columns renders at a different stop on every client. There
is no "broken" screenshot for this — it's broken differently everywhere. Always
expand to literal spaces before sending.

---

## R7 — Test narrow

Preview at the smallest bubble you support (iPhone SE). If the widest line is
≤ 26 and contains only single-cell glyphs, it will render identically on every
phone, tablet, and desktop. Shrinking is always the safe move.
