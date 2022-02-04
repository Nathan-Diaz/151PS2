#######################################
# Name:
# Collaborators:
# Estimated time spent (hr):
#######################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

height = 400
width = 600
gw = GWindow(width, height)
stripe_colors = ["red","orange","yellow","green","blue","purple"]

def draw_flag():
    gw = GWindow(width, height)
    draw_stripe()

def draw_stripe():
    for y in range(height):
        for x in range(width):
            r = GRect(x, y, 1, 1)
            stripe_number = y // 67
            r.set_color(stripe_colors[stripe_number])
            gw.add(r)

draw_flag()
