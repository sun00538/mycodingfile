"""
File: 
Name:Jim (1 hour)
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
start = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(circle_line)


def circle_line(event):
    global start
    if not start:
        start = GOval(SIZE, SIZE, x=event.x-SIZE//2, y=event.y-SIZE//2)
        window.add(start)
    else:
        window.remove(start)
        line = GLine(x0=start.x, y0=start.y, x1=event.x, y1=event.y)
        window.add(line)
        start = None


if __name__ == "__main__":
    main()
