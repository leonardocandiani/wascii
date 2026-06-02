# Tables

WhatsApp has no real tables — you fake them with monospace columns. Left-align
text, right-align numbers, pad to fixed widths.

## Key / value

```
plan      pro
seats     5
renews    jun 14
status    active
```

## Bordered key / value

```
┌────────────────────────┐
│ plan      pro          │
│ seats     5            │
│ renews    jun 14       │
│ status    active       │
└────────────────────────┘
```

## Two columns, numbers right-aligned

```
item        qty
────────────────
coffee        2
filters      40
oat milk      1
```

## Three columns

```
day   in    out
───────────────
mon   09    18
tue   09    17
wed   10    16
```

## Boxed table with header rule

```
┌────────────────────────┐
│ name        score      │
├────────────────────────┤
│ ana         1,240      │
│ bruno       1,110      │
│ caio          980      │
└────────────────────────┘
```

> Right-align a number by left-padding with spaces until the column is full.
> `1,240` and `980` both end in the same column because `980` carries two leading
> spaces.
