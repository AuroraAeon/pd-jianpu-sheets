#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate .jps files for all catalog songs."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog_data import SONGS

OUT = Path(__file__).resolve().parents[1] / "jps"
OUT.mkdir(parents=True, exist_ok=True)

HEADER = """#============================以下为描述头定义==========================
V: 1.0
{titles}
Z: {source}
Z: Public Domain / 公有领域｜rendered with yetist/jianpu-spec (jps2svg)
D: {key}
P: {meter}
{tempo_line}#============================以下开始简谱主体==========================
{body}
"""

def main():
    for s in SONGS:
        titles = "\n".join(f"B: {t}" for t in s["titles"])
        tempo = s.get("tempo") or ""
        tempo_line = f"J: {tempo}\n" if tempo else ""
        text = HEADER.format(
            titles=titles,
            source=s["source"],
            key=s["key"],
            meter=s["meter"],
            tempo_line=tempo_line,
            body=s["body"].strip() + "\n",
        )
        path = OUT / f"{s['slug']}.jps"
        path.write_text(text, encoding="utf-8")
        print("wrote", path.name)
    print(f"Done: {len(SONGS)} jps -> {OUT}")

if __name__ == "__main__":
    main()
