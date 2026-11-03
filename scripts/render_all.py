#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render all .jps to SVG then PNG via jps2svg + cairosvg."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path
import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
JPS = ROOT / "jps"
SVG = ROOT / "svg"
PNG = ROOT / "png"
JPS2SVG = Path("/workspace/jianpu-spec/bin/jps2svg.py")
PYBIN = Path("/workspace/jianpu-venv/bin/python")

SVG.mkdir(parents=True, exist_ok=True)
PNG.mkdir(parents=True, exist_ok=True)

def render_one(jps: Path) -> list[Path]:
    slug = jps.stem
    # clear old svg for this slug
    for old in SVG.glob(f"{slug}.svg"):
        old.unlink()
    for old in SVG.glob(f"{slug}-*.svg"):
        old.unlink()
    out_base = SVG / slug
    r = subprocess.run(
        [str(PYBIN), str(JPS2SVG), str(jps), "-o", str(out_base)],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        raise RuntimeError(f"jps2svg failed for {slug}: {r.stderr or r.stdout}")
    svgs = sorted(SVG.glob(f"{slug}.svg")) + sorted(SVG.glob(f"{slug}-*.svg"))
    if not svgs:
        raise RuntimeError(f"no svg produced for {slug}")
    pngs = []
    if len(svgs) == 1:
        png = PNG / f"{slug}.png"
        cairosvg.svg2png(url=str(svgs[0]), write_to=str(png), scale=2)
        pngs.append(png)
    else:
        pages = []
        for i, s in enumerate(svgs, 1):
            png = PNG / f"{slug}-p{i}.png"
            cairosvg.svg2png(url=str(s), write_to=str(png), scale=2)
            pngs.append(png)
            pages.append(Image.open(png).convert("RGB"))
        # stitch full
        w = max(im.width for im in pages)
        h = sum(im.height for im in pages)
        full = Image.new("RGB", (w, h), (255, 255, 255))
        y = 0
        for im in pages:
            full.paste(im, (0, y))
            y += im.height
        full_path = PNG / f"{slug}_full.png"
        full.save(full_path)
        pngs.append(full_path)
    return pngs

def main():
    files = sorted(JPS.glob("*.jps"))
    ok, bad = [], []
    for jps in files:
        try:
            pngs = render_one(jps)
            print("OK", jps.stem, "->", ", ".join(p.name for p in pngs))
            ok.append(jps.stem)
        except Exception as e:
            print("FAIL", jps.stem, e, file=sys.stderr)
            bad.append((jps.stem, str(e)))
    print(f"\nRendered {len(ok)}/{len(files)}; failures={len(bad)}")
    for slug, err in bad:
        print(" ", slug, err)
    return 0 if not bad else 1

if __name__ == "__main__":
    sys.exit(main())
