from backend.config import (
    HIGH_EXTREMITY, 
    LOW_EXTREMITY, 
    DEFAULT_LINE_THICKNESS, 
    DEFAULT_DOT_SIZE, 
    DEFAULT_GLYPH_WIDTH
)

def draw(pen):

    half = DEFAULT_LINE_THICKNESS // 2
    dot_size = DEFAULT_DOT_SIZE 
    center_x = DEFAULT_GLYPH_WIDTH // 2

    # Top line
    pen.moveTo((LOW_EXTREMITY, HIGH_EXTREMITY - half))
    pen.lineTo((HIGH_EXTREMITY, HIGH_EXTREMITY - half))
    pen.lineTo((HIGH_EXTREMITY, HIGH_EXTREMITY + half))
    pen.lineTo((LOW_EXTREMITY, HIGH_EXTREMITY + half))
    pen.closePath()

    # Middle dot
    pen.moveTo((center_x - dot_size, 500 - dot_size))
    pen.lineTo((center_x + dot_size, 500 - dot_size))
    pen.lineTo((center_x + dot_size, 500 + dot_size))
    pen.lineTo((center_x - dot_size, 500 + dot_size))
    pen.closePath()

    # Bottom line
    pen.moveTo((LOW_EXTREMITY, LOW_EXTREMITY - half))
    pen.lineTo((HIGH_EXTREMITY, LOW_EXTREMITY - half))
    pen.lineTo((HIGH_EXTREMITY, LOW_EXTREMITY + half))
    pen.lineTo((LOW_EXTREMITY, LOW_EXTREMITY + half))
    pen.closePath()