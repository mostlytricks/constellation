#!/usr/bin/env python3
"""constellation/compose -- deterministic deck-spec renderer.

Renders a deck-spec JSON to .pptx via python-pptx. No judgment: the
*composing* (idea x template x theme -> spec) is the agent's job, done
before this script runs -- the script only validates and draws. It is
also the seam's enforcement: a spec whose template/theme/box/token
references don't resolve is refused with every error listed.

Shapes are defined in ../DECK-SPEC.md (spec_version 0).

Usage:
    python build.py <deck-spec.json> [-o out.pptx]
"""
import argparse
import json
import sys
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Emu, Pt

ROOT = Path(__file__).resolve().parents[3]
TEMPLATES = ROOT / "library" / "templates"
THEMES = ROOT / "library" / "themes"
SLIDE_H_EMU = 6858000  # fixed height; width follows the spec's aspect


def load_json(path, what, errors):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{what} not found: {path}")
    except json.JSONDecodeError as e:
        errors.append(f"{what} is not valid JSON: {path} ({e})")
    return None


def validate(spec, templates, theme, errors):
    """Every cross-reference in the spec must resolve. Collects, never raises."""
    if spec.get("spec_version") != 0:
        errors.append(f"spec_version must be 0, got {spec.get('spec_version')!r}")
        return
    colors = theme["tokens"]["colors"]
    styles = theme["tokens"]["text_styles"]
    for style_name, style in styles.items():
        if style["color"] not in colors:
            errors.append(f"theme style '{style_name}' names unknown color token "
                          f"'{style['color']}'")

    for i, slide in enumerate(spec["slides"], start=1):
        where = f"slide {slide.get('n', '?')}"
        if slide.get("n") != i:
            errors.append(f"{where}: 'n' must be sequential (expected {i})")
        tpl = templates.get(slide["template"])
        if tpl is None:
            continue  # missing-template error already recorded at load
        if slide["role"] not in tpl["roles"] and not slide.get("stretch"):
            errors.append(f"{where}: role '{slide['role']}' is not in template "
                          f"'{tpl['template']}' roles {tpl['roles']} -- set "
                          f"\"stretch\": true if the stretch is intentional")
        boxes = {b["box"]: b for b in tpl["boxes"]}
        fill = slide.get("fill", {})
        for key, value in fill.items():
            box = boxes.get(key)
            if box is None or "text_style" not in box:
                errors.append(f"{where}: fill key '{key}' is not a text box of "
                              f"template '{tpl['template']}'")
            elif box.get("content") == "bullets" and not isinstance(value, list):
                errors.append(f"{where}: box '{key}' takes a bullet array, got "
                              f"{type(value).__name__}")
            elif box.get("content") != "bullets" and not isinstance(value, str):
                errors.append(f"{where}: box '{key}' takes a string, got "
                              f"{type(value).__name__}")
        for box in tpl["boxes"]:
            if "text_style" in box:
                if box["text_style"] not in styles:
                    errors.append(f"template '{tpl['template']}' box '{box['box']}': "
                                  f"unknown text_style '{box['text_style']}'")
                if box["box"] not in fill:
                    errors.append(f"{where}: text box '{box['box']}' has no fill "
                                  f"entry -- fill it or write a visible 'OPEN: ...' line")
            if "fill" in box and box["fill"] not in colors:
                errors.append(f"template '{tpl['template']}' box '{box['box']}': "
                              f"unknown color token '{box['fill']}'")


def emu_box(box, sw, sh):
    return (Emu(int(sw * box["x_pct"] / 100)), Emu(int(sh * box["y_pct"] / 100)),
            Emu(int(sw * box["w_pct"] / 100)), Emu(int(sh * box["h_pct"] / 100)))


def draw_fill(slide_obj, box, hex_color, sw, sh):
    x, y, w, h = emu_box(box, sw, sh)
    shape = slide_obj.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor.from_string(hex_color)
    shape.line.fill.background()


def draw_text(slide_obj, box, text, style, colors, sw, sh):
    x, y, w, h = emu_box(box, sw, sh)
    tf = slide_obj.shapes.add_textbox(x, y, w, h).text_frame
    tf.word_wrap = True
    lines = [f"• {item}" for item in text] if isinstance(text, list) else [text]
    for j, line in enumerate(lines):
        para = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
        if box.get("align") == "center":
            para.alignment = PP_ALIGN.CENTER
        run = para.add_run()
        run.text = line
        run.font.size = Pt(style["size_pt"])
        run.font.bold = style["bold"]
        run.font.color.rgb = RGBColor.from_string(colors[style["color"]])
        if "font" in style:
            run.font.name = style["font"]


def build(spec, templates, theme, out_path):
    colors = theme["tokens"]["colors"]
    styles = theme["tokens"]["text_styles"]
    prs = Presentation()
    prs.slide_height = Emu(SLIDE_H_EMU)
    prs.slide_width = Emu(int(SLIDE_H_EMU * spec["deck"]["aspect"]))
    sw, sh = prs.slide_width, prs.slide_height
    blank = next((l for l in prs.slide_layouts if l.name == "Blank"),
                 prs.slide_layouts[6])

    for slide in spec["slides"]:
        tpl = templates[slide["template"]]
        slide_obj = prs.slides.add_slide(blank)
        for box in tpl["boxes"]:
            if "fill" in box:
                draw_fill(slide_obj, box, colors[box["fill"]], sw, sh)
            if "text_style" in box:
                draw_text(slide_obj, box, slide["fill"][box["box"]],
                          styles[box["text_style"]], colors, sw, sh)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(out_path)


def verify(spec, out_path):
    """Round-read the built file: slide count matches, every slide has text."""
    prs = Presentation(out_path)
    slides = list(prs.slides)
    if len(slides) != len(spec["slides"]):
        sys.exit(f"VERIFY FAILED: built {len(slides)} slides, "
                 f"spec has {len(spec['slides'])}")
    for i, slide_obj in enumerate(slides, start=1):
        texts = [s.text_frame.text for s in slide_obj.shapes if s.has_text_frame]
        if not any(t.strip() for t in texts):
            sys.exit(f"VERIFY FAILED: slide {i} round-read with no text")
    return len(slides)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("spec", help="path to the deck-spec.json to render")
    ap.add_argument("-o", "--out", help="output .pptx path "
                    "(default: deck.pptx alongside the spec)")
    args = ap.parse_args()

    errors = []
    spec = load_json(args.spec, "deck-spec", errors)
    if errors:
        sys.exit("\n".join(f"ERROR: {e}" for e in errors))

    theme = load_json(THEMES / f"{spec['deck']['theme']}.theme.json", "theme", errors)
    templates = {}
    for name in {s["template"] for s in spec["slides"]}:
        tpl = load_json(TEMPLATES / f"{name}.template.json", f"template '{name}'", errors)
        if tpl:
            templates[name] = tpl
    if not errors:
        validate(spec, templates, theme, errors)
    if errors:
        sys.exit("\n".join(f"ERROR: {e}" for e in sorted(errors)))

    out = Path(args.out) if args.out else Path(args.spec).parent / "deck.pptx"
    build(spec, templates, theme, out)
    n = verify(spec, out)
    stretches = [s["n"] for s in spec["slides"] if s.get("stretch")]
    note = f"  (stretched slides: {stretches})" if stretches else ""
    print(f"wrote {out}  ({n} slides, verified round-read){note}")


if __name__ == "__main__":
    main()
