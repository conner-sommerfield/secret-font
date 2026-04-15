import os
import string
from PIL import Image, ImageDraw, ImageFont

# ----------------------------
# CONFIG
# ----------------------------
FONT_PATH = "victorian.ttf"
OUTPUT_DIR = "glyphs"

FONT_SIZE = 64
IMAGE_SIZE = (100, 100)

BACKGROUND_COLOR = "black"
TEXT_COLOR = "purple"

DRAW_OFFSET = (20, 10)
IMAGE_MODE = "RGB"

CHARSET = string.ascii_letters

# ----------------------------
# SETUP
# ----------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)

font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

# ----------------------------
# CENTER TEXT
# ----------------------------
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

# ----------------------------
# GENERATE GLYPHS
# ----------------------------
for char in CHARSET:
    codepoint = ord(char)

    img = Image.new(IMAGE_MODE, IMAGE_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    draw_centered(draw, char, font, IMAGE_SIZE, TEXT_COLOR)

    filename = f"{char}.png"
    img.save(os.path.join(OUTPUT_DIR, filename))