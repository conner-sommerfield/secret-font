from backend.config import HIGH_EXTREMITY, LOW_EXTREMITY, DEFAULT_LINE_THICKNESS

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

    # Right line
    pen.moveTo((HIGH_EXTREMITY - half, LOW_EXTREMITY))
    pen.lineTo((HIGH_EXTREMITY + half, LOW_EXTREMITY))
    pen.lineTo((HIGH_EXTREMITY + half, HIGH_EXTREMITY))
    pen.lineTo((HIGH_EXTREMITY - half, HIGH_EXTREMITY))
    pen.closePath()