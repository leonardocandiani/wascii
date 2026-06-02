# Character palette

Every glyph here is grouped by whether it occupies **exactly one monospace cell**
in WhatsApp's chat font. Single-cell glyphs are safe to align with. Anything in
the "unsafe" section will drift your columns.

> Rule of thumb: if it's a box-drawing or block-element codepoint, it's 1 cell.
> If it's an emoji (or a symbol with an emoji-presentation variant), it's 2 cells.

---

## ✅ Safe — single cell

**Light box-drawing**
```
┌ ┐ └ ┘ ─ │ ├ ┤ ┬ ┴ ┼
```

**Heavy box-drawing**
```
┏ ┓ ┗ ┛ ━ ┃ ┣ ┫ ┳ ┻ ╋
```

**Double box-drawing**
```
╔ ╗ ╚ ╝ ═ ║ ╠ ╣ ╦ ╩ ╬
```

**Rounded corners** (house style)
```
╭ ╮ ╰ ╯
```

**Block fills** — full to thin, anchored left
```
█ ▉ ▊ ▋ ▌ ▍ ▎ ▏
```

**Block fills** — low to full, anchored bottom
```
▁ ▂ ▃ ▄ ▅ ▆ ▇ █
```

**Halves & shades**
```
▀ ▄ ▌ ▐  ░ ▒ ▓
```

**Marks & arrows** (text variants — no emoji)
```
→ ← ↑ ↓ ↔ ↕ ▶ ◀ ▲ ▼
● ○ ◉ ◆ ◇ ■ □ ▪ ▫
★ ☆ ✓ ✗ ✕ · • ◦ ‣
```

**Dividers** — light, heavy, double, dashed, dotted
```
─────  ━━━━━  ═════
┄┄┄┄┄  ┈┈┈┈┈  ╌╌╌╌╌
```

---

## ❌ Unsafe — double-width or variable (never inside a frame)

- **All emoji**: 🏆 🔥 ✅ ❌ 🚛 📊 ⭐ … — every one is ~2 cells.
- **Emoji-presentation variants**: `✔️ ❌ ⭐️ ➡️` (a base glyph + U+FE0F). Use the
  plain text twin instead: `✓ ✗ ★ →`.
- **CJK / full-width**: 全角 ， 。 — 2 cells.
- **Zero-width joiners & modifiers**: skin tones, ZWJ sequences — unpredictable.
- **Tabs** (`\t`): expand to a client-dependent stop — banned by R5.

### The `✓` vs `✔️` trap

| You type | Codepoints | Cells | Verdict |
|----------|-----------|-------|---------|
| `✓` | U+2713 | 1 | ✅ safe in frames |
| `✔️` | U+2714 U+FE0F | 2 | ❌ breaks alignment |
| `✗` | U+2717 | 1 | ✅ safe in frames |
| `❌` | U+274C | 2 | ❌ breaks alignment |
| `★` | U+2605 | 1 | ✅ safe in frames |
| `⭐` | U+2B50 | 2 | ❌ breaks alignment |

When you want a tick or a star inside a box, reach for the **single-cell text
glyph**. Save the colorful emoji for the line *above* the fence.

---

## Quick copy block

The everyday working set, ready to paste:

```
╭ ╮ ╰ ╯ ─ │
┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
█ ▓ ▒ ░  ▁▂▃▄▅▆▇█
→ ● ○ ✓ ✗ ★ ·
```
