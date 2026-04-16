from backend.config import (
    HIGH_EXTREMITY, 
    LOW_EXTREMITY, 
    DEFAULT_LINE_THICKNESS, 
    DEFAULT_DOT_SIZE
)

def draw(pen):

    half = DEFAULT_LINE_THICKNESS // 2
    dot_size = DEFAULT_DOT_SIZE

    # Top dot
    pen.moveTo((500-dot_size, HIGH_EXTREMITY-dot_size))
    pen.lineTo((500+dot_size, HIGH_EXTREMITY-dot_size))
    pen.lineTo((500+dot_size, HIGH_EXTREMITY+dot_size))
    pen.lineTo((500-dot_size, HIGH_EXTREMITY+dot_size))
    pen.closePath()

    # Middle line (thin rectangle)
    pen.moveTo((LOW_EXTREMITY, 500-half))
    pen.lineTo((HIGH_EXTREMITY, 500-half))
    pen.lineTo((HIGH_EXTREMITY, 500+half))
    pen.lineTo((LOW_EXTREMITY, 500+half))
    pen.closePath()

    # Bottom dot
    pen.moveTo((500-dot_size, LOW_EXTREMITY-dot_size))
    pen.lineTo((500+dot_size, LOW_EXTREMITY-dot_size))
    pen.lineTo((500+dot_size, LOW_EXTREMITY+dot_size))
    pen.lineTo((500-dot_size, LOW_EXTREMITY+dot_size))
    pen.closePath()