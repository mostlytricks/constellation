#!/usr/bin/env python3
"""Verify a composed deck's extracted structure against its source templates.

Run after build.py and extract.py. This is the deterministic half of the
full-circle gate: every rendered slide must preserve template box geometry and
theme tokens when it is read back through the analyzer.
"""
import argparse
import json
import sys
from pathlib import Path

# Consoles on Korean Windows default to cp949; printed deck data (em-dashes,
# Hangul, census symbols) must never crash on the console's codepage.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC = ROOT / "library" / "decks" / "constellation-intro" / "deck-spec.json"
DEFAULT_STRUCTURE = (
    ROOT / "library" / "analysis" / "constellation-intro-roundtrip" / "structure.json"
)


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"ERROR: not found: {path}")
    except json.JSONDecodeError as exc:
        sys.exit(f"ERROR: invalid JSON: {path} ({exc})")


def verify(spec, structure, tolerance):
    errors = []
    slides = structure.get("slides", [])
    if len(slides) != len(spec.get("slides", [])):
        errors.append(
            f"slide count: extracted {len(slides)} != spec {len(spec.get('slides', []))}"
        )
        return errors

    theme_path = ROOT / "library" / "themes" / f"{spec['deck']['theme']}.theme.json"
    theme = load_json(theme_path)

    for slide_spec, slide_dump in zip(spec["slides"], slides):
        template_path = (
            ROOT / "library" / "templates" / f"{slide_spec['template']}.template.json"
        )
        template = load_json(template_path)
        boxes = template["boxes"]
        shapes = slide_dump["shapes"]
        slide_n = slide_spec["n"]

        if len(shapes) != len(boxes):
            errors.append(
                f"slide {slide_n}: extracted {len(shapes)} shapes != "
                f"template {len(boxes)} boxes"
            )
            continue

        for box, shape in zip(boxes, shapes):
            box_name = box["box"]
            for key in ("x_pct", "y_pct", "w_pct", "h_pct"):
                actual = shape.get(key)
                expected = box[key]
                if actual is None or abs(actual - expected) > tolerance:
                    errors.append(
                        f"slide {slide_n} {box_name} {key}: "
                        f"{actual!r} != {expected!r} (tolerance {tolerance})"
                    )

            if "fill" in box:
                expected_fill = theme["tokens"]["colors"][box["fill"]]
                actual_fill = (shape.get("fill") or {}).get("rgb")
                if actual_fill != expected_fill:
                    errors.append(
                        f"slide {slide_n} {box_name}: fill {actual_fill!r} "
                        f"!= {expected_fill!r}"
                    )

            if "text_style" not in box:
                continue
            style = theme["tokens"]["text_styles"][box["text_style"]]
            census = shape.get("font_census", {})
            fonts = census.get("fonts", {})
            sizes = census.get("sizes_pt", {})
            colors = census.get("colors", {})
            run_count = sum(sizes.values())
            bold_runs = census.get("bold_runs", 0)
            expected_size = str(style["size_pt"])
            expected_color = theme["tokens"]["colors"][style["color"]]
            expected_bold = bool(style["bold"])
            expected_font = style.get("font")
            if expected_size not in sizes:
                errors.append(
                    f"slide {slide_n} {box_name}: missing text size {expected_size}"
                )
            if expected_color not in colors:
                errors.append(
                    f"slide {slide_n} {box_name}: missing text color {expected_color}"
                )
            if expected_bold and bold_runs != run_count:
                errors.append(
                    f"slide {slide_n} {box_name}: expected all {run_count} runs bold, "
                    f"found {bold_runs}"
                )
            if not expected_bold and bold_runs:
                errors.append(
                    f"slide {slide_n} {box_name}: expected no bold runs, "
                    f"found {bold_runs}"
                )
            if expected_font and expected_font not in fonts:
                errors.append(
                    f"slide {slide_n} {box_name}: missing font {expected_font!r}"
                )

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    parser.add_argument("--structure", type=Path, default=DEFAULT_STRUCTURE)
    parser.add_argument("--tolerance", type=float, default=0.1)
    args = parser.parse_args()

    errors = verify(load_json(args.spec), load_json(args.structure), args.tolerance)
    if errors:
        sys.exit("FULL-CIRCLE FAILED\n" + "\n".join(f"- {error}" for error in errors))
    slide_count = len(load_json(args.structure)["slides"])
    print(
        f"FULL-CIRCLE OK: {slide_count} slides match template geometry "
        "and theme tokens"
    )


if __name__ == "__main__":
    main()
