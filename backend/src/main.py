#!/usr/bin/env python3

import fontforge
import importlib
import string

from config import DEFAULT_GLYPH_WIDTH, LOW_EXTREMITY, HIGH_EXTREMITY

FONT_NAME = "victorian"
OUTPUT_FILE = "victorian.ttf"
LETTERS_DIR = "symbols/letters"

font = fontforge.font()
font.fontname = FONT_NAME
font.fullname = FONT_NAME
font.familyname = FONT_NAME

def define_notdef():
    notdef_codepoint = 0
    notdef_filename = ".notdef"
    notdef = font.createChar(notdef_codepoint, notdef_filename)
    notdef.width = DEFAULT_GLYPH_WIDTH

    pen = notdef.glyphPen()
    pen.moveTo((LOW_EXTREMITY, LOW_EXTREMITY))
    pen.lineTo((HIGH_EXTREMITY, LOW_EXTREMITY))
    pen.lineTo((HIGH_EXTREMITY, HIGH_EXTREMITY))
    pen.lineTo((LOW_EXTREMITY, HIGH_EXTREMITY))
    pen.closePath()

def enumerate_symbols(symbols):
    for symbol in symbols:
        codepoint = ord(symbol)
        glyph = font.createChar(codepoint, symbol) 
        glyph.width = DEFAULT_GLYPH_WIDTH

        try:
            module = importlib.import_module(f"{LETTERS_DIR}.{symbol.lower()}")
            module.draw(glyph.glyphPen())
        except ModuleNotFoundError:
            print(f"No symbol module for {symbol}, skipping...")

define_notdef()

enumerate_symbols(string.ascii_lowercase)
enumerate_symbols(string.ascii_uppercase)

font.generate(OUTPUT_FILE)
print(f"Font created: {OUTPUT_FILE}")