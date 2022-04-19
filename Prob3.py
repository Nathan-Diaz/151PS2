#######################################
# Name: Nathan G. Diaz
# Collaborators:
# Estimated time spent (hr):
#######################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

### Prepatory Code ###
height = 400
width = 600
gw = GWindow(width, height)
stripe_colors = ["red","orange","yellow","green","blue","purple"]

cx = width / 2
x_origin = cx / 2 

def draw_flag(): #Code that creates the flag
    gw = GWindow(width, height)
    draw_stripe(gw) #creates rainbow
    draw_triangle(gw) #adds singular triangle b/c I couldn't test and thus figure out how to make a triangle based outside of a two for loops
    make_text(gw) #adds text

def draw_stripe(gw):
    for y in range(height): # y is defined first because triangle will be created ontop of the stripes
        for x in range(width):
            stripe = GRect(x, y, 1, 1) # starts the stripes
            stripe_number = y // 67 # assignes each color a number based by 400 / 6 ~= 67
            stripe.set_color(stripe_colors[stripe_number]) # defines the stripe color based on 
            gw.add(stripe) # adds stripes by color one at a time

def draw_triangle():
        # Draws a 45-45-90 triangle of hypotenuse equal to height with hypotenuse along the x == 0 line.
    
        # We check (x,y) to see if the total distance of x from the left and y from the middle is greater than 500 // 2 == 25-
        # If not, we place a place rectangle at that x,y location.
        for y in range(height):
            for x in range(width):
                r = GRect(x,y,1,1)
                dist_x = x # distance from left
                dist_y = abs((height // 2) - y) # distance from middle
                dist_total = dist_x + dist_y
                
                if dist_total < height // 2:
                    r.set_color("black")
                    gw.add(r)

def make_text(gw):
    title = GLabel("Semi-Progessive Pride Flag", x_origin, height) # I am unsure if this is centered
    title.set_font("bold 20px 'serif'")
    gw.add(title)

draw_flag()
