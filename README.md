<div align="center">

# wascii

### The art of ASCII for WhatsApp

Monospace boxes, bars, charts and leaderboards that **actually line up** on a phone — not just in your editor.

<img src="assets/whatsapp-mockup.png" alt="wascii rendering ASCII art inside a WhatsApp chat on an iPhone" width="300" />

<br>

![License](https://img.shields.io/badge/license-MIT-00d9ff?style=for-the-badge)
![Made for WhatsApp](https://img.shields.io/badge/made%20for-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)
![Claude Skill](https://img.shields.io/badge/Claude-Skill-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![PRs welcome](https://img.shields.io/badge/PRs-welcome-1a1a2e?style=for-the-badge)

</div>

---

## Why this exists

WhatsApp will render a perfectly aligned box on your laptop and **shatter it on a phone**. Send the same drawing without a code fence and it collapses into a proportional-font mess. The difference between art and garbage is a handful of rules about width, fences, and which glyphs are exactly one cell wide.

`wascii` is a [Claude](https://claude.com) **agent skill** (and a plain-English reference) that encodes those rules so structured chat visuals line up the first time, every time.

<div align="center">
<img src="assets/before-after.png" alt="The same table without and with wascii — proportional drift vs aligned monospace" width="300" />
</div>

Left bubble: no fence, proportional font, columns drift. Right bubble: one fenced block, ≤ 26 columns, perfectly square. Same data — one rule set apart.

---

## The seven rules

| # | Rule | Why |
|---|------|-----|
| **R0** | Always wrap it in a **fenced code block** (triple backticks) | WhatsApp only monospaces fenced text. No fence → no alignment. |
| **R1** | Never exceed **26 characters** per line | The narrowest iPhone wraps past ~26 cells, and a wrap detonates the drawing. |
| **R2** | **One glyph, one cell** — or don't use it | Emoji and CJK are double-width and shove every column out of line. |
| **R3** | **Pad** every inner line to the same width | The right border only lands true if every row is padded to one inner width. |
| **R4** | Pick **one border family** and commit | Light, heavy and double corners don't join. Rounded (`╭─╮`) is the house style. |
| **R5** | **Spaces only.** No tabs | Tabs expand to different stops on every client. |
| **R6** | **Emoji live outside** the frame | An emoji inside a box is the #1 way ASCII breaks on WhatsApp. |

> Full rationale with worked before/after examples in [`reference/rules.md`](reference/rules.md).

---

## Quick start

### As a Claude Code / agent skill

Drop the folder into your skills directory:

```bash
git clone https://github.com/leonardocandiani/wascii.git ~/.claude/skills/wascii
```

Now whenever your agent is about to send a box, table, bar or ranking to WhatsApp, it follows [`SKILL.md`](SKILL.md) — fence it, keep it ≤ 26 columns, single-cell glyphs only, emoji outside.

### As a human

Skim [`reference/characters.md`](reference/characters.md) for the safe glyph palette, grab a template from [`examples/`](examples), and paste it into a WhatsApp message **inside triple backticks**.

---

## The safe palette (the short version)

```
╭ ╮ ╰ ╯ ─ │
┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
█ ▓ ▒ ░  ▁▂▃▄▅▆▇█
→ ● ○ ✓ ✗ ★ ·
```

Everything above is **one cell wide**. The trap: `✓` (U+2713) is one cell, but `✔️` (U+2714 + emoji selector) is two. Inside a frame, always reach for the plain text glyph. Full table — including the `✓` vs `✔️` gotcha — in [`reference/characters.md`](reference/characters.md).

---

## Examples gallery

Copy-paste, all ≤ 26 columns, all phone-tested:

| File | What's inside |
|------|---------------|
| [`examples/boxes.md`](examples/boxes.md) | Frames, titled boxes, stat cards, callouts |
| [`examples/tables.md`](examples/tables.md) | Key/value and multi-column tables |
| [`examples/bars-and-charts.md`](examples/bars-and-charts.md) | Progress bars, bar charts, sparklines, gauges |
| [`examples/leaderboards.md`](examples/leaderboards.md) | Rankings, podiums, movement arrows |
| [`examples/titles-and-banners.md`](examples/titles-and-banners.md) | Section headers, wordmarks, dividers, pills |

A taste:

```
╭────────────────────────╮
│ DEPLOY                 │
├────────────────────────┤
│ status   live          │
│ region   gru1          │
│ uptime   99.98%        │
╰────────────────────────╯
```

```
mon ███████░░░   70
tue █████████░   92
wed ████░░░░░░   41
thu ██████████  100
```

---

## Contributing

New templates are welcome — the one hard rule: **every drawing must obey its own rules** (≤ 26 columns, one border family, zero emoji inside a frame). See [`CONTRIBUTING.md`](CONTRIBUTING.md). There's a width-check script in CI that rejects any block over 26 cells.

---

## License

MIT © [Leonardo Candiani](https://leonardocandiani.com.br) — see [`LICENSE`](LICENSE).

<div align="center">
<br>
<sub>Built for agents that talk to humans on WhatsApp.</sub>
</div>
