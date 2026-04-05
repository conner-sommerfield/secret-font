#!/usr/bin/env python3

import fontforge
import importlib
import string

from config import DEFAULT_GLYPH_WIDTH, LOW_EXTREMITY

FONT_NAME = "victorian"
OUTPUT_FILE = "victorian.ttf"
SYMBOLS_DIR = "symbols"

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
    pen.lineTo((700, LOW_EXTREMITY))
    pen.lineTo((700, 700))
    pen.lineTo((LOW_EXTREMITY, 700))
    pen.closePath()

def enumerate_letters(letters):
    for letter in letters:
        codepoint = ord(letter)
        glyph = font.createChar(codepoint, letter) 
        glyph.width = DEFAULT_GLYPH_WIDTH

        try:
            module = importlib.import_module(f"{SYMBOLS_DIR}.{letter.lower()}")
            module.draw(glyph.glyphPen())
        except ModuleNotFoundError:
            print(f"No symbol module for {letter}, skipping...")

define_notdef()

enumerate_letters(string.ascii_lowercase)
enumerate_letters(string.ascii_uppercase)

font.generate(OUTPUT_FILE)
print(f"Font created: {OUTPUT_FILE}")