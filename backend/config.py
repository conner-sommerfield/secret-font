# config.py
from pathlib import Path

FONT_NAME = "kasse"

PROJECT_ROOT = Path.cwd()

ASSETS_DIR = PROJECT_ROOT / "assets"
FONT_FILE = ASSETS_DIR / f"{FONT_NAME}.ttf"
GLYPH_DIR = ASSETS_DIR / "glyphs"

NOTDEF_FILENAME = ".notdef"

DEFAULT_GLYPH_WIDTH = 1000
DEFAULT_DOT_SIZE = 50
DEFAULT_LINE_THICKNESS = 100

HIGH_EXTREMITY = 900
LOW_EXTREMITY = 100

LETTERS_PACKAGE = "backend.symbols.letters"
NUMBERS_PACKAGE = "backend.symbols.numbers"