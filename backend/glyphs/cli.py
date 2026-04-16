from pathlib import Path
import string
from PIL import Image, ImageDraw, ImageFont

from backend.config import (
    FONT_FILE, 
    GLYPH_DIR
)

from backend.glyphs.config import (
    FONT_SIZE,
    IMAGE_SIZE,
    BACKGROUND_COLOR,
    TEXT_COLOR,
    IMAGE_MODE,
)

def center_text(draw, char, font, image_size):
    bbox = draw.textbbox((0, 0), char, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (image_size[0] - text_width) / 2 - bbox[0]
    y = (image_size[1] - text_height) / 2 - bbox[1]

    return x, y


def draw_centered(draw, char, font, image_size, fill):
    x, y = center_text(draw, char, font, image_size)
    draw.text((x, y), char, font=font, fill=fill)


def setup_font():
    GLYPH_DIR.mkdir(parents=True, exist_ok=True)
    font = ImageFont.truetype(FONT_FILE, FONT_SIZE)
    return font


def generate_glyphs(font):
    for char in string.ascii_letters:
        img = Image.new(IMAGE_MODE, IMAGE_SIZE, BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)

        draw_centered(draw, char, font, IMAGE_SIZE, TEXT_COLOR)

        filename = f"{char}.png"
        img.save(GLYPH_DIR / filename)


def main():
    font = setup_font()
    generate_glyphs(font)


if __name__ == "__main__":
    main()