# Public-Domain Jianpu Sheets / 公有领域简谱图集

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
