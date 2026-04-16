from backend.config import HIGH_EXTREMITY, LOW_EXTREMITY, DEFAULT_LINE_THICKNESS, DEFAULT_DOT_SIZE

def draw(pen):

    half = DEFAULT_LINE_THICKNESS // 2

    # Right line
    pen.moveTo((HIGH_EXTREMITY-200 - half, LOW_EXTREMITY-half))
    pen.lineTo((HIGH_EXTREMITY-200 + half, LOW_EXTREMITY-half))
    pen.lineTo((HIGH_EXTREMITY-200 + half, HIGH_EXTREMITY+half))
    pen.lineTo((HIGH_EXTREMITY-200 - half, HIGH_EXTREMITY+half))
    pen.closePath()

    dot_size = DEFAULT_DOT_SIZE
    center = (300, 500)
    pen.moveTo((center[0]-dot_size, center[1]-dot_size))
    pen.lineTo((center[0]+dot_size, center[1]-dot_size))
    pen.lineTo((center[0]+dot_size, center[1]+dot_size))
    pen.lineTo((center[0]-dot_size, center[1]+dot_size))
    pen.closePath()