#!/usr/bin/env python3
"""Create a 4:3 cinematic matte frame with a 16:9 active picture."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def parse_color(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise argparse.ArgumentTypeError("color must be a 6-digit hex value")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def create_frame(
    source_path: Path,
    output_path: Path,
    width: int,
    height: int,
    matte_color: tuple[int, int, int],
) -> None:
    if width * 3 != height * 4:
        raise ValueError("final canvas must be 4:3, for example 1440x1080")

    active_width = width
    active_height = round(width * 9 / 16)
    if active_height > height:
        active_height = height
        active_width = round(height * 16 / 9)

    source = Image.open(source_path).convert("RGB")
    active = ImageOps.fit(
        source,
        (active_width, active_height),
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    )

    canvas = Image.new("RGB", (width, height), matte_color)
    x = (width - active_width) // 2
    y = (height - active_height) // 2
    canvas.paste(active, (x, y))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--width", type=int, default=1440)
    parser.add_argument("--height", type=int, default=1080)
    parser.add_argument("--matte-color", type=parse_color, default=(0, 0, 0))
    args = parser.parse_args()
    create_frame(args.source, args.output, args.width, args.height, args.matte_color)


if __name__ == "__main__":
    main()
