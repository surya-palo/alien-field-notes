# Build log — Alien Field Notes: The Two Day Earth Review

## What the entry is

One original line, an alien tourist's review of Earth:

> 4/5 stars. The locals scoop their pets' droppings into little bags and carry them home like trophies. Would not walk here barefoot.

Second revision: cut the filler beat "Strange planet." — the brief rewards
tightness, and the line is stronger as rating + one observation + verdict,
with the punch landing on the last word.

## Why it fits the judge brief

- **Alien voice first:** the premise is unmistakable — a visitor watching
  Earthlings, not a human joke with an alien slapped on.
- **Funny from the alien angle:** the laugh comes from the visitor
  misreading an ordinary Earth habit (bagging dog droppings) as a proud
  trophy ritual.
- **Original:** avoids the first-obvious topics the brief warns about
  (traffic, gravity, money, weather); dog-waste bags are a specific,
  everyday detail few entrants would reach for.
- **Reads like a real review:** opens with a star rating, closes with a
  verdict ("Would not walk here barefoot.").
- **Tight, single joke:** one observation, no stacked jokes, no
  self-explanation; the punch lands on the last word.

## Verification

- `python3 main.py` run twice; `sha256sum /output/entry.txt` identical
  both times (deterministic, byte-identical output).
- Character count checked against the 200-character limit inside
  `main.py` (raises if out of range).
- `/output` contains only `entry.txt`, mode 0644.
- `main.py` uses Python stdlib only and writes with `open()` directly
  (no tempfile), then `os.chmod(..., 0o644)`.
