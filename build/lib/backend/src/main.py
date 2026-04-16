#!/usr/bin/env python3

import fontforge
import importlib
import string
import logging

from backend.config import (
    FONT_NAME,
    FONT_FILE,
    NOTDEF_FILENAME,
    DEFAULT_GLYPH_WIDTH,
    LOW_EXTREMITY,
    HIGH_EXTREMITY,
    LETTERS_PACKAGE,
    NUMBERS_PACKAGE,
)


class FontGenerator:
    def __init__(self):
        self.logger = self._setup_logger()
        self.font = self._setup_font()

    def _setup_logger(self):
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(__name__)

    def _setup_font(self):
        font = fontforge.font()
        font.fontname = FONT_NAME
        font.fullname = FONT_NAME
        font.familyname = FONT_NAME
        return font

    def define_notdef(self):
        notdef = self.font.createChar(0, NOTDEF_FILENAME)
        notdef.width = DEFAULT_GLYPH_WIDTH

        pen = notdef.glyphPen()
        pen.moveTo((LOW_EXTREMITY, LOW_EXTREMITY))
        pen.lineTo((HIGH_EXTREMITY, LOW_EXTREMITY))
        pen.lineTo((HIGH_EXTREMITY, HIGH_EXTREMITY))
        pen.lineTo((LOW_EXTREMITY, HIGH_EXTREMITY))
        pen.closePath()

    def enumerate_symbols(self, symbols, package):
        for symbol in symbols:
            glyph = self.font.createChar(ord(symbol), symbol)
            glyph.width = DEFAULT_GLYPH_WIDTH

            module_name = f"{package}.{symbol.lower()}"

            try:
                module = importlib.import_module(module_name)
            except ModuleNotFoundError as e:
                self.logger.warning(f"No symbol module for '{symbol}', skipping...")
                continue

            if not hasattr(module, "draw"):
                self.logger.warning(f"{module_name} missing draw(), skipping...")
                continue

            module.draw(glyph.glyphPen())

    def generate_font(self):
        self.define_notdef()
        self.enumerate_symbols(string.ascii_lowercase, LETTERS_PACKAGE)
        self.enumerate_symbols(string.ascii_uppercase, LETTERS_PACKAGE)
        self.font.generate(str(FONT_FILE))
        self.logger.info(f"Font created: {FONT_FILE}")


def main():
    generator = FontGenerator()
    generator.generate_font()


if __name__ == "__main__":
    main()