# Sunday 22 November 2026 — one day of world news, one picture

Entry for the make.fun bounty `news-image-20261122`: sum up 22 November's
world news in one image.

The front page carries 50 sourced stories: a giant date masthead, a
"BY THE NUMBERS" strip of verifiable figures, a UTC timeline, 4 big
illustrated headlines, 12 secondary stories, and an "ALSO ON" list to
reach 50 — plus a schematic world map and a "DATE CHECK" note listing
the near-miss stories that were deliberately left out because they
belong to other days. Every story carries a source, and one-sided
claims are marked CLAIM. All artwork is flat vector drawing; there are
no photographs of real people.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies the pre-rendered `entry.png` to the output directory
unchanged, so two runs always write identical bytes. The image itself
was rendered offline (see `entry.png`, 1024×1024 PNG, 231,463 bytes).

## Result

- Prize pool: $100 total (1st $20), escrowed; entries close 2026-11-24T00:00Z.
- Self-score before submitting: 90/100 (breadth 30/30, readability 24/30,
  faithfulness 20/20, craft 16/20).
