#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble /workspace/pd-jianpu/repo ready for gh repo create."""
from __future__ import annotations
import csv
import shutil
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog_data import SONGS

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT / "repo"
JPS_SRC = ROOT / "jps"
PNG_SRC = ROOT / "png"

def main():
    if REPO.exists():
        shutil.rmtree(REPO)
    (REPO / "jps").mkdir(parents=True)
    (REPO / "png").mkdir(parents=True)
    (REPO / "scripts").mkdir(parents=True)

    # copy jps
    for p in JPS_SRC.glob("*.jps"):
        shutil.copy2(p, REPO / "jps" / p.name)
    # copy png (primary slug.png or slug-p1 + full)
    for s in SONGS:
        slug = s["slug"]
        primary = PNG_SRC / f"{slug}.png"
        if primary.exists():
            shutil.copy2(primary, REPO / "png" / primary.name)
        else:
            # multi-page: copy pages + full if present
            pages = sorted(PNG_SRC.glob(f"{slug}-p*.png"))
            for p in pages:
                shutil.copy2(p, REPO / "png" / p.name)
            full = PNG_SRC / f"{slug}_full.png"
            if full.exists():
                shutil.copy2(full, REPO / "png" / full.name)
            elif pages:
                # use p1 as representative named slug.png
                shutil.copy2(pages[0], REPO / "png" / f"{slug}.png")

    # scripts
    for name in ("catalog_data.py", "generate_jps.py", "render_all.py", "build_repo.py"):
        shutil.copy2(ROOT / "scripts" / name, REPO / "scripts" / name)

    # catalog.csv
    with (REPO / "catalog.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["index", "slug", "title", "key", "meter", "source", "jps", "png"])
        for i, s in enumerate(SONGS, 1):
            title = " / ".join(s["titles"])
            png_name = f"{s['slug']}.png"
            if not (REPO / "png" / png_name).exists():
                pages = sorted((REPO / "png").glob(f"{s['slug']}-p*.png"))
                png_name = pages[0].name if pages else ""
            w.writerow([i, s["slug"], title, s["key"], s["meter"], s["source"], f"{s['slug']}.jps", png_name])

    # catalog.md
    lines = ["# Catalog / 曲目目录", "",
             "| # | Title | Key | Meter | File | Source |",
             "|---|-------|-----|-------|------|--------|"]
    for i, s in enumerate(SONGS, 1):
        title = " / ".join(s["titles"])
        lines.append(f"| {i} | {title} | {s['key']} | {s['meter']} | `{s['slug']}` | {s['source']} |")
    (REPO / "catalog.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # LICENSE CC0
    (REPO / "LICENSE").write_text("""Creative Commons Legal Code

CC0 1.0 Universal

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
    PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
    THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
    HEREUNDER.

Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator
and subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for
the purpose of contributing to a commons of creative, cultural and
scientific works ("Commons") that the public can reliably and without fear
of later claims of infringement build upon, modify, incorporate in other
works, reuse and redistribute as freely as possible in any form whatsoever
and for any purposes, including without limitation commercial purposes.
These owners may contribute to the Commons to promote the ideal of a free
culture and the further production of creative, cultural and scientific
works, or to gain reputation or greater distribution for their Work in
part through the use and efforts of others.

For these and/or other purposes and without any expectation of additional
consideration or compensation, the person associating CC0 with a Work
(the "Affirmer"), to the extent that he or she is an owner of Copyright
and Related Rights in the Work, voluntarily elects to apply CC0 to the
Work and publicly distribute the Work under its terms, with knowledge of
his or her Copyright and Related Rights in the Work and the meaning and
intended legal effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be
protected by copyright and related or neighboring rights ("Copyright and
Related Rights"). Copyright and Related Rights include, but are not
limited to, the following:

  i. the right to reproduce, adapt, distribute, perform, display,
     communicate, and translate a Work;
 ii. moral rights retained by the original author(s) and/or performer(s);
iii. publicity and privacy rights pertaining to a person's image or
     likeness depicted in a Work;
 iv. rights protecting against unfair competition in regards to a Work,
     subject to the limitations in paragraph 4(a), below;
  v. rights protecting the extraction, dissemination, use and reuse of data
     in a Work;
 vi. database rights (such as those arising under Directive 96/9/EC of the
     European Parliament and of the Council of 11 March 1996 on the legal
     protection of databases, and under any national implementation
     thereof, including any amended or successor version of such
     directive); and
vii. other similar, equivalent or corresponding rights throughout the
     world based on applicable law or treaty, and any national
     implementations thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention
of, applicable law, Affirmer hereby overtly, fully, permanently,
irrevocably and unconditionally waives, abandons, and surrenders all of
Affirmer's Copyright and Related Rights and associated claims and causes
of action, whether now known or unknown (including existing as well as
future claims and causes of action), in the Work (i) in all territories
worldwide, (ii) for the maximum duration provided by applicable law or
treaty (including future time extensions), (iii) in any current or future
medium and for any number of copies, and (iv) for any purpose whatsoever,
including without limitation commercial, advertising or promotional
purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
member of the public at large and to the detriment of Affirmer's heirs and
successors, fully intending that such Waiver shall not be subject to
revocation, rescission, cancellation, termination, or any other legal or
equitable action to disrupt the quiet enjoyment of the Work by the public
as contemplated by Affirmer's express Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason
be judged legally invalid or ineffective under applicable law, then the
Waiver shall be preserved to the maximum extent permitted taking into
account Affirmer's express Statement of Purpose. In addition, to the
extent the Waiver is so judged Affirmer hereby grants to each affected
person a royalty-free, non transferable, non sublicensable, non exclusive,
irrevocable and unconditional license to exercise Affirmer's Copyright and
Related Rights in the Work (i) in all territories worldwide, (ii) for the
maximum duration provided by applicable law or treaty (including future
time extensions), (iii) in any current or future medium and for any number
of copies, and (iv) for any purpose whatsoever, including without
limitation commercial, advertising or promotional purposes (the
"License"). The License shall be deemed effective as of the date CC0 was
applied by Affirmer to the Work. Should any part of the License for any
reason be judged legally invalid or ineffective under applicable law, such
partial invalidity or ineffectiveness shall not invalidate the remainder
of the License, and in such case Affirmer hereby affirms that he or she
will not (i) exercise any of his or her remaining Copyright and Related
Rights in the Work or (ii) assert any associated claims and causes of
action with respect to the Work, in either case contrary to Affirmer's
express Statement of Purpose.

4. Limitations and Disclaimers.

 a. No trademark or patent rights held by Affirmer are waived, abandoned,
    surrendered, licensed or otherwise affected by this document.
 b. Affirmer offers the Work as-is and makes no representations or
    warranties of any kind concerning the Work, express, implied,
    statutory or otherwise, including without limitation warranties of
    title, merchantability, fitness for a particular purpose, non
    infringement, or the absence of latent or other defects, accuracy, or
    the present or absence of errors, whether or not discoverable, all to
    the greatest extent permissible under applicable law.
 c. Affirmer disclaims responsibility for clearing rights of other persons
    that may apply to the Work or any use thereof, including without
    limitation any person's Copyright and Related Rights in the Work.
    Further, Affirmer disclaims responsibility for obtaining any necessary
    consents, permissions or other rights required for any use of the
    Work.
 d. Affirmer understands and acknowledges that Creative Commons is not a
    party to this document and has no duty or obligation with respect to
    this CC0 or use of the Work.
""", encoding="utf-8")

    readme = """# Public-Domain Jianpu Sheets / 公有领域简谱图集

100 short **public-domain** melodies engraved as numbered musical notation (**简谱 / jianpu**) PNG images, generated with the open-source [yetist/jianpu-spec](https://github.com/yetist/jianpu-spec) `jps2svg` renderer.

本仓库收录 **100 首公有领域** 短曲的简谱 PNG，使用开源番茄简谱脚本规范本地渲染。

## What’s inside / 内容

| Path | Description |
|------|-------------|
| `png/` | Rendered jianpu sheet images (one primary PNG per piece) |
| `jps/` | Source tomato-jianpu scripts (`.jps`) |
| `catalog.csv` / `catalog.md` | Index: title, key, meter, source note, filenames |
| `scripts/` | Reproducible generators (`catalog_data.py`, `generate_jps.py`, `render_all.py`) |
| `LICENSE` | **CC0 1.0** dedication for the engraved images & scripts in this repo |

## Public domain statement / 公有领域声明

- Every piece is a **traditional folk / nursery / hymn** tune or a **classical theme** whose composer died long enough ago that the underlying melody is treated as public domain under common US and PRC practice (prefer composers deceased before 1955, or anonymous traditional repertoire).
- 每首均为传统民歌/儿歌/赞美诗曲调，或作曲家去世已久的古典主题；按美国与中国常见公有领域实践收录。
- Sources are noted per piece in the `.jps` `Z:` header and in `catalog.csv`.
- These files encode **simple melodic outlines** for education/reference — **not** modern copyrighted arrangements, accompaniments, or sound recordings.
- If you believe a specific engraving incorrectly includes protected material, please open an issue; we will remove or replace it.

## How it was rendered / 如何渲染

```bash
# 1) write .jps from catalog
python3 scripts/generate_jps.py

# 2) need yetist/jianpu-spec + venv with svgwrite, cairosvg, Pillow
python3 scripts/render_all.py
```

Toolchain: `jianpu-spec/bin/jps2svg.py` → SVG → `cairosvg` (scale=2) → PNG. CJK titles use Noto CJK fonts.

## Suggested clone usage

```bash
gh repo create pd-jianpu-sheets --public --source=. --remote=origin --push
```

## Credits

- Renderer / 规范与渲染器: [yetist/jianpu-spec](https://github.com/yetist/jianpu-spec)
- Melodic facts drawn from well-known PD repertoire; jianpu encodings prepared for this collection.
"""
    (REPO / "README.md").write_text(readme, encoding="utf-8")

    n_jps = len(list((REPO / "jps").glob("*.jps")))
    n_png = len(list((REPO / "png").glob("*.png")))
    print(f"Repo ready at {REPO}")
    print(f"jps={n_jps} png={n_png}")

if __name__ == "__main__":
    main()
