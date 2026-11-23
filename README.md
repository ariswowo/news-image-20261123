[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/ariswowo/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/ariswowo/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# News image — Monday 23 November 2026

Entry for make.fun bounty **news-image-20261123** —
["Sum up 23 November's world news in one image"](https://make.fun/bounty/news-image-20261123).

The image is a newspaper front page, "THE WORLD TODAY", dated
**Monday, 23 November 2026**, with five stories from that day:

1. **COP31 collapses** — the climate talks end with no deal on phasing out
   fossil fuels.
2. **Trump, Putin and Xi meet in Shenzhen** — the three leaders sign a
   declaration toward peace.
3. **AI selloff rocks markets** — Seoul stocks plunge 5% as AI shares tumble;
   South Korea's exports top $1 trillion.
4. **Russian warship sunk** — a suspected Ukrainian drone strike hits a
   frigate off Benghazi.
5. **Riemann Hypothesis claimed proved** — an Anthropic mathematician and
   Claude claim a proof of the 160-year-old maths problem.

See [NEWS.md](NEWS.md) for the story details and their sources, and
[TESTS.md](TESTS.md) for how the entry was verified.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled image
`entry.png` to `/output/entry.png`. No network, no clock, no randomness:
two runs write byte-identical output.

```sh
python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `main.py` — the entry program.
- `entry.png` — the image, 1024 x 1024, PNG, under 1 MiB.
- `NEWS.md` — the stories on the page and their sources.
- `TESTS.md` — verification notes.
- `LICENSE` — MIT.

## Prize

$100 in total: 1st $20, 2nd $12, 3rd $6, 4th–10th $2 each,
11th–50th $1.20 each. Entries close 25 November 2026, 00:00 UTC.
