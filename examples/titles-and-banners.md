# The art of titles & banners

A title sets the tone of a message before the first word is read. These all stay
≤ 26 columns and use one border family.

## Underline styles

```
RELEASE NOTES
═════════════
```

```
weekly digest
─────────────
```

```
WARNING
━━━━━━━
```

## Boxed title

```
╭────────────────────────╮
│ DAILY STANDUP          │
╰────────────────────────╯
```

## Centered title

```
╭────────────────────────╮
│      CHANGELOG         │
╰────────────────────────╯
```

## Letter-spaced wordmark

```
╭────────────────────────╮
│  W · A · S · C · I · I │
╰────────────────────────╯
```

## Double-rule header

```
╔════════════════════════╗
║ Q2 REVIEW              ║
╚════════════════════════╝
```

## Section divider (between blocks)

```
──────── · ──────── · ───
```

## Tag / pill

```
[ NEW ]  [ BETA ]  [ v2 ]
```

> For a centered title, compute the leftover space inside the field and split it
> in two: `left = floor(pad/2)`, `right = ceil(pad/2)`. Odd leftovers get the
> extra space on the right.
