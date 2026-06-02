# Bars, charts & sparklines

Block elements (`█▓▒░ ▁▂▃▄▅▆▇`) are single-cell, so they align perfectly. Keep
every line ≤ 26 columns.

## Progress bar

```
uploading
▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░  78%
```

## Labeled progress

```
build   ██████████  done
tests   ███████░░░  71%
deploy  ░░░░░░░░░░  idle
```

## Horizontal bar chart

```
weekly sales
mon ███████░░░   70
tue █████████░   92
wed ████░░░░░░   41
thu ██████████  100
fri ██████░░░░   63
```

## Sparkline (one line)

```
traffic ▁▂▄▆█▇▅▃▂▁▂▅
```

## Mini gauge

```
load  ▐████████▌░░  82%
```

## Rating row (single-cell stars)

```
score  ★★★★☆  4.0
```

> Build a bar: pick a track length (e.g. 10), fill `round(pct/10)` cells with `█`
> and the rest with `░`. Because both glyphs are one cell, the bar end always
> lands in the same column — so the trailing label stays aligned (R3).
