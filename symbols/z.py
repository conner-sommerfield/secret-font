from config import HIGH_EXTREMITY, LOW_EXTREMITY, DEFAULT_LINE_THICKNESS, DEFAULT_DOT_SIZE, DEFAULT_GLYPH_WIDTH

def draw(pen):

    half = DEFAULT_LINE_THICKNESS // 2
    dot_size = DEFAULT_DOT_SIZE
    center_x = DEFAULT_GLYPH_WIDTH // 2

    # Bottom line
    pen.moveTo((LOW_EXTREMITY, LOW_EXTREMITY - half))
    pen.lineTo((HIGH_EXTREMITY, LOW_EXTREMITY - half))
    pen.lineTo((HIGH_EXTREMITY, LOW_EXTREMITY + half))
    pen.lineTo((LOW_EXTREMITY, LOW_EXTREMITY + half))
    pen.closePath()

    # Bottom dot
    pen.moveTo((center_x - dot_size, 400 - dot_size))
    pen.lineTo((center_x + dot_size, 400 - dot_size))
    pen.lineTo((center_x + dot_size, 400 + dot_size))
    pen.lineTo((center_x - dot_size, 400 + dot_size))
    pen.closePath()

    # Middle line
    pen.moveTo((LOW_EXTREMITY, 600 - half))
    pen.lineTo((HIGH_EXTREMITY, 600 - half))
    pen.lineTo((HIGH_EXTREMITY, 600 + half))
    pen.lineTo((LOW_EXTREMITY, 600 + half))
    pen.closePath()

    # Top dot
    pen.moveTo((center_x - dot_size, HIGH_EXTREMITY - dot_size))
    pen.lineTo((center_x + dot_size, HIGH_EXTREMITY - dot_size))
    pen.lineTo((center_x + dot_size, HIGH_EXTREMITY + dot_size))
    pen.lineTo((center_x - dot_size, HIGH_EXTREMITY + dot_size))
    pen.closePath()
