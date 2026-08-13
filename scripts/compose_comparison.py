#!/usr/bin/env python3
"""Compose original and claymation result into one comparison image."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def trim_solid_borders(image: Image.Image, tolerance: int, min_keep_ratio: float) -> Image.Image:
    """Trim near-solid outer borders while keeping the central photo content."""
    rgb = image.convert("RGB")
    width, height = rgb.size
    pixels = rgb.load()

    border_samples = []
    for x in range(width):
        border_samples.append(pixels[x, 0])
        border_samples.append(pixels[x, height - 1])
    for y in range(height):
        border_samples.append(pixels[0, y])
        border_samples.append(pixels[width - 1, y])

    bg = tuple(sorted(channel)[len(channel) // 2] for channel in zip(*border_samples))

    def different(pixel: tuple[int, int, int]) -> bool:
        return sum(abs(pixel[i] - bg[i]) for i in range(3)) > tolerance

    def near_black_line(points: list[tuple[int, int, int]]) -> bool:
        return all(max(pixel) <= tolerance for pixel in points)

    left, right = 0, width - 1
    top, bottom = 0, height - 1

    while top < bottom and (
        near_black_line([pixels[x, top] for x in range(width)])
        or not any(different(pixels[x, top]) for x in range(width))
    ):
        top += 1
    while bottom > top and (
        near_black_line([pixels[x, bottom] for x in range(width)])
        or not any(different(pixels[x, bottom]) for x in range(width))
    ):
        bottom -= 1
    while left < right and (
        near_black_line([pixels[left, y] for y in range(top, bottom + 1)])
        or not any(different(pixels[left, y]) for y in range(top, bottom + 1))
    ):
        left += 1
    while right > left and (
        near_black_line([pixels[right, y] for y in range(top, bottom + 1)])
        or not any(different(pixels[right, y]) for y in range(top, bottom + 1))
    ):
        right -= 1

    cropped_width = right - left + 1
    cropped_height = bottom - top + 1
    if cropped_width < width * min_keep_ratio or cropped_height < height * min_keep_ratio:
        return image
    if (left, top, right, bottom) == (0, 0, width - 1, height - 1):
        return image
    return image.crop((left, top, right + 1, bottom + 1))


def cover_resize(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def contain_resize(image: Image.Image, size: tuple[int, int], background: tuple[int, int, int]) -> Image.Image:
    fitted = ImageOps.contain(image, size, method=Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", size, background)
    x = (size[0] - fitted.width) // 2
    y = (size[1] - fitted.height) // 2
    canvas.paste(fitted.convert("RGB"), (x, y))
    return canvas


def compose(
    original_path: Path,
    result_path: Path,
    output_path: Path,
    mode: str,
    background: tuple[int, int, int],
    trim_original_borders: bool,
    trim_tolerance: int,
    min_keep_ratio: float,
) -> None:
    original = Image.open(original_path).convert("RGB")
    result = Image.open(result_path).convert("RGB")

    if trim_original_borders:
        original = trim_solid_borders(original, trim_tolerance, min_keep_ratio)

    width, height = original.size
    orientation = "portrait" if height > width else "landscape_or_square"

    if orientation == "portrait":
        section_size = (width, height)
        left = original
        right = cover_resize(result, section_size) if mode == "cover" else contain_resize(result, section_size, background)
        canvas = Image.new("RGB", (section_size[0] * 2, section_size[1]), background)
        canvas.paste(left, (0, 0))
        canvas.paste(right, (section_size[0], 0))
    else:
        section_size = (width, height)
        top = original
        bottom = cover_resize(result, section_size) if mode == "cover" else contain_resize(result, section_size, background)
        canvas = Image.new("RGB", (section_size[0], section_size[1] * 2), background)
        canvas.paste(top, (0, 0))
        canvas.paste(bottom, (0, section_size[1]))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path)


def parse_color(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise argparse.ArgumentTypeError("background must be a 6-digit hex color")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("original", type=Path)
    parser.add_argument("result", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--mode", choices=("cover", "contain"), default="cover")
    parser.add_argument("--background", type=parse_color, default=(255, 255, 255))
    parser.add_argument("--no-trim-original-borders", action="store_true")
    parser.add_argument("--trim-tolerance", type=int, default=24)
    parser.add_argument("--min-keep-ratio", type=float, default=0.55)
    args = parser.parse_args()
    compose(
        args.original,
        args.result,
        args.output,
        args.mode,
        args.background,
        not args.no_trim_original_borders,
        args.trim_tolerance,
        args.min_keep_ratio,
    )


if __name__ == "__main__":
    main()
