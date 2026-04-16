from backend.config import HIGH_EXTREMITY, LOW_EXTREMITY, DEFAULT_LINE_THICKNESS, DEFAULT_DOT_SIZE

def draw(pen):

    half = DEFAULT_LINE_THICKNESS // 2

    # Top line
    pen.moveTo((LOW_EXTREMITY, HIGH_EXTREMITY + half))
    pen.lineTo((HIGH_EXTREMITY, HIGH_EXTREMITY + half))
    pen.lineTo((HIGH_EXTREMITY, HIGH_EXTREMITY - half))
    pen.lineTo((LOW_EXTREMITY, HIGH_EXTREMITY - half))
    pen.closePath()

    # Left line
    pen.moveTo((LOW_EXTREMITY - half, LOW_EXTREMITY))
    pen.lineTo((LOW_EXTREMITY + half, LOW_EXTREMITY))
    pen.lineTo((LOW_EXTREMITY + half, HIGH_EXTREMITY))
    pen.lineTo((LOW_EXTREMITY - half, HIGH_EXTREMITY))
    pen.closePath()

    dot_size = DEFAULT_DOT_SIZE
    center = (500, 500)
    pen.moveTo((center[0]-dot_size, center[1]-dot_size))
    pen.lineTo((center[0]+dot_size, center[1]-dot_size))
    pen.lineTo((center[0]+dot_size, center[1]+dot_size))
    pen.lineTo((center[0]-dot_size, center[1]+dot_size))
    pen.closePath()